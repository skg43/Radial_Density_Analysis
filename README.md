# Radial Density Profile in a Nanopore

This project computes the radial density profile of particles confined within a nanopore, using atomic coordinate data from LAMMPS molecular dynamics simulations.  
It performs cylindrical shell binning over a central z-section and outputs a normalized density distribution.

---

## 📁 Project Structure

```
Radial_Density_Analysis/
├── input.inp                # Input file with number of frames per LAMMPS dump
├── dump/                    # Directory containing LAMMPS trajectory files
├── run/
│   ├── run.sh               # Shell script to launch analysis
│   ├── run.log              # Sample log (optional)
│   └── monomer_DP.txt       # Output: radial density data
├── src/
│   ├── Globals.py
│   ├── ParseFrames.py
│   ├── Reports.py
│   ├── ReadInput.py
│   └── run.py               # Main pipeline controller
```

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Edit `input.inp` to specify number of frames in each trajectory file.
3. Place your LAMMPS dump files (e.g., `dump-prod-pol-*.lmp`) in the `dump/` folder.
4. Execute the workflow:

```bash
cd run
bash run.sh
```

5. The output radial density data will be written to `run/monomer_DP.txt`.

---

## 📊 Output Format (`monomer_DP.txt`)

Each line contains:
```
radius   normalized_density   density   proportion   cumulative_proportion
```

- `radius`: radial distance from pore center
- `normalized_density`: density / total density
- `density`: raw shell density
- `proportion`: fraction of atoms in shell
- `cumulative_proportion`: integrated radial occupancy

---

## 🧠 Scientific Context

This method quantifies how particles distribute radially within a nanopore cross-section, useful for understanding confinement effects in soft matter, polymer, or protein transport simulations.

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for details.
