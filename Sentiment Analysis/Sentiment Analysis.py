from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox as ms
from textblob import TextBlob
from tkinter import filedialog




class Sentiment_analysis:



    def __init__(self,root):
        self.root = root
        root.title("Sentiment Analysis")
        root.state('zoomed')
        root.resizable(width=0,height=0)

        # header frame
        header_frame = Frame(root,bg = 'pink',borderwidth = 30,relief = 'sunken',highlightbackground="#51f542",highlightthickness=4)
        header_frame.place(relx = 0 , rely = 0 , relwidth = 1,relheight = 0.2)
        label = Label(header_frame,text = "Sentiment Analysis",bg = "pink",fg = '#e817bb',font = ('comicsansms',50,'bold','underline'), pady = 25)
        label.pack()

        # two sentiment images in header frame
        self.img1 = Image.open("images/sentiment analysis png hd logo images for project1.png")
        self.img1 = self.img1.resize((150, 95), Image.ANTIALIAS)
        self.deco = ImageTk.PhotoImage(self.img1)
        img_label = Label(header_frame, image=self.deco, bg="pink")
        img_label.place(relx=0.002, rely=0.02)

        self.img1 = Image.open("images/sentiment analysis png hd logo images for project3.png")
        self.img1 = self.img1.resize((150, 95), Image.ANTIALIAS)
        self.deco1 = ImageTk.PhotoImage(self.img1)
        img_label = Label(header_frame, image=self.deco1, bg="pink")
        img_label.place(relx=0.89, rely=0.02)

        # # created main frame here
        # self.Main_frame = Frame(root,bg = "#00ffff")
        # self.Main_frame.place(rely = 0.2,relwidth = 1,relheight = 1)



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
                    self.login_body()
                else:
                    ms.showerror("Validation", "Ivalid Username and password")

        self.sub_main_frame = Frame(self.Main_frame)
        self.sub_main_frame.configure(bd = 5,relief = GROOVE,highlightbackground="#f542e3",highlightthickness=3)
        self.sub_main_frame.place(relx = 0.23,rely = 0.1, relwidth = 0.55,relheight = 0.38)

        label = Label(self.sub_main_frame,text = "Username :",padx = 60,pady = 37,font = ('comicsansms',25,'bold'),fg = 'red')
        label.place(relx = 0.02,rely = 0.2,relwidth = 0.3,relheight = 0.2)

        label = Label(self.sub_main_frame, text="Password :", padx=60, pady=37, font=('comicsansms', 25, 'bold'),
                      fg='red')
        label.place(relx=0.02, rely=0.55, relwidth=0.3, relheight=0.2)

        user_value = StringVar()
        pass_value = StringVar()

        user_entry = Entry(self.sub_main_frame, textvariable=user_value, width=25, bd=5, font="large_font 20",justify=LEFT, insertwidth=2)
        user_entry.focus()
        user_entry.place(relx = 0.38,rely = 0.2,relwidth = 0.56,relheight = 0.14)

        pass_entry = Entry(self.sub_main_frame, textvariable=pass_value, width=25, bd=5, font="large_font 20",
                           justify=LEFT, insertwidth=.1, show="*")
        pass_entry.place(relx = 0.38,rely = 0.55,relwidth = 0.56,relheight = 0.14)

        self.img = Image.open("images/login.png")
        self.img = self.img.resize((220, 80), Image.ANTIALIAS)
        self.login_photo = ImageTk.PhotoImage(self.img)

        self.login_button = Button(self.Main_frame, image=self.login_photo, font="comicsansms 25 bold",  bd=0,
                              bg="powder blue",command = login)
        self.login_button.place(relx=0.52, rely=0.57)

        self.img = Image.open("images/reset.png")
        self.img = self.img.resize((220, 80), Image.ANTIALIAS)
        self.reset_photo = ImageTk.PhotoImage(self.img)

        self.reset_button = Button(self.Main_frame, image=self.reset_photo , font="comicsansms 25 bold",  bd=0,
                              bg="powder blue",command = reset)
        self.reset_button.place(relx=0.32, rely=0.57)




    def Main_body(self):
        # created main frame here
        self.Main_frame = Frame(root, bg="#00ffff")
        self.Main_frame.place(rely=0.2, relwidth=1, relheight=1)
        self.sub_main_body()





    def login_body(self):

        def logout():
            self.sub_main_frame.destroy()
            self.Main_body()

        def Review_Analysis():
            self.frame_sub_login_body.destroy()
            self.Review_Analysis_body()


        def Spam_Detection():
            # self.frame_sub_login_body.destroy()
            self.Spam_Detection_body()


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


        # sub frame
        self.frame_sub_login_body = Frame(self.Main_frame)
        self.frame_sub_login_body.configure(bd=5, relief=GROOVE)
        self.frame_sub_login_body.place(relx=0.3, rely=0.15, relwidth=0.42, relheight=.4)

        Review_Analysis_button = Button(self.frame_sub_login_body, text="Review Analysis", font="comicsansms 25 bold", padx=20,pady=2, bg="#7ee431", command=Review_Analysis, width=20)
        Review_Analysis_button.place(relx=0.1, rely=0.2)

        Spam_Detection_button = Button(self.frame_sub_login_body, text="Spam Detection", font="comicsansms 25 bold", padx=20, pady=2,bg="#7ee431", command=Spam_Detection, width=20)
        Spam_Detection_button.place(relx=0.1, rely=0.6)




    def Review_Analysis_body(self):


        def Home():
            self.frame_Review_body.destroy()
            self.login_body()

        def Single_Feedback_Prediction():
            self.frame_Review_body.destroy()
            self.Single_Feedback_Prediction_body()

        def Bulk_Feedback_Prediction():
            self.frame_Review_body.destroy()
            self.Bulk_Feedback_Prediction_body()


        # Home image button
        self.img = Image.open("images/home6.png")
        self.img = self.img.resize((80, 60), Image.ANTIALIAS)
        self.Home_photo = ImageTk.PhotoImage(self.img)

        Home_button = Button(self.Main_frame, image=self.Home_photo, command=Home, bd=0, bg="powder blue")
        Home_button.place(relx=0.78, rely=0.002)

        # Admin frame
        frame_admin_welcome = Frame(self.Main_frame)
        frame_admin_welcome.configure(relief=SUNKEN, bg="#f79c96")
        frame_admin_welcome.place(relx=0.0001, rely=0.001, relwidth=0.23, relheight=.1)

        label = Label(frame_admin_welcome, text="Welcome Admin", font=('comicsansms', 25, 'bold'), bg="#f79c96")
        label.pack(anchor=CENTER)


        # sub frame
        self.frame_Review_body = Frame(self.Main_frame)
        self.frame_Review_body.configure(bd=5, relief=GROOVE)
        self.frame_Review_body.place(relx=0.3, rely=0.15, relwidth=0.42, relheight=.4)

        Single_Feedback_Prediction_button = Button(self.frame_Review_body, text="Single Feedback Prediction", font="comicsansms 25 bold", padx=20,pady=2, bg="#7ee431", command=Single_Feedback_Prediction, width=20)
        Single_Feedback_Prediction_button.place(relx=0.1, rely=0.2)

        Bult_Feedback_Prediction_button = Button(self.frame_Review_body, text="Bulk Feedback Prediction", font="comicsansms 25 bold", padx=20,pady=2,bg="#7ee431", command= Bulk_Feedback_Prediction, width=20)
        Bult_Feedback_Prediction_button.place(relx=0.1, rely=0.6)



    def Single_Feedback_Prediction_body(self):




        def Clear():

            self.Predict_label.configure(text="",bg = "#F1F1F1")
            self.user_value.set("")


        def Home():
            self.Single_Feedback_Prediction_frame.destroy()
            self.Predict_button.destroy()
            self.Clear_button.destroy()
            self.login_body()

        def Predict():

            self.message = self.Enter_msg_entry.get()
            self.blob = TextBlob(self.message)
            self.polarity = self.blob.polarity
            self.subjectivity = self.blob.subjectivity

            if self.polarity > 0:
                self.Predict_label.configure(text="Positive Sentiment", fg='red', bg='yellow')

            elif self.polarity < 0:
                self.Predict_label.configure(text="Negative Sentiment", fg='red', bg='yellow')

            else:
                self.Predict_label.configure(text="No Sentiment", fg='red', bg='yellow')

        # Home image button
        self.img = Image.open("images/home6.png")
        self.img = self.img.resize((80, 60), Image.ANTIALIAS)
        self.Home_photo = ImageTk.PhotoImage(self.img)

        Home_button = Button(self.Main_frame, image=self.Home_photo, command=Home, bd=0, bg="powder blue")
        Home_button.place(relx=0.78, rely=0.002)


        # sub frame
        self.Single_Feedback_Prediction_frame = Frame(self.Main_frame)
        self.Single_Feedback_Prediction_frame.configure(bd=5, relief=GROOVE)
        self.Single_Feedback_Prediction_frame.place(relx=0.22, rely=0.16, relwidth=0.56, relheight=.4)

        label = Label(self.Single_Feedback_Prediction_frame, text="Enter Msg :", padx=60, pady=37, font=('comicsansms', 25, 'bold'),fg='red')
        label.place(relx=0.02, rely=0.32, relwidth=0.3, relheight=0.26)

        self.user_value = StringVar()
        self.Enter_msg_entry = Entry(self.Single_Feedback_Prediction_frame, textvariable = self.user_value, width=25, bd=5, font="large_font 30",justify=LEFT, insertwidth=2)
        self.Enter_msg_entry.focus()
        self.Enter_msg_entry.place(relx=0.35, rely=0.32, relwidth=0.6, relheight=0.26)

        self.Predict_label = Label(self.Single_Feedback_Prediction_frame, text="",
                                   font=('comicsansms', 25, 'bold'), )
        self.Predict_label.place(relx=0.34, rely=0.65, relwidth=0.4, relheight=0.26)


        # predict image button
        self.img = Image.open("images/picture1.png")
        self.img = self.img.resize((250, 100), Image.ANTIALIAS)
        self.predict = ImageTk.PhotoImage(self.img)

        self.Predict_button = Button(self.Main_frame, image=self.predict, command=Predict, bd=0, bg="powder blue")
        self.Predict_button.place(relx=0.28, rely=0.6)

        # Clear Image Button
        self.img = Image.open("images/picture4.png")
        self.img = self.img.resize((250, 100), Image.ANTIALIAS)
        self.Clear = ImageTk.PhotoImage(self.img)

        self.Clear_button = Button(self.Main_frame, image=self.Clear, command=Clear, bd=0, bg="powder blue")
        self.Clear_button.place(relx=0.5, rely=0.6)





    # Bulk Feedback Prediction method
    def Bulk_Feedback_Prediction_body(self):

        def Clear():

            self.Predict_label.configure(text="", bg="#F1F1F1")
            self.user_value_source.set("")
            self.user_value_destination.set("")

        def Home():
            self.Bulk_Feedback_Prediction_frame.destroy()
            self.Clear_button.destroy()
            self.Predict_button.destroy()
            self.Browse_button.destroy()
            self.Browse_button1.destroy()
            self.login_body()

        def Browse_source():
            file_path = filedialog.askopenfilename()
            self.user_value_source.set(file_path)


        def Browse_destination():
            file_path = filedialog.askdirectory()
            self.user_value_destination.set(file_path+'/'+'Result.txt')


        def Predict():

            self.source_path = self.user_value_source.get()
            self.Destination_path = self.user_value_destination.get()
            self.write_file = open(self.Destination_path,'w')
            with open(self.source_path,'r') as f:
                self.full_message = f.readlines()
                for self.message in self.full_message:
                    self.message = self.message.replace('\n','')
                    if self.message == " ":
                        self.write_file.close()
                        break
                    else:
                        self.blob = TextBlob(self.message)
                        self.polarity = self.blob.polarity
                        self.subjectivity = self.blob.subjectivity

                        if self.polarity > 0:
                            self.message_with_sentiment = self.message + "    ------>     " + "Possitive Review \n"
                            print(self.message_with_sentiment)
                            self.write_file.write(self.message_with_sentiment)

                        elif self.polarity < 0:
                            self.message_with_sentiment = self.message + "    ------>     " + "Negative Review \n"
                            self.write_file.write(self.message_with_sentiment)

                        else:
                            self.message_with_sentiment = self.message + "    ------>     " + "Normal \n"
                            self.write_file.write(self.message_with_sentiment)
            self.write_file.close()
            ms.showinfo("Done Sentiment Analysis",'See Result file at destination location')


        # Home image button
        self.img = Image.open("images/home6.png")
        self.img = self.img.resize((80, 60), Image.ANTIALIAS)
        self.Home_photo = ImageTk.PhotoImage(self.img)

        Home_button = Button(self.Main_frame, image=self.Home_photo, command=Home, bd=0, bg="powder blue")
        Home_button.place(relx=0.78, rely=0.002)

        # sub frame
        self.Bulk_Feedback_Prediction_frame = Frame(self.Main_frame)
        self.Bulk_Feedback_Prediction_frame.configure(bd=5, relief=GROOVE)
        self.Bulk_Feedback_Prediction_frame.place(relx=0.1, rely=0.16, relwidth=0.7, relheight=.4)

        # label source
        label_source = Label(self.Bulk_Feedback_Prediction_frame, text="Select Source File : ",
                      font=('comicsansms', 25, 'bold'), fg='red')
        label_source.place( rely=0.22, relwidth=0.41, relheight=0.26)

        # label destination
        label_destination = Label(self.Bulk_Feedback_Prediction_frame, text="Select Destin Path : ",
                      font=('comicsansms', 25, 'bold'), fg='red')
        label_destination.place(rely=0.6, relwidth=0.41, relheight=0.26)

        # user entry source
        self.user_value_source = StringVar()
        self.Enter_msg_entry_source = Entry(self.Bulk_Feedback_Prediction_frame, textvariable=self.user_value_source, width=25,bd=5, font="large_font 30", justify=LEFT, insertwidth=2,fg = 'darkblue')
        self.Enter_msg_entry_source.place(relx=0.37, rely=0.22, relwidth=0.62, relheight=0.26)

        # user entry destination
        self.user_value_destination = StringVar()
        self.Enter_msg_entry_destination = Entry(self.Bulk_Feedback_Prediction_frame, textvariable=self.user_value_destination, width=25,bd=5, font="large_font 30", justify=LEFT, insertwidth=2,fg = 'blue')
        self.Enter_msg_entry_destination.place(relx=0.37, rely=0.6, relwidth=0.62, relheight=0.26)

        # Browse image button
        self.img = Image.open("images/picture5.png")
        self.img = self.img.resize((200, 75), Image.ANTIALIAS)
        self.Browse = ImageTk.PhotoImage(self.img)

        self.Browse_button = Button(self.Main_frame, image=self.Browse, command=Browse_source, bd=0, bg="powder blue")
        self.Browse_button.place(relx=0.81, rely=0.25)

        # Browse image button
        self.img = Image.open("images/picture5.png")
        self.img = self.img.resize((200, 75), Image.ANTIALIAS)
        self.Browse1 = ImageTk.PhotoImage(self.img)

        self.Browse_button1 = Button(self.Main_frame, image=self.Browse1, command=Browse_destination, bd=0, bg="powder blue")
        self.Browse_button1.place(relx=0.81, rely=0.4)

        # predict image button
        self.img = Image.open("images/picture1.png")
        self.img = self.img.resize((250, 100), Image.ANTIALIAS)
        self.predict = ImageTk.PhotoImage(self.img)

        self.Predict_button = Button(self.Main_frame, image=self.predict, command=Predict, bd=0, bg="powder blue")
        self.Predict_button.place(relx=0.25, rely=0.6)

        # Clear Image Button
        self.img = Image.open("images/picture4.png")
        self.img = self.img.resize((250, 100), Image.ANTIALIAS)
        self.Clear = ImageTk.PhotoImage(self.img)

        self.Clear_button = Button(self.Main_frame, image=self.Clear, command=Clear, bd=0, bg="powder blue")
        self.Clear_button.place(relx=0.5, rely=0.6)




















    def Spam_Detection_body(self):
        pass
        # def logout():
        #     self.sub_main_frame.destroy()
        #     self.Main_body()
        #
        # def Home():
        #     self.frame_Review_body.destroy()
        #     self.login_body()
        #
        # def Single_Prediction():
        #     self.frame_sub_login_body.destroy()
        #     self.Single_Prediction_body()
        #
        # def Bulk_Prediction():
        #     self.frame_sub_login_body.destroy()
        #     self.Bulk_Prediction_body()
        #
        #
        # # Home image button
        # self.img = Image.open("images/home6.png")
        # self.img = self.img.resize((80, 60), Image.ANTIALIAS)
        # self.Home_photo = ImageTk.PhotoImage(self.img)
        #
        # Home_button = Button(self.Main_frame, image=self.Home_photo, command=Home, bd=0, bg="powder blue")
        # Home_button.place(relx=0.78, rely=0.002)
        #
        # # Admin frame
        # frame_admin_welcome = Frame(self.Main_frame)
        # frame_admin_welcome.configure(relief=SUNKEN, bg="#f79c96")
        # frame_admin_welcome.place(relx=0.0001, rely=0.001, relwidth=0.23, relheight=.1)
        #
        # label = Label(frame_admin_welcome, text="Welcome Admin", font=('comicsansms', 25, 'bold'), bg="#f79c96")
        # label.pack(anchor=CENTER)
        #
        # # Logout image button
        # self.img = Image.open("images/logout.png")
        # self.img = self.img.resize((200, 60), Image.ANTIALIAS)
        # self.logout_photo = ImageTk.PhotoImage(self.img)
        #
        # logout_button = Button(self.Main_frame, image=self.logout_photo, command=logout, bd=0, bg="powder blue")
        # logout_button.place(relx=0.85, rely=0.002)
        #
        # # sub frame
        # self.frame_Spam_body = Frame(self.Main_frame)
        # self.frame_Spam_body.configure(bd=5, relief=GROOVE)
        # self.frame_Spam_body.place(relx=0.3, rely=0.15, relwidth=0.42, relheight=.4)
        #
        # Single_Prediction_button = Button(self.frame_Spam_body, text="Single Prediction", font="comicsansms 25 bold", padx=20,pady=2, bg="#7ee431", command=Single_Prediction, width=20)
        # Single_Prediction_button.place(relx=0.1, rely=0.2)
        #
        # Bult_Prediction_button = Button(self.frame_Spam_body, text="Bult Prediction", font="comicsansms 25 bold", padx=20,pady=2,bg="#7ee431", command= Bulk_Prediction, width=20)
        # Bult_Prediction_button.place(relx=0.1, rely=0.6)





    def Single_Prediction_body(self):

        pass
        # # sub frame
        # self.frame_Review_body = Frame(self.Main_frame)
        # self.frame_Review_body.configure(bd=5, relief=GROOVE)
        # self.frame_Review_body.place(relx=0.3, rely=0.15, relwidth=0.42, relheight=.4)


    def Bulk_Prediction_body(self):
        pass
        # sub frame
        # self.frame_Review_body = Frame(self.Main_frame)
        # self.frame_Review_body.configure(bd=5, relief=GROOVE)
        # self.frame_Review_body.place(relx=0.3, rely=0.15, relwidth=0.42, relheight=.4)









root = Tk()
root_object = Sentiment_analysis(root)
root_object.Main_body()
root.mainloop()
