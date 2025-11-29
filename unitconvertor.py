from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # import messagebox for popup

def on_button_click():
    try:
        value = float(entry.get())
        from_u = dropdown1.get()
        to_u = dropdown2.get()

        # Check conversions
        if from_u == 'celcius' and to_u == 'fehrenheit':
            result = (value * 9 / 5) + 32
        elif from_u == 'fehrenheit' and to_u == 'celcius':
            result = (value - 32) * 5 / 9
        elif from_u == 'meters' and to_u == 'feet':
            result = value * 3.281
        elif from_u == 'feet' and to_u == 'meters':
            result = value / 3.281
        elif from_u == to_u:
            result = value
        else:
            # Show popup for invalid conversion
            messagebox.showerror("Invalid Conversion", f"Cannot convert from {from_u} to {to_u}")
            return  # Stop execution here
        
        output_label.config(text=f"Output: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Tkinter window
root = Tk()
root.geometry('600x600')
root.title('Unit Converter')
root.configure(bg='pink')

Label(root, text='Unit Converter', font='Times 30', bg='pink').pack(pady=20)

from_unit = ['celcius', 'meters', 'feet', 'fehrenheit']
to_unit = ['fehrenheit', 'feet', 'meters', 'celcius']

Label(root, text='From unit 🌡️', font='Times 20', bg='pink').pack()
dropdown1 = ttk.Combobox(root, values=from_unit, width=23, font='Times 14', state="readonly")
dropdown1.set("select unit")
dropdown1.pack(pady=10)

Label(root, text='To unit 🌡️', font='Times 20', bg='pink').pack()
dropdown2 = ttk.Combobox(root, values=to_unit, width=23, font='Times 14', state="readonly")
dropdown2.set("select unit")
dropdown2.pack(pady=10)

Label(root, text='Enter Value', font='Times 20', bg='pink').pack(pady=10)
entry = Entry(root, width=20, bd=3, relief=SUNKEN, font=("Arial", 14))
entry.pack(padx=10, pady=20)

convert_button = Button(root, text="Convert", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"), command=on_button_click)
convert_button.pack(pady=10)

output_label = Label(root, text='Output', font='Times 20', bg='pink', fg='blue')
output_label.pack(pady=10)

root.mainloop()
