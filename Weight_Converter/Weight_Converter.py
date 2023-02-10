import tkinter as tk

UNITS = {
    'g': 1,
    'kg': 1000,
    'lb': 454,
    't': 907185,
    'amu': 1.66054e-24,
    'ct': 0.2,
    'cg': 0.1,
    'dg': 0.01,
    'dag': 10,
    'dr': 1.7718,
    'fg': 1e-15,
    'fq': 100,
    'gr': 0.0647989,
    'hg': 100,
    'hwt': 50802,
    'lton': 1016046,
    'ug': 1e-6,
    'mg': 0.001,
    'pg': 1e-12,
    'lb_t': 373,
    'ston': 907185,
    'slug': 14593,
    'stick': 113,
    'st': 6350,
    'tola': 180,
    'oz_t': 31.1035,
    'us_q': 100000
}

def to_grams(value, unit):
    if unit not in UNITS:
        raise ValueError("Invalid unit, please use valid units: " + ", ".join(UNITS.keys()))
    return value * UNITS[unit]

def from_grams(value, unit):
    if unit not in UNITS:
        raise ValueError("Invalid unit, please use valid units: " + ", ".join(UNITS.keys()))
    return value / UNITS[unit]

def convert_units(value, from_unit, to_unit):
    gram_value = to_grams(value, from_unit)
    converted_value = from_grams(gram_value, to_unit)
    return converted_value

def calculate_conversion():
    value = float(e1.get())
    from_unit = e2.get()
    Grams = to_grams(value, from_unit)
    e5.delete(0, tk.END)
    e5.insert(0, str(Grams))
    Kilograms = to_grams(value, from_unit) / 1000
    e6.delete(0, tk.END)
    e6.insert(0, str(Kilograms))
    Pounds = to_grams(value, from_unit) / 454
    e7.delete(0, tk.END)
    e7.insert(0, str(Pounds))
    Tons = to_grams(value, from_unit) / 907185
    e8.delete(0, tk.END)
    e8.insert(0, str(Tons))
    Atomic_Mass_Units = to_grams(value, from_unit) / 1.66054e-24
    e9.delete(0, tk.END)
    e9.insert(0, str(Atomic_Mass_Units))
    Carats = to_grams(value, from_unit) / 0.2
    e10.delete(0, tk.END)
    e10.insert(0, str(Carats))
    Centigrams = to_grams(value, from_unit) * 10
    e11.delete(0, tk.END)
    e11.insert(0, str(Centigrams))
    Decigrams = to_grams(value, from_unit) * 100
    e12.delete(0, tk.END)
    e12.insert(0, str(Decigrams))
    Decagrams = to_grams(value, from_unit) / 10
    e13.delete(0, tk.END)
    e13.insert(0, str(Decagrams))
    Drams = to_grams(value, from_unit) / 1.7718
    e14.delete(0, tk.END)
    e14.insert(0, str(Drams))
    Femtograms = to_grams(value, from_unit) * 1e+15
    e15.delete(0, tk.END)
    e15.insert(0, str(Femtograms))
    French_Quarters = to_grams(value, from_unit) / 100
    e16.delete(0, tk.END)
    e16.insert(0, str(French_Quarters))
    Grains = to_grams(value, from_unit) / 0.0647989
    e17.delete(0, tk.END)
    e17.insert(0, str(Grains))
    Hectograms = to_grams(value, from_unit) / 100
    e18.delete(0, tk.END)
    e18.insert(0, str(Hectograms))
    Hundredweights = to_grams(value, from_unit) / 50802
    e19.delete(0, tk.END)
    e19.insert(0, str(Hundredweights))
    Long_Tons = to_grams(value, from_unit) / 1016046
    e20.delete(0, tk.END)
    e20.insert(0, str(Long_Tons))
    Micrograms = to_grams(value, from_unit) * 1e+6
    e21.delete(0, tk.END)
    e21.insert(0, str(Micrograms))
    Milligrams = to_grams(value, from_unit) * 1000
    e22.delete(0, tk.END)
    e22.insert(0, str(Milligrams))
    Picograms = to_grams(value, from_unit) * 1e+12
    e23.delete(0, tk.END)
    e23.insert(0, str(Picograms))
    Pounds_Troy = to_grams(value, from_unit) / 373
    e24.delete(0, tk.END)
    e24.insert(0, str(Pounds_Troy))
    Short_Tons = to_grams(value, from_unit) / 907185
    e25.delete(0, tk.END)
    e25.insert(0, str(Short_Tons))
    Slugs = to_grams(value, from_unit) / 14593
    e26.delete(0, tk.END)
    e26.insert(0, str(Slugs))
    Stone = to_grams(value, from_unit) / 6350
    e27.delete(0, tk.END)
    e27.insert(0, str(Stone))
    Tolas = to_grams(value, from_unit) / 180
    e28.delete(0, tk.END)
    e28.insert(0, str(Tolas))
    Troy_Ounces = to_grams(value, from_unit) / 31.1035
    e29.delete(0, tk.END)
    e29.insert(0, str(Troy_Ounces))
    Us_Quintal = to_grams(value, from_unit) / 100000
    e30.delete(0, tk.END)
    e30.insert(0, str(Us_Quintal))
    
    
    

app = tk.Tk()
app.title("Unit Conversion")

e1 = tk.Entry(app)
e2 = tk.Entry(app)
e5 = tk.Entry(app)
e6 = tk.Entry(app)
e7 = tk.Entry(app)
e8 = tk.Entry(app)
e9 = tk.Entry(app)
e10 = tk.Entry(app)
e11 = tk.Entry(app)
e12 = tk.Entry(app)
e13 = tk.Entry(app)
e14 = tk.Entry(app)
e15 = tk.Entry(app)
e16 = tk.Entry(app)
e17 = tk.Entry(app)
e18 = tk.Entry(app)
e19 = tk.Entry(app)
e20 = tk.Entry(app)
e21 = tk.Entry(app)
e22 = tk.Entry(app)
e23 = tk.Entry(app)
e24 = tk.Entry(app)
e25 = tk.Entry(app)
e26 = tk.Entry(app)
e27 = tk.Entry(app)
e28 = tk.Entry(app)
e29 = tk.Entry(app)
e30 = tk.Entry(app)


l1 = tk.Label(app, text="Value:")
l2 = tk.Label(app, text="From unit:")
l5 = tk.Label(app, text="Grams:")
l6 = tk.Label(app, text="Kilograms:")
l7 = tk.Label(app, text="Pounds:")
l8 = tk.Label(app, text="Tons:")
l9 = tk.Label(app, text="Atomic Mass Units:")
l10 = tk.Label(app, text="Carats:")
l11 = tk.Label(app, text="Centigrams:")
l12 = tk.Label(app, text="Decigrams:")
l13 = tk.Label(app, text="Decagrams:")
l14 = tk.Label(app, text="Drams:")
l15 = tk.Label(app, text="Femtograms:")
l16 = tk.Label(app, text="French Quarters:")
l17 = tk.Label(app, text="Grains:")
l18 = tk.Label(app, text="Hectograms:")
l19 = tk.Label(app, text="Hundredweights:")
l20 = tk.Label(app, text="Long Tons:")
l21 = tk.Label(app, text="Micrograms:")
l22 = tk.Label(app, text="Milligrams:")
l23 = tk.Label(app, text="Picograms:")
l24 = tk.Label(app, text="Pounds Troy:")
l25 = tk.Label(app, text="Short Tons:")
l26 = tk.Label(app, text="Slugs:")
l27 = tk.Label(app, text="Stone:")
l28 = tk.Label(app, text="Tolas:")
l29 = tk.Label(app, text="Troy Ounces:")
l30 = tk.Label(app, text="US Quintal:")

b1 = tk.Button(app, text="Convert", command=calculate_conversion)

l1.grid(row=0, column=0, sticky="W")
e1.grid(row=0, column=1, columnspan=2)

l2.grid(row=1, column=0, sticky="W")
e2.grid(row=1, column=1, columnspan=2)

l5.grid(row=4, column=0, sticky="W")
e5.grid(row=4, column=1, columnspan=2)

l6.grid(row=5, column=0, sticky="W")
e6.grid(row=5, column=1, columnspan=2)

l7.grid(row=6, column=0, sticky="W")
e7.grid(row=6, column=1, columnspan=2)

l8.grid(row=7, column=0, sticky="W")
e8.grid(row=7, column=1, columnspan=2)

l9.grid(row=8, column=0, sticky="W")
e9.grid(row=8, column=1, columnspan=2)

l10.grid(row=9, column=0, sticky="W")
e10.grid(row=9, column=1, columnspan=2)

l11.grid(row=10, column=0, sticky="W")
e11.grid(row=10, column=1, columnspan=2)

l12.grid(row=11, column=0, sticky="W")
e12.grid(row=11, column=1, columnspan=2)

l13.grid(row=12, column=0, sticky="W")
e13.grid(row=12, column=1, columnspan=2)

l14.grid(row=13, column=0, sticky="W")
e14.grid(row=13, column=1, columnspan=2)

l15.grid(row=14, column=0, sticky="W")
e15.grid(row=14, column=1, columnspan=2)

l16.grid(row=15, column=0, sticky="W")
e16.grid(row=15, column=1, columnspan=2)

l17.grid(row=16, column=0, sticky="W")
e17.grid(row=16, column=1, columnspan=2)

l18.grid(row=17, column=0, sticky="W")
e18.grid(row=17, column=1, columnspan=2)

l19.grid(row=18, column=0, sticky="W")
e19.grid(row=18, column=1, columnspan=2)

l20.grid(row=19, column=0, sticky="W")
e20.grid(row=19, column=1, columnspan=2)

l21.grid(row=20, column=0, sticky="W")
e21.grid(row=20, column=1, columnspan=2)

l22.grid(row=21, column=0, sticky="W")
e22.grid(row=21, column=1, columnspan=2)

l23.grid(row=22, column=0, sticky="W")
e23.grid(row=22, column=1, columnspan=2)

l24.grid(row=23, column=0, sticky="W")
e24.grid(row=23, column=1, columnspan=2)

l25.grid(row=24, column=0, sticky="W")
e25.grid(row=24, column=1, columnspan=2)

l26.grid(row=25, column=0, sticky="W")
e26.grid(row=25, column=1, columnspan=2)

l27.grid(row=26, column=0, sticky="W")
e27.grid(row=26, column=1, columnspan=2)

l28.grid(row=27, column=0, sticky="W")
e28.grid(row=27, column=1, columnspan=2)

l29.grid(row=28, column=0, sticky="W")
e29.grid(row=28, column=1, columnspan=2)

l30.grid(row=29, column=0, sticky="W")
e30.grid(row=29, column=1, columnspan=2)

b1.grid(row=30, column=1, pady=6)

app.mainloop()
