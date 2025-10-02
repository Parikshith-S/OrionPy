from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure
import os


def load_fits(file_path):
    hdul = fits.open(file_path)
    data = hdul[0].data.astype(float)
    hdul.close()
    return data


def normalize(img):
    return (img - np.min(img)) / (np.max(img) - np.min(img))


# ---- Stretching Methods ----
def stretch_log(img):
    return np.log1p(normalize(img))


def stretch_asinh(img, factor=10):
    return np.arcsinh(normalize(img) * factor) / np.arcsinh(factor)


def stretch_hist_eq(img):
    return exposure.equalize_hist(normalize(img))


# ---- Save Helpers ----
def save_grayscale(data, out_path="output.png", method="log"):
    if method == "log":
        stretched = stretch_log(data)
    elif method == "asinh":
        stretched = stretch_asinh(data)
    elif method == "hist":
        stretched = stretch_hist_eq(data)
    else:
        stretched = normalize(data)

    plt.imsave(out_path, stretched, cmap="gray", origin="lower")


def combine_rgb(r_file, g_file, b_file, out="rgb.png", stretch="asinh"):
    r = load_fits(r_file)
    g = load_fits(g_file)
    b = load_fits(b_file)

    if stretch == "log":
        r, g, b = stretch_log(r), stretch_log(g), stretch_log(b)
    elif stretch == "asinh":
        r, g, b = stretch_asinh(r), stretch_asinh(g), stretch_asinh(b)
    elif stretch == "hist":
        r, g, b = stretch_hist_eq(r), stretch_hist_eq(g), stretch_hist_eq(b)
    else:
        r, g, b = normalize(r), normalize(g), normalize(b)

    rgb = np.dstack([r, g, b])
    plt.imsave(out, rgb, origin="lower")


# ---- Main Workflow ----
if __name__ == "__main__":
    base = "data/M42"

    r_file = os.path.join(base, "M42R_stack.fits")
    g_file = os.path.join(base, "M42V_stack.fits")  # V as Green
    b_file = os.path.join(base, "M42B_stack.fits")

    # Save grayscale with different stretches
    for method in ["log", "asinh", "hist"]:
        save_grayscale(load_fits(r_file), f"output/M42_red_{method}.png", method)
        save_grayscale(load_fits(g_file), f"output/M42_green_{method}.png", method)
        save_grayscale(load_fits(b_file), f"output/M42_blue_{method}.png", method)

    # Combine into RGB with arcsinh stretch (default)
    combine_rgb(r_file, g_file, b_file, "output/M42_rgb_asinh.png", stretch="asinh")
    combine_rgb(r_file, g_file, b_file, "output/M42_rgb_log.png", stretch="log")
    combine_rgb(r_file, g_file, b_file, "output/M42_rgb_hist.png", stretch="hist")

    print("✅ M42 processing complete. Check /output for results.")
