"""
Reports.py

Generates radial density profile reports from trajectory frame data.
Calculates cylindrical shell densities and writes out normalized profiles.

Developed by: Sanjeev Kumar Gautam
Date: 2025
"""

import sys
from Globals import *
import math

def Report(frames, total_frames, atoms_per_frame):
    """
    Compute and write radial density profile.

    Parameters:
    - frames (dict): Dictionary of trajectory frames with coordinates
    - total_frames (int): Total number of frames to process
    - atoms_per_frame (int): Number of atoms per frame
    """

    # Initialize variables for integration and tracking
    density_sum = 0  # Sum used for integration of density profile
    proportion = 0   # Fraction of particles in current shell
    integral = 0     # Final integral result
    cumulative_proportion = 0  # Running total of normalized particle proportions
    total_density = 0          # Total density across all shells
    total_monomers_in_range = 0  # Number of particles in the selected z-range
    total_atoms_in_bins = 0      # Total binned atoms across all frames

    # Allocate bins for radial density profile
    radial_bin_counts = [0 for _ in range(gl.n_bins + 1)]

    # Open output file for writing results
    output_file = open('../run/particle_DP.txt', 'w')

    # -----------------------------
    # First pass: Bin particles by radial distance
    # -----------------------------
    for frame_index in range(total_frames):
        for atom_index in range(atoms_per_frame):
            z = frames[str(frame_index)]["z"][atom_index]
            if gl.Entry_z < z < gl.Exit_z:  # Select atoms within z slice
                x = frames[str(frame_index)]["x"][atom_index]
                y = frames[str(frame_index)]["y"][atom_index]
                r = math.sqrt(x**2 + y**2)  # Compute radial distance
                bin_index = int(math.floor(r * gl.factor))  # Map to bin index

                if bin_index < 0:
                    # Log invalid bin index
                    print(f"bin_index= {bin_index} resid= {frames[str(frame_index)]['Resid'][atom_index]}")
                    bin_index = 0

                if bin_index <= gl.n_bins:
                    radial_bin_counts[bin_index] += 1  # Increment count for that bin
                    total_monomers_in_range += 1      # Track total included atoms

    # Total number of atoms across all bins
    total_atoms_in_bins = sum(radial_bin_counts)

    # Diagnostic output

    print("Total Atoms in the bins: %5.2f" % (total_atoms_in_bins / total_frames))

    # -----------------------------
    # Second pass: Compute total density
    # -----------------------------
    for j in range(1, len(radial_bin_counts)):
        r_center = j / gl.factor  # Bin center radius
        density = (float(radial_bin_counts[j]) / (2 * gl.pi * gl.Length * total_frames)) * (gl.n_bins / float(gl.max_dist)) / r_center  # ρ = n / (2πr h dr)
        total_density += density  # Accumulate for later normalization

    # -----------------------------
    # Third pass: Write density profile
    # -----------------------------
    for j in range(1, len(radial_bin_counts)):
        r_center = j / gl.factor  # Bin center in Å

        # Compute density again for this bin
        density = (float(radial_bin_counts[j]) / (2 * gl.pi * gl.Length * total_frames)) * (gl.n_bins / float(gl.max_dist)) / r_center

        # Normalize density by total density
        normalized_density = density / total_density if total_density > 0 else 0

        # Compute normalized proportion of total atoms
        proportion = radial_bin_counts[j] / total_atoms_in_bins * (gl.n_bins / float(gl.max_dist))

        # Cumulative normalized count (should approach 1.0)
        cumulative_proportion += proportion / (gl.n_bins / float(gl.max_dist))

        # Weighted sum for integration of r * ρ(r)
        density_sum += density * r_center

        # Write: radius | normalized_density | density | proportion | cumulative_proportion
        output_file.write(f"{r_center/10:.6f} 	 {normalized_density:.6f} 	 {density:.12f} 	 {proportion:.5f} 	 {cumulative_proportion:.5f}\n")

    # -----------------------------
    # Final integration of ρ(r) * 2πr dr over the cylinder
    # -----------------------------
    integral = density_sum * 2 * math.pi * gl.Length / (gl.n_bins / float(gl.max_dist))

    output_file.close()
    
    # Report integration results
    print("#############################################################")
    print(f"Integration = {integral:.5f}  Proportion = {proportion:.5f}  r = {gl.max_dist:.5f}  factor = {(gl.n_bins / float(gl.max_dist)):.2f}  Density_sum = {density_sum:.6f}  Total_density = {total_density:.10f}")
    print(f"Sum of all proportions = {cumulative_proportion:.2f} (should be ≈ 1)")
    print("############################### Results Written ##############################")
