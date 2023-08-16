#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:38:38 2023
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 16:38:38 2023

@author: aquilavijayanayagam
"""

from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk

root=Tk()
root.title("random list")
root.geometry("400x400")
root.configure(background="orange")

mercury=ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
earth=ImageTk.PhotoImage(Image.open("earth.jpg"))

Label_planet = Label(root,text="planet : ",bg="lightblue")

Label_planet_name = Label(root,font=("courier ",18,"bold"),bg="lightblue")

Label_planet_image=Label(root,bg="gold2",highlightcolor="orange",highlightthickness=5,borderwidth=2)

Label_planet_gravity_radius = Label(root,font=("castellar",18,"bold"),bg="lightblue")

Label_planet_info = Label(root,font=("courier",10,"bold"),bg="lightblue",wraplength=500)

planets=["mercury","venus","earth"]
selectedval = StringVar()
dropdown = ttk.Combobox(root,values=planets, textvariable=selectedval)

def planetInfo():
    planet=selectedval.get()
    if planet == "mercury":
        Label_planet_name['text']="mercury"
        Label_planet_image['image']=mercury
        Label_planet_gravity_radius['text']="Gravity and radius - Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        Label_planet_info['text']="Information - Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
        
    elif planet == "venus":
            Label_planet_name['text']="venus"
            Label_planet_image['image']=venus
            Label_planet_gravity_radius['text']="Gravity and radius - Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
            Label_planet_info['text']="Information - Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
            
    elif planet == "earth":
                Label_planet_name['text']="earth"
                Label_planet_image['image']=earth
                Label_planet_gravity_radius['text']="Gravity and radius - Gravity : 9.807 m/s² \n Radius : 6,371 km"
                Label_planet_info['text']="Information - Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."





btn=Button(root,text="show planet info ",command=planetInfo)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)
Label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
Label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
Label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
Label_planet_gravity_radius.place(relx=0.5, rely=0.8, anchor=CENTER)
Label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
