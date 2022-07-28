<<<<<<< HEAD
from tkinter import *
import datetime 

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    

    lab_hr.config(text = hr)
    lab_min.config(text = min)
    lab_sec.config(text =sec)
    lab_am.config(text = am)
    lab_date.config(text = date)
    lab_month.config(text = month)
    lab_year.config(text = year)
    lab_day.config(text = day)
    
    lab_hr.after(1,date_time)
    

clock = Tk()
clock.title('       ****Digital clock****')
clock.geometry("1000x500")
clock.config(bg = 'yellow')

# ************time


lab_hr = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_hr.place(x=120,y=45,height=110,width=100)
lab_hr_txt = Label(clock,text="Hour",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)


lab_min = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt = Label(clock,text="Min",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_min_txt.place(x=340,y=190,height=40,width=100)


lab_sec = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt = Label(clock,text="Sec",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)


lab_am = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_am.place(x=780,y=45,height=110,width=100)
lab_am_txt = Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_am_txt.place(x=780,y=190,height=40,width=100)


#****************  date


lab_date = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_date.place(x=120,y=260,height=110,width=100)
lab_date_txt = Label(clock,text="Date",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_date_txt.place(x=120,y=400,height=40,width=100)


lab_month = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_month.place(x=340,y=260,height=110,width=100)
lab_month_txt = Label(clock,text="Month",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_month_txt.place(x=340,y=400,height=40,width=100)


lab_year = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_year.place(x=560,y=260,height=110,width=100)
lab_year_txt = Label(clock,text="Year",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_year_txt.place(x=560,y=400,height=40,width=100)


lab_day = Label(clock,text="00",font=("Time New Roman",35,"bold"),
                bg = "red",fg = "white")
lab_day.place(x=780,y=260,height=110,width=100)
lab_day_txt = Label(clock,text="Day",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_day_txt.place(x=780,y=400,height=40,width=100)


date_time()

=======
from tkinter import *
import datetime 

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime("%I")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    am = time.strftime("%p")
    date = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%y")
    day = time.strftime("%a")
    

    lab_hr.config(text = hr)
    lab_min.config(text = min)
    lab_sec.config(text =sec)
    lab_am.config(text = am)
    lab_date.config(text = date)
    lab_month.config(text = month)
    lab_year.config(text = year)
    lab_day.config(text = day)
    
    lab_hr.after(1,date_time)
    

clock = Tk()
clock.title('       ****Digital clock****')
clock.geometry("1000x500")
clock.config(bg = 'yellow')

# ************time


lab_hr = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_hr.place(x=120,y=45,height=110,width=100)
lab_hr_txt = Label(clock,text="Hour",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_hr_txt.place(x=120,y=190,height=40,width=100)


lab_min = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_min.place(x=340,y=45,height=110,width=100)
lab_min_txt = Label(clock,text="Min",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_min_txt.place(x=340,y=190,height=40,width=100)


lab_sec = Label(clock,text="00",font=("Time New Roman",60,"bold"),
                bg = "red",fg = "white")
lab_sec.place(x=560,y=45,height=110,width=100)
lab_sec_txt = Label(clock,text="Sec",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_sec_txt.place(x=560,y=190,height=40,width=100)


lab_am = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_am.place(x=780,y=45,height=110,width=100)
lab_am_txt = Label(clock,text="AM/PM",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_am_txt.place(x=780,y=190,height=40,width=100)


#****************  date


lab_date = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_date.place(x=120,y=260,height=110,width=100)
lab_date_txt = Label(clock,text="Date",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_date_txt.place(x=120,y=400,height=40,width=100)


lab_month = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_month.place(x=340,y=260,height=110,width=100)
lab_month_txt = Label(clock,text="Month",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_month_txt.place(x=340,y=400,height=40,width=100)


lab_year = Label(clock,text="00",font=("Time New Roman",50,"bold"),
                bg = "red",fg = "white")
lab_year.place(x=560,y=260,height=110,width=100)
lab_year_txt = Label(clock,text="Year",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_year_txt.place(x=560,y=400,height=40,width=100)


lab_day = Label(clock,text="00",font=("Time New Roman",35,"bold"),
                bg = "red",fg = "white")
lab_day.place(x=780,y=260,height=110,width=100)
lab_day_txt = Label(clock,text="Day",font=("Time New Roman",20,"bold"),
                bg = "red",fg = "white")
lab_day_txt.place(x=780,y=400,height=40,width=100)


date_time()

>>>>>>> 147352ee0cc45a3d3fe0ee0dff0eadc8f65c89e3
clock.mainloop()