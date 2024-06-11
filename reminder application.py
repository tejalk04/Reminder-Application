from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from plyer import notification
import time

t=Tk()
t.title("Notifier-App")
t.geometry("600x300")
img=Image.open("bell.png")
tkimage=ImageTk.PhotoImage(img)

#get details
def get_details():
    get_title=title.get()
    get_msg=msg.get()
    get_time=time1.get()

    if (get_title=="" or get_msg=="" or get_time==""):
        messagebox.showerror("Alert","All fields are required!")
    else:
        int_time=int(float(get_time))
        min_to_sec=int_time*60
        messagebox.showinfo("notifier set","set notification?")

        time.sleep(min_to_sec)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="notifier",
                            app_icon="ico.ico",
                            timeout=10)

img_label=Label(t,image=tkimage).grid()

#label1
t_label=Label(t,text="TITLE OF NOTIFICATION",font=("poppins",10))
t_label.place(x=12,y=70)

#entry1
title=Entry(t,font=("poppins",13))
title.place(x=165,y=70)

#label2
m_label=Label(t,text="DISPLAY MESSAGE",font=("poppins",10))
m_label.place(x=12,y=120)

#entry2
msg=Entry(t,font=("poppins",13))
msg.place(x=145,y=120, height=30)

#label3
time_label=Label(t,text="SET TIME",font=("poppins",10))
time_label.place(x=12,y=175)

#entry3
time1=Entry(t,width="5",font=("poppins",13))
time1.place(x=90,y=175)

#label4
time_min_label=Label(t,text="min",font=("poppins",10))
time_min_label.place(x=140,y=180)

#button
but=Button(t,text="SET NOTIFICATION", font=("poppins",10,'bold'),fg="#ffffff",
           bg="#528DFF", relief="raised",command=get_details)
but.place(x=170,y=230)

t.resizable(0,0)
t.mainloop()
