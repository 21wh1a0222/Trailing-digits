#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk

def doodad(P, D, MP):
    s = MP // P
    max_i = 0
    for i in range(1, s):
        res = i * P
        res_str = str(res)
        num_trailing_digits = len(res_str) - len(res_str.rstrip(str(D)))
        max_i = max(max_i, num_trailing_digits)
    return max_i

def on_button_click():
    price = int(price_entry.get())
    trailing_digit = str(digit_entry.get())
    max_price = int(max_price_entry.get())
    max_trailing_digits = doodad(price, trailing_digit, max_price)
    result_label.config(text=f"Max Trailing Digits: {max_trailing_digits}")

root = tk.Tk()
root.title("Trailing Digits")
root.geometry("400x200")

# Load the image file and create a label to display it
bg_image = tk.PhotoImage(file=r"C:\Users\Khyathi\Downloads\pic (1).png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

price_label = tk.Label(root, text="Price of the Doodad:")
price_label.pack(padx=5,pady=15)
price_entry = tk.Entry(root)
price_entry.pack()

digit_label = tk.Label(root, text="Desired Trailing Digit:")
digit_label.pack(padx=5,pady=15)
digit_entry = tk.Entry(root)
digit_entry.pack()

max_price_label = tk.Label(root,text="Maximum Bundle Price:")
max_price_label.pack(padx=5,pady=15)
max_price_entry = tk.Entry(root)
max_price_entry.pack()

button = tk.Button(root, text="Calculate",command=on_button_click)
button.pack(padx=5, pady=15)
result_label = tk.Label(root, text="")
result_label.pack()


root.mainloop()


# In[ ]:




