# OrionPy 🐍

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build CI](https://github.com/<your-username>/OrionPy/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/OrionPy/actions)

**OrionPy** is a Python-based workflow to process astronomical FITS images, starting with the Orion Nebula (M42). It provides tools to load, calibrate, stretch, and combine stacked FITS frames into stunning grayscale and RGB composites. The workflow balances scientific accuracy with astrophotography aesthetics.

---

## Features

- Load and visualize FITS files
- Apply multiple stretch methods:
  - Logarithmic
  - Arcsinh (asinh)
  - Histogram equalization
- Combine multi-filter FITS images (R, V, B) into RGB composites
- Save outputs as PNG for quick previews or publication
- Pre-configured for Ruff linting, pre-commit hooks, and GitHub Actions CI

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Parikshith-S/OrionPy.git
cd OrionPy
```

2. **Install Poetry (if not installed)**
```bash
pip install poetry
```

3. **Install dependencies**
```bash
poetry install
```

4. **Activate Poetry shell (optional)**
```bash
poetry shell
```

---

## Usage

1. **Place your FITS files inside data/M42/:**
# M42

* [M42B_stack.fits](.\M42\M42B_stack.fits)
* [M42R_stack.fits](.\M42\M42R_stack.fits)
* [M42V_stack.fits](.\M42\M42V_stack.fits)

2. **Run the processing script**
```bash
poetry run python src/process.py
```

3. **Outputs will appear in the output/ folder:**
- Grayscale previews per channel:
    - M42_red_log.png, M42_green_asinh.png, etc.
- Color composites:
    - M42_rgb_asinh.png, M42_rgb_log.png, M42_rgb_hist.png

---

## Example Output

**RGB Composite (Arcsinh Stretch):**

**Grayscale Previews:**
- Red channel:
- Green channel:
- Blue channel:

Replace the image paths above with actual screenshots from your /output folder.

---

## Linting & Pre-Commit

**This project uses Ruff for linting and formatting, and pre-commit hooks for code quality.**

- Install hooks:
```bash
poetry run pre-commit install
```

- Manually check all files:
```bash
poetry run pre-commit run --all-files
```

---

## CI/CD
**The repo is pre-configured with GitHub Actions to run:**
- Ruff lint and formatting checks
- Pytest unit tests

## Lincense
**MIT License © Parikshith-S**
