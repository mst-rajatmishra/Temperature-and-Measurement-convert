import tkinter as tk
from tkinter import ttk

def convert():
    try:
        measure = float(Entry.get())  
        unit_of_measure = drop_down.get()  
        convert_to = selected_unit.get()  

        
        if unit_of_measure == 'km':
            converted = convert_to_kilometer(measure, convert_to)
        elif unit_of_measure == 'm':
            converted = convert_to_meter(measure, convert_to)
        elif unit_of_measure == 'cm':
            converted = convert_to_centimeter(measure, convert_to)

        
        display_conversion_result(converted, convert_to)

    except ValueError as e:
        
        display_conversion_result(f"Error: {e}", None)

def display_conversion_result(converted, unit):
    
    new_window = tk.Tk()
    new_window.title('Converted Measurement')

    frame3 = tk.Frame(new_window)

    
    if isinstance(converted, str):  
        result_message = converted
    else:
        result_message = f"Converted value: {converted} {unit}"

    resulting = ttk.Label(frame3, text=result_message)
    resulting.pack(padx=5, pady=5)

    frame3.pack()
    new_window.mainloop()

def convert_to_kilometer(measure, convert_to):
    if convert_to == 'cm':
        return measure * 100000
    elif convert_to == 'm':
        return measure * 1000
    else:
        return measure

def convert_to_meter(measure, convert_to):
    if convert_to == 'km':
        return measure / 1000
    elif convert_to == 'cm':
        return measure * 1000
    else:
        return measure
    
def convert_to_centimeter(measure, convert_to):
    if convert_to == 'km':
        return measure / 100000
    elif convert_to == 'm':
        return measure / 1000
    else:
        return measure


window = tk.Tk()
window.title('Measurement Convert')
window.geometry('350x200')


temperature_label = ttk.Label(window, text='Enter Measurement To Convert')
temperature_label.pack(pady=20)

frame = ttk.Frame(window) 
Entry = ttk.Entry(frame)
units = ["km", "cm", "m"]
drop_down = ttk.Combobox(frame, values=units, state='readonly')
drop_down.set("m")
Entry.grid(padx=5, row=0, column=1)
drop_down.grid(padx=2, row=0, column=2)
frame.pack()

frame2 = ttk.Frame(window)
selected_unit = tk.StringVar()
celcius = ttk.Radiobutton(frame2, text='Centimeter (cm)', value='cm', variable=selected_unit)
kelvin = ttk.Radiobutton(frame2, text='Kilometer (km)', value='km', variable=selected_unit)
fahrenheit = ttk.Radiobutton(frame2, text='Meter (m)', value='m', variable=selected_unit)
celcius.grid(row=0, column=1, padx=2)
kelvin.grid(row=0, column=2, padx=2)
fahrenheit.grid(row=0, column=3, padx=2)
frame2.pack()


button = ttk.Button(window, text='Convert', command=convert)
button.pack(pady=20)


window.mainloop()
