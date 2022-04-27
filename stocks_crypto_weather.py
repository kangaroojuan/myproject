import tkinter as tk
from tkinter import ttk
import requests
import price_finder as price_api
import weather_api

HEIGHT = 500
WIDTH = 600

def get_entry(cmb,entry):
    try:
        get_price(cmb, entry.strip())
    except KeyError:
        label['text'] = "Incorrect Format"
        print()

def get_price(SCW, api_arg):
    if SCW == "STOCK":
        new_url = price_api.generate_stock_url(api_arg.upper(), price_api.API_KEY)
        price = price_api.generate_price(new_url)
        if price == -1:
            label['text'] = "Has no price."
            print("Has no price.")
        else:
            label['text'] = "${price:.2f}".format(price=price)
            print("$", price, sep="")
    elif SCW == "CRYPTO":
        crypto_url = price_api.generate_crypto_url(api_arg.upper(), price_api.API_KEY)
        crypto_price = price_api.generate_price(crypto_url)
        if crypto_price == -1:
            label['text'] = "Has no price."
            print("Has no price.")
        else:
            label['text'] = "${price:.2f}".format(price=crypto_price)
            print("$", str(crypto_price)[:-2], sep="")
    elif SCW == "WEATHER":
        weather_url = weather_api.generate_weather_url(api_arg, weather_api.WEATHER_API_KEY)
        label['text'] = "The temperature outside is " + str(weather_api.generate_temp(weather_url)) + "°F" \
            ".\n" + "The condition is " + weather_api.generate_condition(weather_url) + "."
        print("The temperature outside is", weather_api.generate_temp(weather_url), end=".\n")
        print("The condition is", weather_api.generate_condition(weather_url), end=".\n")
    else:
        label['text'] = "Select from drop down."

root =  tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='0_rKEzfMrYUwfSLCeA.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relheight=1, relwidth=1)

frame =  tk.Frame(root, bg='#79a832', bd=5)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

cmb = ttk.Combobox(root, value=["CRYPTO", "STOCK", "WEATHER"])
cmb.place(relx=0.13, rely=0.11, relheight=0.08, relwidth=0.13)

entry = tk.Entry(frame, font=40)
entry.place(relx=0.18, relheight=1, relwidth=0.5)

button = tk.Button(frame, text="Search", font=40, command=lambda: get_entry(cmb.get(), entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

#upper_frame =  tk.Frame(root, bg='#79a832', bd=5)
#upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.75, anchor='n')

lower_frame = tk.Frame(root, bg='#79a832', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=50)
label.place(relwidth=1, relheight=1)

root.title('stock, crypto, and weather')

root.mainloop()