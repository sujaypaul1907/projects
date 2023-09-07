from tkinter import *
import datetime

def date_time():
    #For getting time data
    time = datetime.datetime.now()
    hrt = time.strftime("%I")
    mint = time.strftime("%M")
    sect = time.strftime("%S")
    ampmt = time.strftime("%p")
    hr.config(text=hrt)
    min1.config(text=mint)
    sec.config(text=sect)
    ampm.config(text=ampmt)
    hr.after(200, date_time)

    #For getting date data
    datet = time.strftime("%d")
    montht = time.strftime("%m")
    yeart = time.strftime("%y")
    dayt = time.strftime("%a")
    date.config(text=datet)
    month.config(text=montht)
    year.config(text=yeart)
    day.config(text=dayt)

clock = Tk()
clock.title("**** Digital Clock ****")
clock.geometry("800x500")
clock.config(bg="Yellow")

#TIME BLOCKS

hr = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
hr.place(x=50, y=50, height=100, width=100)

min1 = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
min1.place(x=250, y=50, height=100, width=100)

sec = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
sec.place(x=450, y=50, height=100, width=100)

ampm = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
ampm.place(x=650, y=50, height=100, width=100)

hr_lab = Label(clock, text="HOUR", font=("Arial", 17, "bold"), bg="Red", fg="White") 
hr_lab.place(x=50, y=180, height=50, width=100)

min_lab = Label(clock, text="MIN.", font=("Arial", 17, "bold"), bg="Red", fg="White") 
min_lab.place(x=250, y=180, height=50, width=100)

sec_lab = Label(clock, text="SEC.", font=("Arial", 17, "bold"), bg="Red", fg="White") 
sec_lab.place(x=450, y=180, height=50, width=100)

ampm_lab = Label(clock, text="AM/PM", font=("Arial", 17, "bold"), bg="Red", fg="White") 
ampm_lab.place(x=650, y=180, height=50, width=100)

#DATE BLOCKS

date = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
date.place(x=50, y=280, height=100, width=100)

month = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
month.place(x=250, y=280, height=100, width=100)

year = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
year.place(x=450, y=280, height=100, width=100)

day = Label(clock, text="00", font=("Times New Roman", 40, "bold"), bg="Red", fg="White") 
day.place(x=650, y=280, height=100, width=100)

date_lab = Label(clock, text="DATE", font=("Arial", 17, "bold"), bg="Red", fg="White") 
date_lab.place(x=50, y=410, height=50, width=100)

month_lab = Label(clock, text="MONTH", font=("Arial", 17, "bold"), bg="Red", fg="White") 
month_lab.place(x=250, y=410, height=50, width=100)

year_lab = Label(clock, text="YEAR", font=("Arial", 17, "bold"), bg="Red", fg="White") 
year_lab.place(x=450, y=410, height=50, width=100)

day_lab = Label(clock, text="DAY", font=("Arial", 17, "bold"), bg="Red", fg="White") 
day_lab.place(x=650, y=410, height=50, width=100)

date_time()

clock.mainloop()