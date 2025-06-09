# Radial Density Analysis in a Nanopore

This repository contains scripts to compute the **radial density profile (DP)** of molecules (e.g., **Nup monomers**, **NTF2**, and **Kap proteins**) confined in a **cylindrical nanopore**, using **LAMMPS molecular dynamics** trajectory files as input.

Snapshots from simulations are analyzed to extract spatial distributions of particles across the radial direction (_r_) within a central axial slice of the pore (_z ∈ [−3 nm, 3 nm]_).

---

## 📂 Repository Structure

```
Radial_Density_Analysis/
├── input.inp               # Input file with frame count per trajectory
├── dump/                   # Folder for LAMMPS dump files (*.lmp)
├── run/
│   ├── run.sh              # Shell script to launch analysis
│   ├── run.log             # Sample log output
│   └── monomer_DP.txt      # Output: radial density data
├── src/
│   ├── Globals.py
│   ├── ParseFrames.py
│   ├── Reports.py
│   ├── ReadInput.py
│   └── run.py              # Main analysis controller
```

---

## 🧪 Scientific Background

This analysis quantifies how biomolecules distribute radially in the central region of a nanopore, which is critical for understanding selective transport mechanisms through crowded, confined environments such as the **nuclear pore complex (NPC)**.

### 📉 What It Computes

- Radial density distribution of specified molecules (e.g., FG-Nups, NTF2, Kapβ1)  
- Normalized density profile over cylindrical shells  
- Integrated cumulative density and occupancy  

### 📏 Analysis Region

Only molecules within a central region of the pore (**−3 nm < z < 3 nm**) are considered for density calculations.

---

## 📐 Normalization Equation

The radial density profile ( ψ(r) is normalized using the following condition:

2π L ∫₀ᴿ ψ(r)·r dr = N


Where:
- \( L \) is the length of the central region along the z-axis (here, 6 nm)
- \( r \) is the radial distance from the pore center (cylinder axis)
- \( N \) is the average number of molecules in the central region
- \( ψ(r) \) is the number density at distance \( r \)

---

## 📋 Output Format (`monomer_DP.txt`)

Each line contains the following columns:

```
radius   normalized_density   density   proportion   cumulative_proportion
```

- **radius**: distance from center of pore  
- **normalized_density**: normalized ψ(r)  
- **density**: raw molecule count in shell  
- **proportion**: shell's share of total molecule count  
- **cumulative_proportion**: integrated radial occupancy

---

## ⚙️ How to Run

1. Ensure Python 3 is installed.
2. Edit `input.inp` to specify the number of frames in each LAMMPS trajectory file.
3. Place `.lmp` files in the `dump/` directory.
4. From the `run/` directory, run:

```bash
bash run.sh
```

5. Output will be saved to `monomer_DP.txt`.

---

## 🧠 Applications

This code can be used to:
- Analyze biomolecular crowding in confined systems
- Compare density distributions between different transport proteins

---

## 📜 License

MIT License
