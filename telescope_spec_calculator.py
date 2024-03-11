import tkinter as tk
from tkinter import messagebox

def calculate_telescope_specifications(aperture, focal_length):
    focal_ratio = focal_length / aperture
    resolving_power = 116 / aperture
    magnification = focal_length / 50
    return focal_ratio, resolving_power, magnification

def calculate_focal_length(aperture, focal_ratio):
    return aperture * focal_ratio

def calculate_button_clicked():
    try:
        aperture = float(aperture_entry.get())
        focal_ratio = float(focal_ratio_entry.get())
        
        focal_length = calculate_focal_length(aperture, focal_ratio)
        focal_ratio_calculated, resolving_power, magnification = calculate_telescope_specifications(aperture, focal_length)
        
        result_text = f"Calculated Telescope Specifications:\n\n"
        result_text += f"Aperture: {aperture} mm\n"
        result_text += f"Focal Length: {focal_length:.2f} mm\n"
        result_text += f"Focal Ratio: f/{focal_ratio_calculated:.2f}\n"
        result_text += f"Resolving Power: {resolving_power:.2f} arc-seconds\n"
        result_text += f"Maximum Useful Magnification: {magnification:.2f}x"
        
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for Aperture and Focal Ratio.")

# Create main window
root = tk.Tk()
root.title("Telescope Specifications Calculator")

# Aperture entry
aperture_label = tk.Label(root, text="Aperture (mm):")
aperture_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

aperture_entry = tk.Entry(root)
aperture_entry.grid(row=0, column=1, padx=5, pady=5)

# Focal Ratio entry
focal_ratio_label = tk.Label(root, text="Focal Ratio (f/number):")
focal_ratio_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

focal_ratio_entry = tk.Entry(root)
focal_ratio_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, columnspan=2, padx=5, pady=10)

# Result label
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop()
