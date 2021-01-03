import time
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("CountDown")

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("0")
minute.set("0")
second.set("0")

hourEntry = Entry(root, width=3, font=("Arial", 18, ""),
                  textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),
                    textvariable=second)
secondEntry.place(x=180, y=20)


def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")
    while temp > -1:
        # bngeb ba2y ele seconds ba3d ma 7wlna kol 60 l min
        mins, secs = divmod(temp, 60)

        hours = 0
        if mins > 60:
            # nfs el kalam
            hours, mins = divmod(mins, 60)

        # 3wzen two deccimal places bs , tzbet ll 4kl
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        # kol sanya
        time.sleep(1)


        if (temp == 0):
            messagebox.showinfo("Time Countdown", "Time's up ")

        temp -= 1



btn = Button(root, text='Set Time Countdown', bd='5',
             command=submit)
btn.place(x=70, y=120)


root.mainloop()