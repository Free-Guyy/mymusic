import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
a = Tk()
menubar=Menu(a)
a.config(menu=menubar)
def browse_file():
    global b
    b=filedialog.askopenfilename()
    print(b)
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Love File", menu=submenu)
submenu.add_command(label="Open your Love",command=browse_file)
submenu.add_command(label = "New_file")
submenu.add_command(label = "Exit",command=a.destroy)
label = Label(a,text="LETS MAKE LOVE")
label.pack()
def About_Love():
    tkinter.messagebox.showerror("C:\\Users\\S Pavan Kumar Reddy\\Desktop\\Music Player\\Manju.png","Love cannot express with words")
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Love helper", menu=submenu)
submenu.add_command(label="About Love",command=About_Love)
def YOUR_OPINION():
    tkinter.messagebox.showerror("C:\\Users\\S Pavan Kumar Reddy\\Desktop\\Music Player\\Manju.png","You're the one can make ur life with full of love")
submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="YOUR FEELINGS", menu=submenu)
submenu.add_command(label="OPINION",command=YOUR_OPINION)
mixer.init()
a.title(" Manju")
a.iconbitmap("C:\\Users\\S Pavan Kumar Reddy\\Pictures\\Saved Pictures\\Pavan.png")
Photo =  PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\Desktop\\Music Player\\Manju.png")
labelphoto = Label(a, image=Photo)
labelphoto.pack()
filelabel = Label(a, text ="YOUR SONG")
filelabel.pack(pady=10)
lengthlabel = Label(a, text ="LENGTH OF SONG:--:--")
lengthlabel.pack()
def show_details():
    filelabel["text"]="PLAYING"+ "-" + os.path.basename(b)
    file_data = os.path.split(b)
    if file_data[1] == ".mp3":
        audio = MP3(b)
        total_length = audio.info.lenght()
    else:
        g=mixer.Sound(b)
        total_length = g.get_length()
    mins,secs = divmod(total_length,60)
    mins = round(mins)
    secs =round(secs)
    timeformat = "(:02d):(:02d)".format(mins,secs)
    print(timeformat)
    lengthlabel["text"]="TOTAL LENGTH"+ "-" + timeformat
def play_music():
    global paused
    if paused:
        mixer.music.unpause()
        statusbar["text"]="MUSIC RESUMED"
        paused = FALSE
    else:
        try:
            mixer.music.load(b)
            mixer.music.play()
            statusbar["text"]="LIFE WITH FULL OF LOVE" + " " + os.path.basename(b)
            show_details()
        except:
            tkinter.messagebox.showerror("file not found")
def stop_music():
    mixer.music.stop()
    statusbar["text"]="LIFE END"
    print("Your love destination")
paused =FALSE
def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"]="MUSIC PAUSED"
    print("If you lie to your lover,You will stuck")
def rewind_music():
    mixer.music.rewind()
    statusbar["text"]="REWINDING LOVE"
def set_vol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)
muted = FALSE
def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.8)
        volumeBtn.configure(image=volumephoto)
        scale.set(80)
        muted = FALSE
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutephoto)
        scale.set(0)
        muted=TRUE
middleframe=Frame(a,relief=RAISED,borderwidth = 1)
middleframe.pack(padx=50, pady=50)
playphoto = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\m.png")
playBtn= Button(middleframe,image=playphoto,command=play_music)
playBtn.grid(row=0,column=0,padx=10)
stop_photo = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\s.png")
stopBtn= Button(middleframe,image=stop_photo,command=stop_music)
stopBtn.grid(row=0,column=2,padx=10)
pausephoto = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\q.png")
pauseBtn = Button(middleframe, image=pausephoto, command =pause_music,text="Lets make your LoveStop")
pauseBtn.grid(row=0,column=1,padx=10)
bottomframe= Frame(a)
bottomframe.pack()
rewindphoto = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\rewind.png")
rewindBtn = Button(bottomframe, image=rewindphoto, command =rewind_music)
rewindBtn.grid()
mutephoto = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\mute.png")
volumephoto = PhotoImage(file="C:\\Users\\S Pavan Kumar Reddy\\desktop\\Music Player\\sound.png")
volumeBtn = Button(bottomframe, image=volumephoto, command = mute_music)
volumeBtn.grid(row=0,column=1)
scale=Scale(a,from_=0,to=100,orient= "horizontal",command = set_vol)
scale.set(80)
mixer.music.set_volume(0.8)
scale.pack(pady=10)
statusbar = Label(a,text="welcome to love",relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill = X)
a.mainloop()
