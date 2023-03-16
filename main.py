"""---------------------------------------- Length index converter ----------------------------------------
This project is a **Length index converter**.
First, it receives the length value and primary and secondary indexes from the user. It performs the calculations and
displays the result according to the second index.
"""

# ---------------------------------------- Add Required Library ----------------------------------------

from tkinter import *

# ---------------------------------------- Calculation function ----------------------------------------

convertor = {
    # ---------------------------------------- Conversion formulas from meter ----------------------------------------
    "Meter": {"Meter": "No conversion required!", "Kilo Meter": lambda x: x * 0.001, "Mile": lambda x: x * 0.000621371,
              "Yard": lambda x: x * 1.09361, "Foot": lambda x: x * 3.28084, "Inch": lambda x: x * 39.3701,
              "Nautical Mile": lambda x: x * 0.000539957},
    # ---------------------------------------- Conversion formulas from kilo meter ------------------------------------
    "Kilo Meter": {"Meter": lambda x: x * 1000, "Kilo Meter": "No conversion required!", "Mile": lambda x: x * 0.621371,
                   "Yard": lambda x: x * 1093.61, "Foot": lambda x: x * 3280.84, "Inch": lambda x: x * 39370.1,
                   "Nautical Mile": lambda x: x * 0.539957},
    # ---------------------------------------- Conversion formulas from mile ----------------------------------------
    "Mile": {"Meter": lambda x: x * 1609.34, "Kilo Meter": lambda x: x * 1.60934, "Mile": "No conversion required!",
             "Yard": lambda x: x * 1760, "Foot": lambda x: x * 5280, "Inch": lambda x: x * 63360,
             "Nautical Mile": lambda x: x * 0.868976},
    # ---------------------------------------- Conversion formulas from yard ----------------------------------------
    "Yard": {"Meter": lambda x: x * 0.9144, "Kilo Meter": lambda x: x * 0.0009144, "Mile": lambda x: x * 0.000568182,
             "Yard": "No conversion required!", "Foot": lambda x: x * 3, "Inch": lambda x: x * 36,
             "Nautical Mile": lambda x: x * 0.000493737},
    # ---------------------------------------- Conversion formulas from foot ----------------------------------------
    "Foot": {"Meter": lambda x: x * 0.3048, "Kilo Meter": lambda x: x * 0.0003048, "Mile": lambda x: x * 0.000189394,
             "Yard": lambda x: x * 0.333333, "Foot": "No conversion required!", "Inch": lambda x: x * 12,
             "Nautical Mile": lambda x: x * 0.000164579},
    # ---------------------------------------- Conversion formulas from inch ----------------------------------------
    "Inch": {"Meter": lambda x: x * 0.0254, "Kilo Meter": lambda x: x * 2.54 * pow(10, -5),
             "Mile": lambda x: x * 1.5783 * pow(10, -5), "Yard": lambda x: x * 0.0277778,
             "Foot": lambda x: x * 0.0833333, "Inch": "No conversion required!",
             "Nautical Mile": lambda x: x * 1.3715 * pow(10, -5)},
    # ---------------------------------------- Conversion formulas from nautical mile ---------------------------------
    "Nautical Mile": {"Meter": lambda x: x * 1852, "Kilo Meter": lambda x: x * 1.852, "Mile": lambda x: x * 1.15078,
                      "Yard": lambda x: x * 2025.37, "Foot": lambda x: x * 6076.12, "Inch": lambda x: x * 72913.4,
                      "Nautical Mile": "No conversion required!"}, }


def convert():
    m_value = float(input.get())
    first_index = str(clicked_1.get())
    con = convertor[first_index]
    second_index = str(clicked_2.get())
    result = con[second_index]
    label_3.config(text=f"{round(result(m_value), 4)}")


# ---------------------------------------- Add GUI ----------------------------------------


window = Tk()
window.title("Length index converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=25)

input = Entry(width=10)
input.grid(column=0, row=0)

options = ["Meter", "Kilo Meter", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]

clicked_1 = StringVar()
first_dropmenu = OptionMenu(window, clicked_1, *options)
first_dropmenu.grid(column=1, row=0)

to_label = Label(text="to")
to_label.grid(column=2, row=0)

clicked_2 = StringVar()
second_dropmenu = OptionMenu(window, clicked_2, *options)
second_dropmenu.grid(column=3, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

label_3 = Label(text="0")
label_3.grid(column=1, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=4)

window.mainloop()
