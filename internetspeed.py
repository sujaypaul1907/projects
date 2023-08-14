#Internet Speed Test checker

from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downsp = str(round((sp.download()/10**6),3))+"Mbps"
    upsp = str(round((sp.upload()/10**6),3))+"Mbps"
    downspeed.config(text=downsp)
    upspeed.config(text=upsp)

sp = Tk()
sp.title("**** Internet Speed Test ****")
sp.geometry("500x600")
sp.config(bg="Green")

speed = Label(sp, text="Internet Speed Test", font=("Times New Roman", 20, "bold"), cursor = "circle", bg="Green", fg="White") 
speed.place(x=75, y=60, height=50, width=350)

down = Label(sp, text="Downloading Speed", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle") 
down.place(x=100, y=150, height=50, width=300)

downspeed = Label(sp, text="00", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle") 
downspeed.place(x=100, y=220, height=50, width=300)

up = Label(sp, text="Uploading Speed", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle") 
up.place(x=100, y=320, height=50, width=300)

upspeed = Label(sp, text="00", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle") 
upspeed.place(x=100, y=390, height=50, width=300)

starttest = Button(sp, text="Start Test", font=("Times New Roman", 20, "bold"), relief = RAISED, cursor = "circle", command=speedcheck) 
starttest.place(x=150, y=500, height=50, width=200)


sp.mainloop()