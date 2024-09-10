from tkinter import *

def miles_to_km():
    result = float(entry.get()) * 1.609
    label_converted.config(text=round(result))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.focus()
entry.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_converted = Label(text="0")
label_converted.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
