from tkinter import *
import os
import random
from tkinter import messagebox
from PIL import ImageTk,Image
from pygame import mixer
mixer.init()
import time
from pygame import mixer
# mixer.pre_init(44100,16,2,4096)

root = Tk()

def music(file,x,y=0):
   global Mid_Sound
   if x == 1:
      # bulletSound = mixer.Sound("laser.wav")
      # bulletSound.play()
      Mid_Sound = mixer.Sound(f"{file}.wav")
      Mid_Sound.play(-1)
      Mid_Sound.set_volume(0.5)
   elif x ==2:
      mixer.music.load(f"{file}.mp3")
      mixer.music.play(-1)
   elif x == 3:
      mixer.music.load(f"{file}.mp3")
      mixer.music.play(1)
   if y==1:
      Mid_Sond = mixer.Sound(f"{file}.wav")
      Mid_Sond.play(-1)
      Mid_Sond.set_volume(1)


root.title("Welcome To Play Stone Paper World Made by Vivek")
root.config(bg = 'cyan')
# root.iconbitmap("tr4.ico"
root.iconphoto(False,PhotoImage(file = "tr1.png"))
root.geometry("650x700")
# root.state('zoomed')
root.resizable(height=0,width=0)


def imagge():
   print("cmp - %s user %s"%(cmp,x))
   global y,z,igu,pgu,igc,pgc
   if x == 'Scissor':
      y = 1
   elif x == 'Paper':
      y = 2
   elif x == 'Stone':
      y = 3

   framec = Frame(frameb, relief=SUNKEN, height=300, width=300, bd=15)
   framec.grid(row=0, column=0)
   canvas = Canvas(framec, width=260, height=260)
   canvas.grid(row=0, column=0)
   igu = Image.open(f"{y}.png")
   igu = igu.resize((250, 250), Image.ANTIALIAS)
   pgu = ImageTk.PhotoImage(igu)
   canvas.create_image(8, 8, anchor=NW, image=pgu)
   if cmp == 'Scissor':
      z = 1
   elif cmp == 'Paper':
      z = 2
   elif cmp == 'Stone':
      z = 3
   framed = Frame(frameb, relief=SUNKEN, height=300, width=300, bd=15)
   framed.grid(row=0, column=1)
   canvas = Canvas(framed, width=260, height=260)
   canvas.grid(row=0, column=0)
   igc = Image.open(f"{z}.png")
   igc = igc.resize((250, 250), Image.ANTIALIAS)
   pgc = ImageTk.PhotoImage(igc)
   canvas.create_image(8, 8, anchor=NW, image=pgc)

def Total_Matches():
   a1.set(f"{var.get()}")
   b1.set(f"{var.get()}")

def Match_Played(i):
   a2.set(i)
   b2.set(i)

def Win_Matches():
   if (cmp_point == user_point):
      a3.set(f"{user_point}")
      b3.set(f"{cmp_point}")
   elif (user_point < cmp_point):
      # mixer.music.stop()
      # music("lost",1)
      b3.set(f"{user_point}")
      a3.set(f"{cmp_point}")
   elif (cmp_point < user_point):
      # mixer.music.stop()
      # music("won",1)
      b3.set(f"{user_point}")
      a3.set(f"{cmp_point}")
m,n = 0,0
def Lost_Matches():
   global m,n
   if cmp == User:
      pass
   elif((cmp=="Stone" and x=="Scissor") or (cmp=="Paper" and x =="Stone") or (cmp=="Scissor" and x=="Paper")):
      mixer.music.stop()
      music("lost", 3)
      m = m + 1
      b4.set(m)
   elif((cmp=="Stone" and x=="Paper") or (cmp=="Paper" and x =="Scissor") or (cmp=="Scissor" and x=="Stone")):
      mixer.music.stop()
      music("won", 3)
      n = n + 1
      a4.set(n)

def Points(user_point,cmp_point):
   val1.set(f"{user_point}")
   val2.set(f"{cmp_point}")

o = 0
def Draw():
   if x == cmp:
      global o
      mixer.music.stop()
      music("draw", 3)
      o = o +1
      a5.set(o)
      b5.set(o)


def Play_Again(event):
   mixer.quit()
   top.destroy()
   os.system("Stone_paper.py")

def Exit_Game(event):
   top.destroy()


def Next():
   if var.get() > 0:
      global pho,pho1,pho2,pho3,pho4,pho5
      frameb.destroy()
      # framei.destroy()
      frameg.destroy()
      # frameh.destroy()
      framee.destroy()
      framed.destroy()
      framec.destroy()
      print(cmp,User)
      if (cmp_point == user_point):
            music("Surprise",3)
            framew1 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
            framew1.grid(row=0, column=0)
            canv = Canvas(framew1, width=500, height=295)
            canv.grid(row=0, column=0)
            # ima = Image.open("13.png")
            # ima = ima.resize((270, 300), Image.ANTIALIAS)
            # pho = ImageTk.PhotoImage(ima)
            # canv.create_image(0, 0, anchor=NW, image=pho)
            ima1 = Image.open("draw4.jpg")
            ima1 = ima1.resize((500, 302), Image.ANTIALIAS)
            pho1 = ImageTk.PhotoImage(ima1)
            canv.create_image(-4,0, anchor=NW, image=pho1)
            framew2 = Frame(framew1, relief=SUNKEN, height=300, width=300, bd=15)
            framew2.grid(row=1, column=0)
            buttona = Button(framew2, text="Play again", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
            buttona.grid(row=0, column=0)
            buttona.bind("<Button-1>", Play_Again)
            buttonb = Button(framew2, text="Exit Game", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
            buttonb.grid(row=0, column=1)
            buttonb.bind("<Button-1>", Exit_Game)
            framew3 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
            framew3.grid(row=1, column=0)
            Label(framew3, text="          Game Draw          ",font = "comicsansms 33 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)

      elif (cmp_point > user_point):
         music("oops",3)
         framew1 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
         framew1.grid(row=0, column=0)
         canv2 = Canvas(framew1, width=500, height=295)
         canv2.grid(row=0, column=0)
         # ima2 = Image.open("lose1.jpg")
         # ima2 = ima2.resize((270, 300), Image.ANTIALIAS)
         # pho2 = ImageTk.PhotoImage(ima2)
         # canv2.create_image(0, 0, anchor=NW, image=pho2)
         ima2 = Image.open("lose1.jpg")
         ima2 = ima2.resize((500, 300), Image.ANTIALIAS)
         pho3 = ImageTk.PhotoImage(ima2)
         canv2.create_image(2,0, anchor=NW, image=pho3)
         framew2 = Frame(framew1, relief=SUNKEN, height=300, width=300, bd=15)
         framew2.grid(row=1, column=0)
         buttonc = Button(framew2, text="Play Again", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
         buttonc.grid(row=0, column=0)
         buttonc.bind("<Button-1>", Play_Again)
         buttond = Button(framew2, text="Exit Game", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
         buttond.grid(row=0, column=1)
         buttond.bind("<Button-1>", Exit_Game)

         framew3 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
         framew3.grid(row=1, column=0)
         Label(framew3, text=" oops! You Lost The Game ",font = "comicsansms 28 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)

      elif (cmp_point < user_point):
         music("congratulation",3)
         music("explosion",1,1)
         music("laser",1,1)
         framew1 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
         framew1.grid(row=0, column=0)
         canv3 = Canvas(framew1, width=500, height=295)
         canv3.grid(row=0, column=0)
         # ima3 = Image.open("13.png")
         # ima3 = ima3.resize((270, 300), Image.ANTIALIAS)
         # pho4 = ImageTk.PhotoImage(ima3)
         # canv3.create_image(0, 0, anchor=NW, image=pho4)
         ima3 = Image.open("13.png")
         ima3 = ima3.resize((310, 300), Image.ANTIALIAS)
         pho5 = ImageTk.PhotoImage(ima3)
         canv3.create_image(100, 0, anchor=NW, image=pho5)
         framew2 = Frame(framew1, relief=SUNKEN, height=300, width=300, bd=15)
         framew2.grid(row=1, column=0)
         buttone = Button(framew2, text="Play again", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
         buttone.grid(row=0, column=0)
         buttone.bind("<Button-1>", Play_Again)
         buttonf = Button(framew2, text="Exit Game", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
         buttonf.grid(row=0, column=1)
         buttonf.bind("<Button-1>", Exit_Game)
         framew3 = Frame(framem, relief=SUNKEN, height=300, width=300, bd=15)
         framew3.grid(row=1, column=0)
         Label(framew3, text="Congratulation! you won match", font="comicsansms 25 bold", fg='darkblue', padx=20, pady=10).grid(row=0,
                                                                                                                 column=0)
   else:
      messagebox.showinfo("Zero Games Selected","Please select the number of games you want to play")
      top.destroy()
      os.system("Stone_paper.py")


def getvals(event):

   try:

      x = event.widget.cget("text")
      Computer.set(f"{cmp}")
      print("user = ",x, "=========","Computer" ,cmp)
      User.set(x)
   except:

      pass

def things():
   messagebox.showinfo("message","Button clicked")


def play():

   root.destroy()
   global var,a1,a2,a3,a4,b1,b2,b3,b4,a5,b5
   global photo,image,phot,phot1,frameb,val1,val2,User,Computer,framec,framed,framea,framee,top,framem,framei,frameh,frameg,canvas
   top = Tk()
   User = StringVar()
   Computer = StringVar()
   val1 = StringVar()
   val2 = StringVar()
   val1.set("0")
   val2.set("0")
   a1 = StringVar()
   a1.set(0)
   a2 = StringVar()
   a2.set(0)
   a3 = StringVar()
   a3.set(0)
   a4 = StringVar()
   a4.set(0)
   a5 =StringVar()
   a5.set(0)
   b1 = StringVar()
   b1.set(0)
   b2 = StringVar()
   b2.set(0)
   b3 = StringVar()
   b3.set(0)
   b4 = StringVar()
   b4.set(0)
   b5 = StringVar()
   b5.set(0)
   print("var.grt",var.get())

   #### Music code

   music("background", 1)


   top.title("Welcome To Play Stone Paper World")
   top.attributes("-fullscreen", True)
   top.config(bg='cyan')

   # Title Frame
   framea = Frame(top, relief=SUNKEN, height=1000, width=200, bd=25)
   framea.pack(side = TOP,pady = 10)

   # Computer entries
   framei = Frame(top, relief=SUNKEN, bd=8,height=1000, width=200)
   framei.pack(side=RIGHT, padx=10)
   Label(framei, text="Player 2  ", font="lucida 30 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)
   Entry(framei, textvariable=Computer, font="large_font 20 bold").grid(row=1, column=0, ipady=10)
   framej = Frame(framei, relief=SUNKEN, bd=1, height=1000, width=200)
   framej.grid(row = 2,column =0)
   Label(framej, text="Total Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)
   Label(framej, text="Match Played", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=1,column=0)
   Label(framej, text="Win Matches ", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=2, column=0)
   Label(framej, text="Lost Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=3, column=0)
   Label(framej, text="Draw Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=4, column=0)
   Entry(framej, textvariable = a1, width=5, bd=2, font='large_font 20').grid(row=0, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framej, textvariable = a2, width=5, bd=2, font='large_font 20').grid(row=1, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framej, textvariable = a3, width=5, bd=2, font='large_font 20').grid(row=2, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framej, textvariable = a4, width=5, bd=2, font='large_font 20').grid(row=3, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framej, textvariable = a5, width=5, bd=2, font='large_font 20').grid(row=4, column=1, ipadx=15, ipady=15, pady=5)


   # User Entries
   frameh = Frame(top, relief=SUNKEN, bd=8,height=1000, width=200)
   frameh.pack(side = LEFT,padx = 10)
   Label(frameh, text="Player 1 ", font="lucida 30 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)
   Entry(frameh, textvariable=User, font="large_font 20 bold").grid(row=1, column=0, ipady=10)
   framek = Frame(frameh, relief=SUNKEN, bd=1, height=1000, width=200)
   framek.grid(row=2, column=0)
   Label(framek, text="Total Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)
   Label(framek, text="Match Played", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=1, column=0)
   Label(framek, text="Win Matches ", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=2, column=0)
   Label(framek, text="Lost Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=3, column=0)
   Label(framek, text="Draw Matches", font="comicsansms 18 bold", fg='darkblue', padx=20, pady=10).grid(row=4, column=0)
   Entry(framek, width=5, textvariable = b1,bd=2, font='large_font 20').grid(row=0, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framek, width=5, textvariable = b2, bd=2, font='large_font 20').grid(row=1, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framek, width=5, textvariable = b3, bd=2, font='large_font 20').grid(row=2, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framek, width=5, textvariable = b4, bd=2, font='large_font 20').grid(row=3, column=1, ipadx=15, ipady=15, pady=5)
   Entry(framek, width=5, textvariable = b5, bd=2, font='large_font 20').grid(row=4, column=1, ipadx=15, ipady=15, pady=5)

   # Title
   Label(framea, text="Welcome Stone Paper Scissor World", font="lucida 20 bold", fg='darkblue').pack()

   # Main Frame of all Centre Frame
   framem = Frame(top, relief=SUNKEN, height=1000, width=600, bd=20)
   framem.pack(pady = 20)

   # Computer pointd and user points frames
   frameg = Frame(top, relief=SUNKEN, height=900, width=950, bd=10)
   frameg.pack(pady = 2)

   # Computer points and user points entry widget
   Label(frameg, text="User Points", font="comicsansms 19 bold", fg='darkblue', padx=20, pady=10).grid(row=0, column=0)
   Label(frameg, text="Computer Points", font="comicsansms 19 bold", fg='darkblue', padx=20, pady=10).grid(row=0,column=2)
   Entry(frameg,textvar =val1,width = 5,bd = 2,font='Helvetica 20').grid(row = 0,column = 1,ipadx=13,ipady=15,pady = 5)
   Entry(frameg,textvar =val2,width = 5,bd = 2,font='large_font 20').grid(row = 0,column = 3,ipadx=13,ipady=15,pady = 5)

   # Main Frame of Images
   frameb = Frame(framem, relief=SUNKEN, height=309, width=600, bd=15)
   frameb.grid(row = 0 ,column = 0)

   # Stone paper Buttons and their frame
   framee = Frame(framem, relief=SUNKEN, height=150, width=780, bd=10)
   framee.grid(row = 1,column = 0)
   button1 = Button(framee, text="Stone", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
   button1.grid(row = 0,column =0)
   button1.bind("<Button-1>", getvals)
   button2 = Button(framee, text="Paper", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
   button2.grid(row=0,column=1)
   button2.bind("<Button-1>", getvals)
   button3 = Button(framee, text="Scissor", font="lucida 19 bold", padx=50, pady=6, bg='lightgreen', fg='black')
   button3.grid(row=0,column=2)
   button3.bind("<Button-1>", getvals)




   # Frames of images and canvas
   framec = Frame(frameb, relief=SUNKEN, height=300, width=300, bd=15)
   framec.grid(row = 0,column = 0)
   canvas = Canvas(framec, width=260, height=260)
   canvas.grid(row = 0 ,column = 0)
   image = Image.open("u.png")
   image = image.resize((200, 180), Image.ANTIALIAS)
   phot = ImageTk.PhotoImage(image)
   canvas.create_image(40,8, anchor=NW, image=phot)
   
   image = Image.open("bu.png")
   image = image.resize((120, 50), Image.ANTIALIAS)
   phot1 = ImageTk.PhotoImage(image)
   # phot1_label = Label(image = phot1)
   # phot1_label.grid(row = 0 , column = 0)
   # bu_button = Button(root,image = phot1,commond = things)
   # bu_button.grid(row = 1,column = 0)
   canvas.create_image(83,205, anchor=NW, image=phot1)

   # Frames of images and canvas
   framed = Frame(frameb, relief=SUNKEN, height=300, width=300, bd=15)
   framed.grid(row = 0,column = 1)
   canvas = Canvas(framed, width=260, height=260)
   canvas.grid(row = 0 , column = 0)
   image = Image.open("c3.png")
   image = image.resize((250, 250), Image.ANTIALIAS)
   photo = ImageTk.PhotoImage(image)
   canvas.create_image(8, 8, anchor=NW, image=photo)


   # stone,paper,scissor Code

   import random
   global cmp_point,cmp,x,i
   global user_point
   cmp_point = 0
   user_point = 0
   print("Value of radio========",button3.cget("text"),  var.get())
   for i in range(var.get()):
      Total_Matches()
      l = ["Stone","Scissor", "Paper"]
      random.shuffle(l)
      cmp = random.choice(l)

      print("Wait......")

      top.wait_variable(User)


      x = User.get()
      imagge()
      if(cmp==x):
         pass
      elif ((cmp=="Stone" and x=="Scissor") or (cmp=="Paper" and x =="Stone") or (cmp=="Scissor" and x=="Paper")):
         cmp_point += 1
      else:
         user_point += 1
      Points(user_point, cmp_point)
      Match_Played(i+1)
      Win_Matches()
      Lost_Matches()
      Draw()
   print("user point =",user_point)
   print("cmp point =",cmp_point)
   if(cmp_point == user_point):
         print("Match tie")
   elif(cmp_point>user_point):
         print("Computer won the match")
   else:
         print("User won the match")
   framee.destroy()
   button1.destroy()
   button2.destroy()
   button3.destroy()
   framee = Frame(framem, relief=SUNKEN, height=150, width=780, bd=8)
   framee.grid(row=1, column=0)
   Label(framee, text="Press Next to Continue", font="comicsansms 25 bold", fg='darkblue', padx=40, pady=10).grid(row=0, column=0)
   button4 = Button(framee, text="Next", font="lucida 19 bold",command = Next, padx=40, pady=3, bg='lightgreen', fg='black')
   button4.grid(row=0, column=1)
   top.mainloop()

def check(event):
   if var.get() > 0:
      play()
   else:
      messagebox.showinfo("Zero Games Selected", "Please select the number of games you want to play")
      top.destroy()
      os.system("Stone_paper.py")





#######    Root window start from there

# music("background", 1)
music("welcome",3)

frame1 = Frame(root, relief = SUNKEN, height = 900, width = 200, bd = 18)
frame1.pack( fill = X)
Title = Label(frame1, text = " Welcome To Play Stone Paper Scissor World ", font = "lucida 20 bold", fg = 'darkblue')
Title.pack()

frame4 = Frame(root, relief = RIDGE, height = 900, width = 200, bd = 15, bg = 'linen')
frame4.pack(pady = 10)
canvas = Canvas(frame4, width=500, height=350)
canvas.grid(row=0, column=0)
image = Image.open("tr.png")
image = image.resize((500, 350), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
canvas.create_image(1, 1, anchor=NW, image=photo)


frame3 = Frame(root, relief = SUNKEN, height = 900, width = 200, bd = 15, bg = 'linen')
frame3.pack(pady = 5,padx = 10)
var = IntVar()
radio = Radiobutton(frame3, text = "1 Game",padx =14,variable = var ,value = "1",font = "comicsansms 17 bold")
radio.grid(row = 0, column = 0)

radio = Radiobutton(frame3, text = "5 Game",padx =14,variable = var ,value = "5",font = "comicsansms 17 bold")
radio.grid(row = 0, column = 1)

radio = Radiobutton(frame3, text = "10 Game",padx =14,variable = var ,value = "10",font = "comicsansms 17 bold")
radio.grid(row = 0, column = 3)

radio = Radiobutton(frame3, text = "15 Game",padx =14,variable = var ,value = "15",font = "comicsansms 17 bold")
radio.grid(row = 1, column = 0)

radio = Radiobutton(frame3, text = "20 Game",padx =14,variable = var ,value = "20",font = "comicsansms 17 bold")
radio.grid(row = 1, column = 1)

radio = Radiobutton(frame3, text = "30 Game",padx =14,variable = var ,value = "30",font = "comicsansms 17 bold")
radio.grid(row = 1, column = 3)

frame5 = Frame(root, relief = SUNKEN, height = 900, width = 200, bd = 15, bg = 'white')
frame5.pack(padx = 20,pady = 14)

submit = Button(frame5, text =" PLAY", font = "comicsansms 17 bold",padx = 25,pady = 5, bg = 'red', fg = 'black' )
submit.pack()
submit.bind("<Button-1>", check)

root.mainloop()
