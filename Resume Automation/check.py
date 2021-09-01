# from nltk.stem import WordNetLemmatizer,PorterStemmer
# from nltk.corpus import stopwords
# import re
# import nltk
# import os
# import glob
# import docxpy
#
#
#
#
#
# with open(r'F:\Data Science\DataScience Aditya Sir\1.  Datasets of Adity Sir\sentiment\vivek.txt', 'r') as file:
#     data = file.read()
#     lemitezer_obj = WordNetLemmatizer()
#     document = re.sub('[^a-zA-Z]', " ",data)
#     document = document.lower()
#     document = [lemitezer_obj.lemmatize(word) for word in nltk.word_tokenize(document) if word not in stopwords.words('English')]
#     document = [i for i in document if len(i) != 1]
#     document = " ".join(document)
#     document = set(document.split())
#     print(document)
#
#
# all_resume_files = glob.glob('C:/Users/Rana/Desktop/resume/*.txt')
# print(all_resume_files)
#
# for f in all_resume_files:
#     # text = docxpy.process(f)
#     text = open(f,'r')
#     text = text.read()
#     text = text.lower()
#     count = 0
#     for doc_text in document:
#
#         if doc_text in text:
#             print(count,doc_text, '----------------- doc text ---------------')
#             count+=1
#     percent = count / len(document)*100
#     print(percent)













# from tkinter import *
# import webbrowser
#
# def callback(url):
#     webbrowser.open_new(url)
#
# root = Tk()
# link1 = Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))
#
# link2 = Label(root, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>", lambda e: callback(r"C:\Users\Rana\Desktop\resume\my resume.txt"))
#
# root.mainloop()











# import tkinter as tk
#
# list_of_file_data = [["Data set 1!", "This is the contents of data set 1.", True],
#                      ["Data set 2!", "This is the contents of data set 2.", True],
#                      ["Data set 3!", "This is the contents of data set 3.", True]]
#
# class Example(tk.Tk):
#     def __init__(self):
#
#         tk.Tk.__init__(self)
#         self.geometry("350x200")
#         self.txt_frame = tk.Frame(self)
#         self.txt_frame.grid(row=1, column=1)
#         self.txt_box = tk.Text(self.txt_frame, width=40, height=15)
#         self.txt_box.pack()
#         self.update_textbox()
#
#     def update_textbox(self):
#         self.txt_box.delete(1.0, "end")
#         for ndex, data_set in enumerate(list_of_file_data):
#             if data_set[2] == True:
#                 self.txt_box.insert("end", "{}".format(data_set[0]))
#                 self.txt_box.window_create(self.txt_box.index("end"), window = tk.Button(self.txt_box, text="F", command=lambda x=ndex: self.toggle_data(x)))
#                 self.txt_box.insert("end", "\n")
#                 self.txt_box.insert("end", "    {}\n\n".format(data_set[1]))
#             else:
#                 self.txt_box.insert("end", "{}".format(data_set[0]))
#                 self.txt_box.window_create(self.txt_box.index("end"), window = tk.Button(self.txt_box, text="F", command=lambda x=ndex: self.toggle_data(x)))
#                 self.txt_box.insert("end", "\n...\n")
#
#
#     def toggle_data(self, ndex):
#         if list_of_file_data[ndex][2] == True:
#             list_of_file_data[ndex][2] = False
#         else:
#             list_of_file_data[ndex][2] = True
#         self.update_textbox()
#
#
# if __name__ == "__main__":
#     Example().mainloop()
#
#
#

# import tkinter as tk
# from tkinter import *
# from tkinter import messagebox as msg
# root = tk.Tk()
# root.state('zoomed')
# f = tk.Frame(root)
# f.place(x=10, y=20)
#
# def Report():
#     msg.showinfo('report','clicked')
#
#
# scrollbar = Scrollbar(f)
# t = tk.Text(f, height=40, width=160, yscrollcommand=scrollbar.set)
# for index1,i in enumerate(range(150)):
#     t.window_create(t.index("insert"),padx = 59,
#                     window=tk.Button(t, text="Click To See Result", command=lambda x=index1: Report()))
#
#     t.insert(END,'\n\n')
#     t.insert(INSERT,i)
# scrollbar.config(command=t.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# t.pack(side="right")
#
# root.mainloop()


















import webbrowser
from tkinter import *
from tkinter import Scrollbar

def reset_tabs(event):
    '''Add a tabstop at the right edge of the widget'''
    right_margin = event.width - 8
    if right_margin <= 0: return
    tabs = (right_margin, "right")
    event.widget.configure(tabs=tabs)

def callback(text,word_matched):
    index  = int("{}".format(text))

    win = Tk()
    win.geometry('780x500')
    win.resizable(width = 0,height=0)
    win.title('Top Most Words')
    header_frame = Frame(win, bg='pink', borderwidth=4, relief='sunken', highlightbackground="white",highlightthickness=8)
    header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)
    header_frame_label = Label(header_frame, text="Top Most Words That Satisfying Requirements", bg="pink", fg='#e817bb',font=('comicsansms', 25, 'bold'), pady=18)
    header_frame_label.pack()

    text_frame = Frame(win, borderwidth=0, relief='sunken', highlightbackground="white",highlightthickness=8)
    text_frame.place(relx=0, rely=0.15, relwidth=1, relheight=0.85)
    # text_frame.pack(side = BOTTOM)
    # ne, e, se, s, sw, w, nw
    scrollbar = Scrollbar(text_frame)

    text = Text(text_frame, font=('comicsansms', 10, 'bold'), fg='darkblue', pady=5, padx=15, yscrollcommand=scrollbar.set,state = 'disabled')
    text.pack(fill="both", expand=True)
    text.bind("<Configure>", reset_tabs)

    j = 0
    for i, link in enumerate(word_matched[index]):
        if j == 0:
            label1 = Label(text, text=f'{link}\n', font=('comicsansms', 20, 'bold'), width='36',fg='darkblue', bg='orange')

            text.window_create('insert', window=label1,padx = 45)
            j = 1

        elif j == 1:
            global label2
            label2 = Label(text, text=f'{link}\n', font=('comicsansms', 20, 'bold'), width='36',fg='darkblue', bg='pink')

            text.window_create('end-2c', window=label2, padx=45, pady=20 )
            j = 0
    scrollbar.config(command=text.yview, bg='red')
    scrollbar.pack(side=RIGHT, fill=Y)
    text.pack(side='left',padx = 0)




















global label2
def callback2(event):
    print(event.widget.cget('text'))
    webbrowser.open_new(event.widget.cget('text'))


# All_Sort_Listed_Resumes,Word_matched
def All_Shortlisted_Resumes(All_Sort_Listed_Resumes,Word_matched):

    root =  Tk()

    root.state('zoomed')
    root.resizable(width=0,height=0)
    # word_matched = [['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me'],['hello','vivek','i','have','completed','python','i','hope','feel','good','about','me']]
    header_frame =  Frame(root, bg='pink', borderwidth=30, relief='sunken', highlightbackground="#51f542",highlightthickness=5)
    header_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)
    header_frame_label =  Label(header_frame, text="All Shortlisted Resumes", bg="pink", fg='#e817bb',font=('comicsansms', 50, 'bold', 'underline'), pady=25)
    header_frame_label.pack()

    f =  Frame(root,bd = 8,relief = GROOVE)
    f.place(relx=0, rely=0.2,relwidth = 1,relheight = 0.8)

    links = ['https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.google.com','https://www.youtube.com','https://www.Mysir.com','https://www.google.com','https://www.tutorialspoint.com/','https://www.google.com']

    scrollbar = Scrollbar(f)

    text =  Text(f,font = ('comicsansms',10,'bold'),fg = 'darkblue',pady = 5,padx = 15,yscrollcommand=scrollbar.set,state = 'disabled')
    text.pack(fill="both", expand=True)
    text.bind("<Configure>", reset_tabs)
    j = 0
    for i,link in enumerate(All_Sort_Listed_Resumes):
        item = "{}".format(i)
        if j == 0:
            label1 =  Label(text, text=f'{link}\n', font=('Helvetica', 20, 'bold'),width = '55',cursor="hand2",fg = 'darkblue',bg='orange')
            label1.bind("<Button-1>",callback2)
            text.window_create('insert',window = label1)
            j = 1

        elif j == 1:
            global label2
            label2 = Label(text, text=f'{link}\n', font=('comicsansms', 20, 'bold'), width='52',cursor="hand2",fg = 'darkblue',bg='pink')

            label2.bind("<Button-1>",callback2)

            text.window_create('end-2c', window=label2,padx = 20,pady = 0,)
            j = 0
        # text.insert("end", item + "\t\n")
        button =  Button(text, text="Click To See Report" ,width = 25,bd = 8,height = 3,font=('comicsansms', 15, 'bold'),padx = 15,
                           cursor="left_ptr",
                            highlightthickness=0,
                           command = lambda text=item: callback(text,Word_matched))

        text.window_create("end-2c", window=button)
        # button.pack(side = tk.TOP,anchor = 'se')
    scrollbar.config(command=text.yview,bg = 'red')
    scrollbar.pack(side= RIGHT, fill= Y)
    text.pack(side='left')
    root.mainloop()







# All_Shortlisted_Resumes()
















# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# def callback3(event):
#     print(event)
#
#     event.widget.config(bg='light blue')
#     event.widget.focus_set()  # give keyboard focus to the label
#     event.widget.bind('<Key>', edit)
#     print(event.widget.cget("text"))
#
# def edit(event):
#     print(event.char)
#
# example = Label(frame, text='Click me')
#
# pre = 'fsdddddds'
# example.bind('<Button-1>', lambda x = pre : callback3(x))
# example.pack()
# mainloop()








# from tkinter import Tk, Label, StringVar
# import webbrowser
#
# root = Tk()
#
# list1 = ["site1-google", "site2-facebook"]
# list2 = ["google.com", "fb.com"]
#
# for v1, v2 in zip(list1, list2):
#     item_values = '{}'.format(v1)
#     sv = StringVar()
#     lbl = Label(root, width="100", height="2", textvariable=sv)
#
#     lbl.bind("<Button-1>", lambda e: callback(v2))
#     lbl.pack()
#     sv.set(item_values)
#
#
#     def callback(url):
#
#         webbrowser.open_new(url)
#
# root.mainloop()




# from tkinter import *
# import webbrowser
#
# # def callback1(url):
# #     webbrowser.open_new(url)
#
# def callback1(event):
#     print(event.widget.cget('text'))
#     webbrowser.open_new(event.widget.cget('text'))
#
# root = Tk()
# link1 = Label(root, text="http://www.google.com", fg="blue", cursor="hand2")
# link1.pack()
# link1.bind("<Button-1>",callback1)
#
# link2 = Label(root, text="http://www.ecosia.org", fg="blue", cursor="hand2")
# link2.pack()
# link2.bind("<Button-1>",callback1)
#
# root.mainloop()






























# import webbrowser
# import tkinter as tk
# from tkinter import Scrollbar
#
# def reset_tabs(event):
#     '''Add a tabstop at the right edge of the widget'''
#     right_margin = event.width - 8
#     if right_margin <= 0: return
#     tabs = (right_margin, "right")
#     event.widget.configure(tabs=tabs)
#
# def callback(text):
#     print("you clicked {}".format(text))
#
#
# def callback2(url):
#     webbrowser.open_new(url)
#
# root = tk.Tk()
#
# root.geometry('700x600')
# f = tk.Frame(root,bd = 8,relief =tk.GROOVE)
# f.place(relx=0.2, rely=0.2,relwidth = 0.7,relheight = 0.6)
#
# links = ['https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.tutorialspoint.com/','https://www.google.com','https://www.youtube.com','https://www.Mysir.com','https://www.google.com','https://www.tutorialspoint.com/']
#
# scrollbar = Scrollbar(f)
#
# text = tk.Text(f,font = ('comicsansms',10,'bold' ),fg = 'darkblue',pady = 5,padx = 15,yscrollcommand=scrollbar.set)
# text.pack(fill="both", expand=True)
# text.bind("<Configure>", reset_tabs)
# j = 0
# for i,link in enumerate(links):
#     item = "this is item {}".format(i+1)
#     if j == 0:
#         label1 = tk.Label(text, text=f'{link}\n', font=('comicsansms', 20, 'bold'),width = '35',cursor="hand2",fg = 'darkblue',
#                            bg='orange')
#         label1.bind("<Button-1>", lambda e: callback2(f"{link}"))
#         text.window_create('insert',window = label1)
#         j = 1
#     elif j == 1:
#         label2 = tk.Label(text, text=f'{link}\n', font=('comicsansms', 20, 'bold'), width='35',cursor="hand2",fg = 'darkblue',
#                          bg='pink')
#         label2.bind("<Button-1>", lambda e: callback2(f'{link}'))
#         text.window_create('end-2c', window=label2,padx = 20,pady = 0,)
#         j = 0
#     # text.insert("end", item + "\t\n")
#     button = tk.Button(text, text="Click To See Report" ,width = 25,bd = 8,height = 3,font=('comicsansms', 11, 'bold'),
#                        cursor="left_ptr",
#                         highlightthickness=0,
#                        command = lambda text=item: callback(text))
#     # button.place(relx = 0.2,rely = 0.4,relwidth = 0.4,relheight = 0.2)
#     # ne, e, se, s, sw, w, nw
#     # button.pack(side=tk.TOP, anchor='se')
#     text.window_create("end-2c", window=button)
#     # button.pack(side = tk.TOP,anchor = 'se')
# scrollbar.config(command=text.yview,bg = 'red')
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# text.pack(side='left')
# root.mainloop()