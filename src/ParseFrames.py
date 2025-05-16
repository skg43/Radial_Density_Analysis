"""
Radial Density Profile Analysis - Frame Loader

Developed by: Sanjeev Kumar Gautam
Date: 2025

Description:
    Parses atomic coordinates from multiple LAMMPS trajectory files
    to prepare frame-wise data for radial density calculations.
    Targets a specific residue or atom range for analysis.
"""

import itertools as it
import concurrent.futures as cf
from Globals import *

def parse_frame(framescount, startline, endline, file_index):
    """
    Parses a single frame from a given LAMMPS dump file.

    Args:
        framescount (int): Global frame index
        startline (int): Start line of this frame in the dump file
        endline (int): End line of this frame in the dump file
        file_index (int): Index of the dump file being read

    Returns:
        dict: A dictionary with frame coordinates (x, y, z) and IDs
    """
    data = {"fc": [], "id": [], "Resid": [], "x": [], "y": [], "z": []}
    filename = f"../dump/dump-prod-pol-{gl.file_index + gl.START_INDEX}.lmp"

    with open(filename, 'r') as f:
        lines = it.islice(f, startline, endline)
        for line in lines:
            parts = line.split()
            if int(parts[1]) <= gl.N_Residue:
                data["fc"].append(framescount)
                data["id"].append(int(parts[0]))
                data["Resid"].append(int(parts[1]))
                data["x"].append(float(parts[3]))
                data["y"].append(float(parts[4]))
                data["z"].append(float(parts[5]))

    print(f"Loaded frame {framescount + 1} from {filename}")
    return data


def Load_all_Frames():
    """
    Loads all frames from all LAMMPS dump files using multiprocessing.

    Returns:
        all_data (dict): Dictionary of frame-indexed atom data
        total_frames (int): Total number of frames processed
        atoms_per_frame (int): Atom count in a single processed frame
    """
    total_frames = sum(gl.NO_FRAMES)
    frames = {}
    workers = [None] * total_frames
    current_frame = 0

    with cf.ProcessPoolExecutor() as executor:
        for gl.file_index, frame_count in enumerate(gl.NO_FRAMES):
            startline = gl.H_lines
            for i in range(frame_count):
                endline = startline + gl.ATOM_COUNT
                workers[current_frame] = executor.submit(parse_frame, current_frame, startline, endline, gl.file_index)
                startline = endline + gl.H_lines
                current_frame += 1

        for i in range(total_frames):
            frames[str(i)] = workers[i].result()

    atoms_per_frame = len(frames['0']['id'])
    print(atoms_per_frame)
    return frames, total_frames, atoms_per_frame
