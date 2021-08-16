from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os
import random
import time
from pygame import mixer,image
mixer.init()
root = Tk()
root.title("Tic Tac Toe Game Made By Vivek kumar")
root.config(bg='cyan')
root.geometry("650x600")
root.resizable(height=0, width=0)

global frame_Tic_toe_image,play_button,Entry_user,Entry_computer
User = StringVar()
Computer = StringVar()


############ play start from there @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def play(event):
    global play_photo,exit_photo,back_photo,back1_photo
    frame_First_page.destroy()
    play_button.destroy()
    root.state('zoomed')
    t1, t2, t3, t4, t5, t6, t7, t8, t9 = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
    t1.set("")
    t2.set("")
    t3.set("")
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    t8.set("")
    t9.set("")

    def play_again():
        mixer.quit()
        root.destroy()
        os.system("Tic_Tac_Toe.py")

    def exit():
        mixer.quit()
        root.destroy()

    framem = Frame(root, relief=SUNKEN, bg="cyan")
    framem.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.66)

    frame_computer = Frame(root, relief=SUNKEN, bd=8, height=1000, width=200)
    frame_computer.pack(anchor=NE, side=RIGHT, padx=10)
    label_computer = Label(frame_computer, text="Player 2  ", font="lucida 30 bold", fg='black', padx=20, pady=10)
    label_computer.grid(row=0, column=0)
    Entry_computer = Entry(frame_computer, textvariable=Computer, font="large_font 20 bold", justify=CENTER,insertontime=0)
    Entry_computer.grid(row=1, column=0, ipady=10)

    frame_user = Frame(root, relief=SUNKEN, bd=8, height=1000, width=200)
    frame_user.pack(anchor=NW, side=LEFT, padx=10)
    label_user = Label(frame_user, text="Player 1  ", font="lucida 30 bold", fg='darkblue', padx=20, pady=10)
    label_user.grid(row=0, column=0)
    Entry_user = Entry(frame_user, textvariable=User, font="large_font 20 bold", justify=CENTER, insertontime=0,fg='darkblue')
    Entry_user.grid(row=1, column=0, ipady=10)




    image = Image.open("t.png")
    image = image.resize((300, 300), Image.ANTIALIAS)
    back_photo = ImageTk.PhotoImage(image)
    back_label = Label(root, image=back_photo, bg='cyan')
    back_label.place(relx=0.01, rely=0.4)

    image = Image.open("t.png")
    image = image.resize((300, 300), Image.ANTIALIAS)
    back1_photo = ImageTk.PhotoImage(image)
    back1_label = Label(root, image=back1_photo, bg='cyan')
    back1_label.place(relx=0.77, rely=0.4)

    # Main Frame of Lines
    frameb = Frame(framem, relief=SUNKEN, height=309, width=600, bd=25)
    frameb.grid(row=0, column=0)

    framed = Frame(frameb, relief=SUNKEN, height=300, width=250, bd=25)
    framed.grid(row=0, column=0)
    # Frames of line and canvas
    framec = Frame(framed, relief=SUNKEN, height=300, width=250, bd=15)
    framec.grid(row=0, column=0)



    canvas = Canvas(framec, width=400, height=300, bg='white')
    canvas.grid(row=0, column=0)

    def get_t1():
        global u1, entry1
        button1.destroy()
        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)

        entry1 = Entry(canvas, textvariable=t1, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,insertontime=0)
        canvas.create_window(70, 48, window=entry1, height=90, width=130)
        User.set("")
        u1 = 1
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry1.configure(fg="#0942f9")
            if p1 == 'x':
                t1.set("x")
            else:
                t1.set('0')
        elif count == 0:
            if p2 == 'x':
                t1.set("x")
            else:
                t1.set('0')
        # entry1.configure(state = DISABLED)

    def get_t2():
        global u1, entry2
        button2.destroy()
        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)

        entry2 = Entry(canvas, textvariable=t2, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,insertontime=0)
        canvas.create_window(207, 48, window=entry2, height=90, width=120)
        User.set("")
        u1 = 2
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry2.configure(fg="#0942f9")
            if p1 == 'x':
                t2.set("x")
            else:
                t2.set('0')
        elif count == 0:
            if p2 == 'x':
                t2.set("x")
            else:
                t2.set('0')
        # entry2.configure(state=DISABLED)

    def get_t3():
        global u1, entry3
        button3.destroy()
        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)

        entry3 = Entry(canvas, textvariable=t3, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,insertontime=0)
        canvas.create_window(338, 48, window=entry3, height=90, width=120)
        User.set("")
        u1 = 3
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry3.configure(fg="#0942f9")
            if p1 == 'x':
                t3.set("x")
            else:
                t3.set('0')
        elif count == 0:
            if p2 == 'x':
                t3.set("x")
            else:
                t3.set('0')
        # entry3.configure(state=DISABLED)

    def get_t4():
        global u1, entry4
        button4.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry4 = Entry(canvas, textvariable=t4, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,insertontime=0)
        canvas.create_window(70, 150, window=entry4, height=94, width=133)
        User.set("")
        u1 = 4
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry4.configure(fg="#0942f9")
            if p1 == 'x':
                t4.set("x")
            else:
                t4.set('0')
        elif count == 0:
            if p2 == 'x':
                t4.set("x")
            else:
                t4.set('0')
        # entry4.configure(state=DISABLED)

    def get_t5():
        global u1, entry5
        button5.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry5 = Entry(canvas, textvariable=t5, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,insertontime=0)
        canvas.create_window(207, 150, window=entry5, height=95, width=123)
        User.set("")
        u1 = 5
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry5.configure(fg="#0942f9")
            if p1 == 'x':
                t5.set("x")
            else:
                t5.set('0')
        elif count == 0:
            if p2 == 'x':
                t5.set("x")
            else:
                t5.set('0')
        # entry5.configure(state=DISABLED)

    def get_t6():
        global u1, entry6
        button6.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry6 = Entry(canvas, textvariable=t6, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,
                       insertontime=0)
        canvas.create_window(337, 150, window=entry6, height=95, width=123)
        User.set("")
        u1 = 6
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry6.configure(fg="#0942f9")
            if p1 == 'x':
                t6.set("x")
            else:
                t6.set('0')
        elif count == 0:
            if p2 == 'x':
                t6.set("x")
            else:
                t6.set('0')
        # entry6.configure(state=DISABLED)

    def get_t7():
        global u1, entry7
        button7.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry7 = Entry(canvas, textvariable=t7, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,
                       insertontime=0)
        canvas.create_window(70, 253, window=entry7, height=95, width=133)
        User.set("")
        u1 = 7
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry7.configure(fg="#0942f9")
            if p1 == 'x':
                t7.set("x")
            else:
                t7.set('0')
        elif count == 0:
            if p2 == 'x':
                t7.set("x")
            else:
                t7.set('0')
        # entry7.configure(state=DISABLED)

    def get_t8():
        global u1, entry8
        button8.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry8 = Entry(canvas, textvariable=t8, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,
                       insertontime=0)
        canvas.create_window(206, 253, window=entry8, height=95, width=121)
        User.set("")
        u1 = 8
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry8.configure(fg="#0942f9")
            if p1 == 'x':
                t8.set("x")
            else:
                t8.set('0')
        elif count == 0:
            if p2 == 'x':
                t8.set("x")
            else:
                t8.set('0')
        # entry8.configure(state=DISABLED)

    def get_t9():
        global u1, entry9
        button9.destroy()

        Button_Sound = mixer.Sound("Sound_0_x.wav")
        Button_Sound.set_volume(0.5)
        Button_Sound.play(0)


        entry9 = Entry(canvas, textvariable=t9, width=5, bd=0, font='Helvetica 40 bold', justify=CENTER, insertwidth=.4,
                       insertontime=0)
        canvas.create_window(337, 252, window=entry9, height=95, width=123)
        User.set("")
        u1 = 9
        if (p1 == 'x' or p1 == '0') and identify_player == 1 and count == 0:
            entry9.configure(fg="#0942f9")
            if p1 == 'x':
                t9.set("x")
            else:
                t9.set('0')
        elif count == 0:
            if p2 == 'x':
                t9.set("x")
            else:
                t9.set('0')
        # entry9.configure(state=DISABLED)

    button1 = Button(canvas, text="", command=get_t1, bd=0, bg='white')
    button1.place(relx=0.001, rely=0.01, relwidth=0.34, relheight=0.3)
    button2 = Button(canvas, text="", command=get_t2, bd=0, bg='white')
    button2.place(relx=0.36, rely=0.01, relwidth=0.3, relheight=0.3)
    button3 = Button(canvas, text="", command=get_t3, bd=0, bg='white')
    button3.place(relx=0.68, rely=0.01, relwidth=0.31, relheight=0.3)
    button4 = Button(canvas, text="", command=get_t4, bd=0, bg='white')
    button4.place(relx=0.001, rely=0.33, relwidth=0.34, relheight=0.32)
    button5 = Button(canvas, text="", command=get_t5, bd=0, bg='white')
    button5.place(relx=0.36, rely=0.33, relwidth=0.3, relheight=0.32)
    button6 = Button(canvas, text="", command=get_t6, bd=0, bg='white')
    button6.place(relx=0.68, rely=0.33, relwidth=0.31, relheight=0.32)
    button7 = Button(canvas, text="", command=get_t7, bd=0, bg='white')
    button7.place(relx=0.001, rely=0.67, relwidth=0.34, relheight=0.32)
    button8 = Button(canvas, text="", command=get_t8, bd=0, bg='white')
    button8.place(relx=0.36, rely=0.67, relwidth=0.3, relheight=0.32)
    button9 = Button(canvas, text="", command=get_t9, bd=0, bg='white')
    button9.place(relx=0.68, rely=0.67, relwidth=0.31, relheight=0.32)

    canvas.create_line(140.5, 0, 140.5, 300, fill='#ff1504')
    canvas.create_line(140, 0, 140, 300, fill='#ff1504')
    canvas.create_line(142, 0, 142, 300, fill='#ff1504')
    canvas.create_line(143, 0, 143, 300, fill='#ff1504')

    canvas.create_line(270, 0, 270, 300, fill='#ff1504')
    canvas.create_line(270.5, 0, 270.5, 300, fill='#ff1504')
    canvas.create_line(272, 0, 272, 300, fill='#ff1504')
    canvas.create_line(273, 0, 273, 300, fill='#ff1504')

    canvas.create_line(0, 97, 400, 97, fill='#ff1504')
    canvas.create_line(0, 98, 400, 98, fill='#ff1504')
    canvas.create_line(0, 95.5, 400, 95.5, fill='#ff1504')
    canvas.create_line(0, 95, 400, 95, fill='#ff1504')

    canvas.create_line(0, 200, 400, 200, fill='#ff1504')
    canvas.create_line(0, 202, 400, 202, fill='#ff1504')
    canvas.create_line(0, 203, 400, 203, fill='#ff1504')
    canvas.create_line(0, 200.5, 400, 200.5, fill='#ff1504')

    #### TIC TOE TOE WORLD code

    global p1, identify_player, count, flag
    flag = 0
    p1 = random.choice(['x', '0'])
    print(p1, "is slected")
    if p1 == '0':
        print("\t  palyer 2 choice is X \n")
        p2 = 'x'
    elif p1 == 'X' or p1 == 'x':
        print("\t  Player 2 choice is 0 \n")
        p2 = '0'

    l = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    l1 = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    for i in l1:
        for j in i:
            print(" ", j, end="")
        print()
    print()
    n = 0
    p = 1

    while ((n < 9) and (
            (l[0][0] != l[0][1] or l[0][1] != l[0][2]) and (l[0][0] != l[1][0] or l[1][0] != l[2][0]) and (
            l[2][0] != l[2][1] or l[2][1] != l[2][2])
            and (l[2][2] != l[1][2] or l[1][2] != l[0][2]) and (
                    l[0][1] != l[1][1] or l[1][1] != l[2][1]) and (l[1][0] != l[1][1] or l[1][1] != l[1][2])
            and (l[1][1] != l[0][2] or l[1][1] != l[2][0]) and (l[1][1] != l[0][0] or l[1][1] != l[2][2]))):
        k = 1
        count = 0
        if n % 2 == 0:
            print("  Player 1 enter the position : ")
            if p != 2:
                Computer.set('')
                User.set("Your Turn ")
                Entry_computer.configure(bg='white')
                Entry_user.configure(bg = 'lightgreen')
                identify_player = 1
                root.wait_variable(User)
                print(u1, "is the position of player1")
            print("Usser", u1, "chl gya")
            p = 3
            if ((l[0][0] != l[0][1] or l[0][1] != l[0][2]) and (l[0][0] != l[1][0] or l[1][0] != l[2][0]) and (
                    l[2][0] != l[2][1] or l[2][1] != l[2][2])
                    and (l[2][2] != l[1][2] or l[1][2] != l[0][2]) and (
                            l[0][1] != l[1][1] or l[1][1] != l[2][1]) and (l[1][0] != l[1][1] or l[1][1] != l[1][2])
                    and (l[1][1] != l[0][2] or l[1][1] != l[2][0]) and (l[1][1] != l[0][0] or l[1][1] != l[2][2])):
                count = 1
        elif n % 2 != 0:
            print("  Player 2 enter the position : ")
            User.set('')
            Computer.set("Your Turn")
            Entry_user.configure(bg = 'white')
            Entry_computer.configure(bg = 'lightgreen')
            identify_player = 2
            root.wait_variable(User)
            print(u1, "is the postion of player2")
            print("computer", u1, "chl gya")
            if ((l[0][0] != l[0][1] or l[0][1] != l[0][2]) and (l[0][0] != l[1][0] or l[1][0] != l[2][0]) and (
                    l[2][0] != l[2][1] or l[2][1] != l[2][2])
                    and (l[2][2] != l[1][2] or l[1][2] != l[0][2]) and (
                            l[0][1] != l[1][1] or l[1][1] != l[2][1]) and (l[1][0] != l[1][1] or l[1][1] != l[1][2])
                    and (l[1][1] != l[0][2] or l[1][1] != l[2][0]) and (l[1][1] != l[0][0] or l[1][1] != l[2][2])):
                count = 2
        for i in l:
            m = 0
            for j in i:
                if n % 2 == 0:
                    if k == u1:
                        print(" ", p1, end="")
                        i[m] = p1
                    else:
                        print(" ", j, end="")
                    m += 1
                    k += 1
                elif n % 2 != 0:
                    if k == u1:
                        print(" ", p2, end="")
                        i[m] = p2
                    else:
                        print(" ", j, end="")
                    m += 1
                    k += 1
            print("\n")
        n += 1


    if ((l[0][0] == l[0][1] and l[0][1] == l[0][2])):
        flag = 1
        entry1.configure(bg='cyan')
        entry2.configure(bg='cyan')
        entry3.configure(bg='cyan')

    if ((l[1][0] == l[1][1] and l[1][1] == l[1][2])):
        flag = 1
        entry4.configure(bg='cyan')
        entry5.configure(bg='cyan')
        entry6.configure(bg='cyan')

    if ((l[2][0] == l[2][1] and l[2][1] == l[2][2])):
        flag = 1
        entry7.configure(bg='cyan')
        entry8.configure(bg='cyan')
        entry9.configure(bg='cyan')

    if ((l[0][0] == l[1][0] and l[1][0] == l[2][0])):
        flag = 1
        entry1.configure(bg='cyan')
        entry4.configure(bg='cyan')
        entry7.configure(bg='cyan')

    if ((l[0][1] == l[1][1] and l[1][1] == l[2][1])):
        flag = 1
        entry2.configure(bg='cyan')
        entry5.configure(bg='cyan')
        entry8.configure(bg='cyan')

    if ((l[0][2] == l[1][2] and l[1][2] == l[2][2])):
        flag = 1
        entry3.configure(bg='cyan')
        entry6.configure(bg='cyan')
        entry9.configure(bg='cyan')

    if ((l[0][0] == l[1][1] and l[1][1] == l[2][2])):
        flag = 1
        entry1.configure(bg='cyan')
        entry5.configure(bg='cyan')
        entry9.configure(bg='cyan')

    if ((l[0][2] == l[1][1] and l[1][1] == l[2][0])):
        flag = 1
        entry3.configure(bg='cyan')
        entry5.configure(bg='cyan')
        entry7.configure(bg='cyan')

    if count == 1 and flag == 1:
        User.set("")
        Entry_user.configure(bg = 'white')
        mixer.music.load("Congratulation_player1.mp3")
        mixer.music.play(0)
        print("Congratulation player 1 won the match ")
        count = 5
        # messagebox.showinfo("Congratulation", "Congratulation player1 you won the match")
    elif count == 2 and flag == 1:
        Computer.set("")
        Entry_computer.configure(bg = "white")
        mixer.music.load("Congratulation Player 2..mp3")
        mixer.music.play()
        print("Congratulation player 2 won the match ")
        count = 5
        # messagebox.showinfo("Congratulation", "Congratulation player2 you won the match")
    elif flag == 0:
        User.set("")
        Entry_user.configure(bg='white')
        Computer.set("")
        Entry_computer.configure(bg="white")
        mixer.music.load("draw.mp3")
        mixer.music.play(0)
        print("Game draw")
        count = 5
        # messagebox.showinfo("OOPS", "Game draw")
    else:
        messagebox.showinfo("Warning", "Game Crashes")
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    button9.destroy()
    # framee = Frame(framem, relief=SUNKEN, height=550, width=520, bd=1,pady = 30)
    # framee.grid(row=1, column=0)
    image_play = Image.open("play_again3.png")
    image_play = image_play.resize((200,90),Image.ANTIALIAS)
    play_photo = ImageTk.PhotoImage(image_play)
    play_again_button = Button(root,image = play_photo,bg = 'cyan',bd = 0,command = play_again)
    play_again_button.place(relx = 0.3,rely = 0.84)

    image_exit = Image.open("exit2.png")
    image_exit = image_exit.resize((190, 100), Image.ANTIALIAS)
    exit_photo = ImageTk.PhotoImage(image_exit)
    exit_again_button = Button(root, image=exit_photo, bg='cyan', bd=0,command = exit)
    exit_again_button.place(relx=0.55, rely=0.84)



###  play Frame start from here
mixer.music.load("Welcome.mp3")
mixer.music.play()
# Title Frame

framea = Frame(root, relief=SUNKEN, height=1000, width=300, bd=25)
framea.pack(side=TOP)

# Title
Label(framea, text="Welcome TIC TAC TOE World", font="lucida 30 bold", fg='darkblue').pack()

# Main Frame of all Centre Frame
frame_First_page = Frame(root, relief=SUNKEN,bg = "cyan")
frame_First_page.place(relx=0.0, rely=0.2, relwidth=1, relheight=1)
#
#
frame_Tic_toe_image = Frame(frame_First_page, relief=SUNKEN, height=300, width=250,bg = 'cyan')
frame_Tic_toe_image.place(relx=0.0, rely=0.08, relwidth=1, relheight=1)


image = Image.open("t3.png")
image = image.resize((400,300),Image.ANTIALIAS)
Tic_photo = ImageTk.PhotoImage(image)
Tic_label = Label(frame_Tic_toe_image,image = Tic_photo,bg = "cyan")
Tic_label.pack()

img = Image.open("play.png")
img = img.resize((220,80),Image.ANTIALIAS)
play_photo = ImageTk.PhotoImage(img)
play_button = Button(frame_Tic_toe_image,image = play_photo,bd = 0,bg = 'cyan')
play_button.pack(pady = 30)
play_button.bind("<Button-1>", play)


root.mainloop()
