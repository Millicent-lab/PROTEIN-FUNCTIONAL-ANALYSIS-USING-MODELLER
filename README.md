# PROTEIN-FUNCTIONAL-ANALYSIS-USING-MODELLER
A Python script for automated protein structure modeling using Modeller, with built-in alignment validation.
# Protein Modelling Automation Script (Modeller)

This repository contains a Python script that automates homology modeling using [Modeller](https://salilab.org/modeller/). It includes a custom sequence validator to ensure the alignment file is correctly formatted before model building.

---

## 🧬 Features

- ✅ Checks `.ali` alignment files for invalid residues or formatting errors
- ✅ Builds **wildtype** and **mutant** protein models using Modeller’s `AutoModel`
- ✅ Supports assessment via **DOPE** and **GA341** scoring methods
- ✅ Prints useful console logs for user feedback

---

## 🧰 Requirements

- [Modeller](https://salilab.org/modeller/) (Python interface)
- Python 3.6+
- A valid `.ali` alignment file
- A known structure from PDB or AlphaFold for homology

---

## 🚀 How to Use

1. **Install Modeller** (requires registration):  
   https://salilab.org/modeller/download_installation.html

2. **Prepare Your Files**:
   - A valid `.ali` alignment file (wildtype + mutant sequences)
   - The template PDB (e.g., AlphaFold model ID or PDB ID)

3. **Edit the Script**:
   - Update paths to your `.ali` file and template model ID in the `__main__` block:
     ```python
     alnfile = r"C:\Users\millicent\Downloads\gp173_modeling.ali"
     ```

4. **Run the Script**:
   ```bash
   python modeller_script.py
