from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as ms
import os
import time
import nltk
from textblob import TextBlob
from tkinter import filedialog
import threading
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import glob
import re
from tkinter.ttk import Combobox
import docxpy
import shutil
from check import All_Shortlisted_Resumes



class Resume_Shortlister:



    def __init__(self,root):
        self.root = root

        root.title("Sentiment Analysis")
        root.state('zoomed')
        root.resizable(width=0,height=0)

        # header frame

        self.header_frame = Frame(root,bg = 'pink',borderwidth = 30,relief = 'sunken',highlightbackground="#51f542",highlightthickness=5)
        self.header_frame.place(relx = 0 , rely = 0 , relwidth = 1,relheight = 0.21)
        self.header_frame_label = Label(self.header_frame,text = "Automation Resume Shortlist",bg = "pink",fg = '#e817bb',font = ('comicsansms',50,'bold','underline'), pady = 25)
        self.header_frame_label.pack()






    # Motion widgets
    def Motion(self):
        lis = os.listdir(r"images\motion")
        i = j = 0
        color_list = ['#0000cc', '#42d4f5', '#0000ff', '#003399', '#0055ff', '#3366cc', '#00ff00', '#ff00ff',
                           '#ff33ff', '#ff0066', '#e6005c', '#ff0000', '#33ccff', '#00bfff', '#1a75ff', '#4040bf',
                           '#00aaff', '#00e6ac', '#00cc99', '#53ff1a', '#00cc44', '#ace600', '#99cc00', '#804000',
                           '#663300', '#ff3333', '#b38600', '#9900ff', '#a31aff', '#00b300', '#ff9900', '#cc0099',
                           '#00e6e6', '#0099cc', '#5500ff', '#77773c', '#666699', '#ff471a', '#cccc00', '#99cc00',
                           '#00e600', '#4d9900', '#00e600', '#33d6ff', '#3333cc']

        mix_color_list = ['#42d4f5','#0000cc','#ff6600','#ffb380','#e65c00','#cc0066','#ff80bf','#00cc66','#99ffcc','#00994d','#00e6e6','#009999','#e6e600','#f56642','#f57b42','#f5ad42','#f5c842','#f5ef42','#d7f542','#bcf542','#96f542','#54f542','#42f59e','#42f5c5','#42f5f5','#42c5f5','#429ef5','#4269f5','#4542f5','#5d42f5','#8a42f5','#a142f5','#ce42f5','#f542f2','#f542b3','#f5427e','#f54257','#ff99ff','#cc00cc','#1a1aff']

        self.header_time = time.time()
        print(self.header_time)
        self.header_label_timer = 1
        while True:
            if threading.main_thread().is_alive():
                pass
            else:
                break
            try:
                if time.time() - self.header_time  >= self.header_label_timer:
                    self.header_frame_label.configure(fg=color_list[j])
                    try:
                        self.Admin_label.configure(fg = color_list[j+2])
                        self.Admin_login_frame.configure(bg = mix_color_list[j])
                    except:
                        pass


                # two sentiment images in header frame
                self.img1 = Image.open(f"images/motion/{lis[i]}")
                self.img1 = self.img1.resize((150, 95), Image.ANTIALIAS)
                self.deco = ImageTk.PhotoImage(self.img1)
                img_label = Label(self.header_frame, image=self.deco, bg="pink")
                img_label.place(relx=0.002, rely=0)


                self.img1 = Image.open(f"images/motion/{lis[i]}")
                self.img1 = self.img1.resize((150, 95), Image.ANTIALIAS)
                self.deco1 = ImageTk.PhotoImage(self.img1)
                img_label = Label(self.header_frame, image=self.deco1, bg="pink")
                img_label.place(relx=0.89, rely=0)
                time.sleep(2)
                i += 1
                j += 1

                if len(lis)-2 == i:
                    lis = os.listdir(r"F:\Data Science\DataScience Aditya Sir\56. Textblob\sentiment analysis\Advance Image Downloader Tkinter\images\motion")
                    i = 0
                elif len(color_list) - 1 == j:
                    color_list = ['#42d4f5', '#f56642', '#f57b42', '#f5ad42', '#f5c842', '#f5ef42', '#d7f542', '#bcf542',
                                  '#96f542', '#54f542', '#42f59e', '#42f5c5', '#42f5f5', '#42c5f5', '#429ef5', '#4269f5',
                                  '#4542f5', '#5d42f5', '#8a42f5', '#a142f5', '#ce42f5', '#f542f2', '#f542b3', '#f5427e',
                                  '#f54257']
                    j = 0
            except:
                pass


    # Sub main body
    def sub_main_body(self):

        def reset():
            self.Main_body()

        def login():
            u = user_entry.get()
            p = pass_entry.get()
            if u == "" and p == "":
                ms.showwarning("Validation", "Username and password can't be empty")
            else:
                if u == "admin" and p == "admin":
                    self.sub_main_frame.destroy()
                    self.login_button.destroy()
                    self.reset_button.destroy()
                    self.Admin_login_frame.destroy()
                    self.login_body()
                else:
                    ms.showerror("Validation", "Invalid Username and password")

        self.sub_main_frame = Frame(self.Main_frame)
        self.sub_main_frame.configure(bd = 5, relief=GROOVE,highlightbackground="pink",highlightthickness=0)
        self.sub_main_frame.place(relx = 0.23,rely = 0.2, relwidth = 0.55,relheight = 0.4)

        # Admin Login frame
        self.Admin_login_frame = Frame(self.Main_frame)
        self.Admin_login_frame.configure(bd=5, relief=GROOVE)
        self.Admin_login_frame.place(relx=0.385, rely=0.085, relwidth=0.25, relheight=0.12)


        # Admin label
        self.Admin_label = Label(self.Admin_login_frame, text="Admin Login", font=('comicsansms', 29, 'bold'),
                      fg='black')
        self.Admin_label.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

        # user label
        label = Label(self.sub_main_frame,text = "Username :",padx = 60,pady = 37,font = ('comicsansms',25,'bold'),fg = 'red')
        label.place(relx = 0.02,rely = 0.2,relwidth = 0.3,relheight = 0.2)

        # password label
        label = Label(self.sub_main_frame, text="Password :", padx=60, pady=37, font=('comicsansms', 25, 'bold'),
                      fg='red')
        label.place(relx=0.02, rely=0.55, relwidth=0.3, relheight=0.2)

        user_value = StringVar()
        pass_value = StringVar()


        # user value entry
        user_entry = Entry(self.sub_main_frame, textvariable=user_value, width=35, bd=5, font="large_font 20",justify=LEFT, insertwidth=2,fg = 'darkblue')
        user_entry.focus()
        user_entry.place(relx = 0.38,rely = 0.22,relwidth = 0.56,relheight = 0.16)


        # password value entry
        pass_entry = Entry(self.sub_main_frame, textvariable=pass_value, width=25, bd=5, font="large_font 20",fg = 'darkblue',
                           justify=LEFT, insertwidth=.1, show="*")
        pass_entry.place(relx = 0.38,rely = 0.57,relwidth = 0.56,relheight = 0.16)


        # login image button
        self.img = Image.open("images/login.png")
        self.img = self.img.resize((250, 80), Image.ANTIALIAS)
        self.login_photo = ImageTk.PhotoImage(self.img)

        self.login_button = Button(self.Main_frame, image=self.login_photo, font="comicsansms 25 bold",  bd=0,
                              bg="powder blue",command = login)
        self.login_button.place(relx=0.54, rely=0.65)

        # Reset image button
        self.img = Image.open("images/reset.png")
        self.img = self.img.resize((250, 80), Image.ANTIALIAS)
        self.reset_photo = ImageTk.PhotoImage(self.img)

        self.reset_button = Button(self.Main_frame, image=self.reset_photo , font="comicsansms 25 bold",  bd=0,
                              bg="powder blue",command = reset)
        self.reset_button.place(relx=0.28, rely=0.65)





    def Main_body(self):
        # created main frame here
        self.Main_frame = Frame(root, bg="#00ffff")
        self.Main_frame.place(rely=0.21, relwidth=1, relheight=1)
        self.sub_main_body()












    def login_body(self):

        self.Requirement_value = StringVar()
        self.Resume_value = StringVar()
        self.Destination_value = StringVar()


        def logout():
            self.Main_frame.destroy()
            self.Main_body()


        def Browse_Requirement_file():
            # selected_or_not = self.course_combobox.get()
            # if selected_or_not !="Select Your File Choice":
            #      self.course_combobox.configure(state = 'disabled')
            self.requirement_file = filedialog.askopenfilename()
            self.Requirement_value.set(self.requirement_file)


        def Browse_Resume_file():
            self.requirement_file = filedialog.askdirectory()
            self.Resume_value.set(self.requirement_file)


        def Browse_Destination_file():
            self.requirement_file = filedialog.askdirectory()
            self.Destination_value.set(self.requirement_file)

        def Extract_Resume():

                with open(f'{self.Requirement_value.get()}','r') as file:
                    data = file.read()
                    lemitezer_obj = WordNetLemmatizer()
                    document = re.sub('[^a-zA-Z]', " ", data)
                    document = document.lower()
                    document = [lemitezer_obj.lemmatize(word) for word in nltk.word_tokenize(document) if
                                word not in stopwords.words('English')]
                    document = [i for i in document if len(i) != 1]
                    document = " ".join(document)
                    document = set(document.split())
                    print(document)

                global All_Sort_Listed_Resumes,Word_matched
                All_Sort_Listed_Resumes = []
                Word_matched = []
                Type = self.course_combobox.get()
                print(Type)
                if Type == "Select Your File Choice":
                    ms.showwarning('Invalid File Choice','Please Select The File Type')
                # "All Docx Files", 'All Doc Files', 'Single File', 'All Files'

                if Type == "All Docx Files":
                    all_resume_files = glob.glob(f'{self.Resume_value.get()}/*.docx')
                    print(all_resume_files)
                    All_Sort_Listed_Resumes = []
                    Word_matched = []
                    for f in all_resume_files:
                        text = docxpy.process(f)
                        text = text.lower()
                        count = 0
                        word = []
                        for doc_text in document:
                            if doc_text in text:
                                print(doc_text, '----------------- doc text ---------------')
                                word.append(doc_text)
                                count += 1
                        percent = count / len(document) * 100
                        print(percent)
                        if percent > 20:
                            All_Sort_Listed_Resumes.append(f)
                            print('Sortlisted---------------------------------------------')
                            Word_matched.append(word)

                elif Type == 'All Doc Files':
                    all_resume_files = glob.glob(f'{self.Resume_value.get()}/*.doc')
                    print(all_resume_files)
                    All_Sort_Listed_Resumes = []
                    Word_matched = []
                    for f in all_resume_files:
                        text = docxpy.process(f)
                        text = text.lower()
                        count = 0
                        word = []
                        for doc_text in document:
                            if doc_text in text:
                                print(doc_text, '----------------- doc text ---------------')
                                word.append(doc_text)
                                count += 1
                        percent = count / len(document) * 100
                        print(percent)
                        if percent > 20:
                            All_Sort_Listed_Resumes.append(f)
                            print('Sortlisted---------------------------------------------')
                            Word_matched.append(word)



                elif Type == 'All Files':
                    all_resume_files = glob.glob(f'{self.Resume_value.get()}/*.docx')
                    print(all_resume_files)
                    All_Sort_Listed_Resumes = []
                    Word_matched = []
                    for f in all_resume_files:
                        text = docxpy.process(f)
                        text = text.lower()
                        count = 0
                        word = []
                        for doc_text in document:
                            if doc_text in text:
                                print(doc_text, '----------------- doc text ---------------')
                                word.append(doc_text)
                                count += 1
                        percent = count / len(document) * 100
                        print(percent)
                        if percent > 20:
                            All_Sort_Listed_Resumes.append(f)
                            print('Sortlisted---------------------------------------------')
                            Word_matched.append(word)


                elif Type == 'Specific Text Files':

                    all_resume_files = glob.glob(f'{self.Resume_value.get()}/*.txt')
                    print(all_resume_files)
                    All_Sort_Listed_Resumes = []
                    Word_matched = []
                    for f in all_resume_files:
                        # text = docxpy.process(f)
                        text = open(f, 'r')
                        text = text.read()
                        text = text.lower()
                        count = 0
                        word = []
                        for doc_text in document:
                            if doc_text in text:
                                print(doc_text, '----------------- doc text ---------------')
                                word.append(doc_text)
                                count += 1
                        percent = count / len(document) * 100
                        print(percent)
                        if percent > 20:
                            All_Sort_Listed_Resumes.append(f)
                            print('Sortlisted---------------------------------------------')
                            Word_matched.append(word)


                if len(All_Sort_Listed_Resumes) == 0:
                    if self.course_combobox.get() != "Select Your File Choice":
                        ms.showinfo('Resume Shorlisted','No Resume Shortlisted')

                else:
                    if not os.path.exists(f'{self.Destination_value.get()}/All Shortlisted Resumes'):
                        os.makedirs(f'{self.Destination_value.get()}/All Shortlisted Resumes')
                    try:
                        for resume in All_Sort_Listed_Resumes:
                            print(resume)
                            shutil.copy(resume,f'{self.Destination_value.get()}/All Shortlisted Resumes')

                        # root.destroy()
                        All_Shortlisted_Resumes(All_Sort_Listed_Resumes, Word_matched)
                        print("All Done")
                    except EXCEPTION as e:
                        print(e)
                    else:
                        print('all Thing Done')

        # Admin frame
        frame_admin_welcome = Frame(self.Main_frame)
        frame_admin_welcome.configure(relief=SUNKEN, bg="#f79c96")
        frame_admin_welcome.place(relx=0.0001, rely=0.001, relwidth=0.23, relheight=.1)
        label = Label(frame_admin_welcome, text="Welcome Admin", font=('comicsansms', 25, 'bold'), bg="#f79c96")
        label.pack(anchor=CENTER)

        # Logout image button
        self.img = Image.open("images/logout.png")
        self.img = self.img.resize((200, 60), Image.ANTIALIAS)
        self.logout_photo = ImageTk.PhotoImage(self.img)
        logout_button = Button(self.Main_frame, image=self.logout_photo, command=logout, bd=0, bg="powder blue")
        logout_button.place(relx=0.85, rely=0.002)


        self.sub_main_frame = Frame(self.Main_frame)
        self.sub_main_frame.configure(bd=1, relief=GROOVE, highlightbackground="#f542e3", highlightthickness=3,padx = 0,pady = 0)
        self.sub_main_frame.place(relx=0.1, rely=0.2, relwidth=0.75, relheight=0.4)


        # Requirement Label

        self.label = Label(self.sub_main_frame,text = 'Requirement File : ',font=('comicsansms', 20, 'bold'),fg = 'darkblue')
        self.label.grid(row = 0 ,column = 0,padx = 30,pady = 30)

        # Requirement value entry

        self.Requirement_entry = Entry(self.sub_main_frame, textvariable=self.Requirement_value, width=25, bd=5, font="large_font 20",justify=LEFT, insertwidth=2)
        self.Requirement_entry.place(relx=0.32, rely=0.09, relwidth=0.66, relheight=0.18)

        # Requirement Browse image button

        self.img = Image.open("images/Browse.png")
        self.img = self.img.resize((200, 75), Image.ANTIALIAS)
        self.Browse1 = ImageTk.PhotoImage(self.img)

        self.Browse_button1 = Button(self.Main_frame, image=self.Browse1, command=Browse_Requirement_file, bd=0,bg="powder blue")
        self.Browse_button1.place(relx=0.85, rely=0.22)



        # Resume Label
        self.label = Label(self.sub_main_frame, text='Resume File Path : ', font=('comicsansms', 20, 'bold'),fg='darkblue')
        self.label.grid(row=1, column=0, padx=30, pady=30)


        # Resumes value entry
        pass_entry = Entry(self.sub_main_frame, textvariable=self.Resume_value, width=25, bd=5, font="large_font 20",
                           justify=LEFT, insertwidth=.1)
        pass_entry.place(relx=0.32, rely=0.43, relwidth=0.66, relheight=0.18)


        # Resumes Browse image button
        self.img = Image.open("images/Browse.png")
        self.img = self.img.resize((200, 75), Image.ANTIALIAS)
        self.Browse2 = ImageTk.PhotoImage(self.img)

        self.Browse_button2 = Button(self.Main_frame, image=self.Browse2, command=Browse_Resume_file, bd=0,
                                     bg="powder blue")
        self.Browse_button2.place(relx=0.85, rely=0.36)

        # Destination Label
        self.label = Label(self.sub_main_frame, text='Destination Folder : ', font=('comicsansms', 20, 'bold'),fg='darkblue')
        self.label.grid(row=2, column=0, padx=30, pady=30)

        # Destination value entry
        Destination_Entry = Entry(self.sub_main_frame,textvariable = self.Destination_value,bd = 5,font = 'large_font 20',justify = LEFT,insertwidth = .1)
        Destination_Entry.place(relx = 0.32,rely = 0.76,relwidth = 0.66,relheight = 0.18)

        # Destination Browse image button
        self.img = Image.open("images/Browse.png")
        self.img = self.img.resize((200, 75), Image.ANTIALIAS)
        self.Browse3 = ImageTk.PhotoImage(self.img)

        self.Browse_button3 = Button(self.Main_frame, image=self.Browse2, command=Browse_Destination_file, bd=0, bg="powder blue")
        self.Browse_button3.place(relx=0.85, rely=0.5)

        # Combobox widget
        ''' n, ne, e, se, s, sw, w, nw, or center'''
        values = ["Select Your File Choice", "All Docx Files",'All Doc Files','Specific Text Files','All Files']
        self.course_combobox = Combobox(self.Main_frame,width = 20,height = 8, font="large_font 30",justify=LEFT,values = values,state = 'normal')
        self.course_combobox.pack()
        self.course_combobox.current(0)

        # login image button
        self.img = Image.open("images/Extract Resume.png")
        self.img = self.img.resize((270, 80), Image.ANTIALIAS)
        self.Extract_photo = ImageTk.PhotoImage(self.img)

        self.Extract_button = Button(self.Main_frame, image=self.Extract_photo, font="comicsansms 25 bold", bd=0,bg="powder blue", command=Extract_Resume)
        self.Extract_button.place(relx=0.4, rely=0.65)



    def Show_All_Sortlisted_Resumes(self):


        # self.sub_main_frame = Frame(self.Main_frame)
        # self.sub_main_frame.configure(bd=1, relief=GROOVE, highlightbackground="#f542e3", highlightthickness=3)
        # self.sub_main_frame.place(relx = 0.1, rely=0.15, relwidth=0.8, relheight=0.6)


        self.win = Tk()

        self.win.title("Sortlisted Resumes")
        self.win.state('zoomed')
        self.win.resizable(width=0, height=0)

        self.main_frame = Frame(self.win)
        self.main_frame.configure(bd=2, relief=GROOVE, highlightbackground="#f542e3", highlightthickness=3,bg = 'pink')
        self.main_frame.place(relx = 0, rely=0, relwidth=1, relheight=0.18)

        self.Resumes_label = Label(self.main_frame,text = 'Sortlisted Resumes',font = ('comicsansms',35,'bold','underline'),fg = 'red',pady = 20,bg = 'pink')
        self.Resumes_label.pack()

        self.sub_frame = Frame(self.win,bd=0,  highlightbackground="#f542e3", highlightthickness=3)
        self.sub_frame.place(rely=0.18, relwidth=1, relheight=1)

        self.textfield = Text(self.sub_frame,height = 50,width = 50)
        self.textfield.insert(INSERT,'hello')
        self.textfield.insert(END,'')
        self.textfield.place(relx = 0.1,rely = 0.1,relwidth = 0.4,relheight = 0.3)




if __name__ == '__main__':

    root = Tk()
    root_object = Resume_Shortlister(root)
    root_object.Main_body()
    th1 = threading.Thread(target=root_object.Motion)
    th1.start()

    root.mainloop()


















