import tkinter as tk

#Celsius to {} conversion functions

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def celsius_to_fahrenheit(celsius):
    return (9 / 5) * celsius + 32

def celsius_to_rankine(celsius):
    return (9 / 5) * celsius + 491.67

def celsius_to_reaumur(celsius):
    return celsius * (4 / 5)

def celsius_to_triple_point_of_water(celsius):
    return celsius / 273.16

#Kelvin to {} conversion functions

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (9 / 5) * (kelvin - 273.15) + 32

def kelvin_to_rankine(kelvin):
    return kelvin * 1.8 + 491.67

def kelvin_to_reaumur(kelvin):
    return (kelvin - 273.15) * (4 / 5)

def kelvin_to_triple_point_of_water(kelvin):
    return (kelvin - 273.15) / 273.16


#Fahrenheit to {} conversion functions

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def fahrenheit_to_kelvin(fahrenheit):
    return (5 / 9) * (fahrenheit - 32) + 273.15

def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67

def fahrenheit_to_reaumur(fahrenheit):
    return (fahrenheit - 32) * (4 / 9)

def fahrenheit_to_triple_point_of_water(fahrenheit):
    return (fahrenheit - 32) / 1.8

#Rankine to {} conversion functions

def rankine_to_celsius(rankine):
    return (5 / 9) * (rankine - 491.67)

def rankine_to_kelvin(rankine):
    return (rankine - 491.67) / 1.8

def rankine_to_fahrenheit(rankine):
    return rankine - 459.67

def rankine_to_reaumur(rankine):
    return (rankine - 491.67) * (4 / 9)

def rankine_to_triple_point_of_water(rankine):
    return (rankine - 491.67) / 1.8

#Reaumur to {} conversion functions

def reaumur_to_celsius(reaumur):
    return reaumur * (5 / 4)

def reaumur_to_kelvin(reaumur):
    return reaumur * (5 / 4) + 273.15

def reaumur_to_fahrenheit(reaumur):
    return reaumur * (9 / 4) + 32

def reaumur_to_rankine(reaumur):
    return reaumur * (9 / 4) + 491.67

def reaumur_to_triple_point_of_water(reaumur):
    return reaumur * 273.16

#Triple point of water to {} conversion functions

def triple_point_of_water_to_celsius(triple_point_of_water):
    return triple_point_of_water * 273.16

def triple_point_of_water_to_kelvin(triple_point_of_water):
    return triple_point_of_water * 273.16 + 273.15

def triple_point_of_water_to_fahrenheit(triple_point_of_water):
    return triple_point_of_water * 1.8 + 32

def triple_point_of_water_to_rankine(triple_point_of_water):
    return triple_point_of_water * 1.8 + 491.67

def triple_point_of_water_to_reaumur(triple_point_of_water):
    return triple_point_of_water / 273.16


#Temperature conversion functions

TEMP_CONVERSION_FUNCTIONS = {
    'C': {
        'K': celsius_to_kelvin,
        'F': celsius_to_fahrenheit,
        'R': celsius_to_rankine,
        'RE': celsius_to_reaumur,
        'TP': celsius_to_triple_point_of_water
    },
    'K': {
        'C': kelvin_to_celsius,
        'F': kelvin_to_fahrenheit,
        'R': kelvin_to_rankine,
        'RE': kelvin_to_reaumur,
        'TP': kelvin_to_triple_point_of_water
    },
    'F': {
        'C': fahrenheit_to_celsius,
        'K': fahrenheit_to_kelvin,
        'R': fahrenheit_to_rankine,
        'RE': fahrenheit_to_reaumur,
        'TP': fahrenheit_to_triple_point_of_water
    },
    'R': {
        'C': rankine_to_celsius,
        'K': rankine_to_kelvin,
        'F': rankine_to_fahrenheit,
        'RE': rankine_to_reaumur,
        'TP': rankine_to_triple_point_of_water
    },
    'RE': {
        'C': reaumur_to_celsius,
        'K': reaumur_to_kelvin,
        'F': reaumur_to_fahrenheit,
        'R': reaumur_to_rankine,
        'TP': reaumur_to_triple_point_of_water
    },
    'TP': {
        'C': triple_point_of_water_to_celsius,
        'K': triple_point_of_water_to_kelvin,
        'F': triple_point_of_water_to_fahrenheit,
        'R': triple_point_of_water_to_rankine,
        'RE': triple_point_of_water_to_reaumur
    }
    }

def convert():
    try:
        value = float(entry.get())
        conversion_func = TEMP_CONVERSION_FUNCTIONS[from_var.get()][to_var.get()]
        result = conversion_func(value)
        result_label.config(text="Result: {:.2f}".format(result))
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Temperature Converter")

from_var = tk.StringVar(root)
from_var.set("C")

to_var = tk.StringVar(root)
to_var.set("K")

from_menu = tk.OptionMenu(root, from_var, *TEMP_CONVERSION_FUNCTIONS.keys())
from_menu.grid(row=0, column=0, padx=10, pady=10)

to_menu = tk.OptionMenu(root, to_var, *TEMP_CONVERSION_FUNCTIONS.keys())
to_menu.grid(row=0, column=1, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()