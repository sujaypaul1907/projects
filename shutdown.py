#Shutdown / Restart GUI for PC

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()

st.title("ShutDown App")
st.geometry("500x450")
st.config(bg="Blue")

r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle", command = restart) 
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart with Time", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle", command = restart_time) 
rt_button.place(x=100, y=150, height=50, width=300)

s_button = Button(st, text="Shutdown", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle", command = shutdown) 
s_button.place(x=150, y=240, height=50, width=200)

lg_button = Button(st, text="Log Out", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle", command = logout) 
lg_button.place(x=150, y=330, height=50, width=200)

st.mainloop()
