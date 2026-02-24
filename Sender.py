import tkinter as tk
from tkinter import messagebox
import smtplib
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk, Image

class EmailSender:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Email Sender')
        self.root.geometry('400x300')
        self.root.maxsize(400,300)
        self.root.minsize(400,300)

        self.header = tk.Label(self.root,bg="orange",width=300,height=2)
        self.header.place(x=0,y=0)
        self.h1 = tk.Label(self.root,text="Email Sender",bg="orange",fg="black",font=('verdana',13,'bold'))
        self.h1.place(x=135,y=5)

        self.img = ImageTk.PhotoImage(Image.open('gmail.png'))
        self.logo = tk.Label(self.root,image=self.img,borderwidth=0)
        self.logo.place(x=150,y=38)

        self.e = tk.Label(self.root,text="Email Address",font=('verdana',10,'bold'))
        self.e.place(x=100,y=130)
        self.email = tk.Entry(self.root,width=30,relief=tk.RIDGE,borderwidth=3)
        self.email.place(x=100,y=150)

        self.p = tk.Label(self.root,text="Password",font=('verdana',10,'bold'))
        self.p.place(x=100,y=190)
        self.password = tk.Entry(self.root,width=30,relief=tk.RIDGE,borderwidth=3, show='*')
        self.password.place(x=100,y=210)

        self.login = tk.Button(self.root,text="Login",padx=30,bg="orange",relief=tk.RIDGE,borderwidth=1,font=('verdana',10,'bold'),cursor="hand2",command=self.Login)
        self.login.place(x=135,y=240)

    def Login(self):
        e = self.email.get()
        p = self.password.get()
        if '@gmail.com' not in e or e == "" :
            messagebox.showerror('Login error',"Please Write the Valid Email")
        elif p == "":
            messagebox.showerror('Login error'," Password Shouldn't be Empty")
        else:
            try:
                self.s = smtplib.SMTP('smtp.gmail.com', 587)
                self.s.starttls()
                self.s.login(e,p)
                messagebox.showinfo("Login Success","You have Logged to Gmail Successfully")
                self.root.destroy()
                self.main_window(e, p)
            except:
                messagebox.showerror('Login error',"Failed to Login, Either Your Email or Password is Wrong nor You did Enable less secure Apps in gmail Setting")

    def main_window(self, e2, p):
        self.root = tk.Tk()
        self.root.title('Email Sender')
        self.root.geometry('500x400')

        self.header1 = tk.Label(self.root,bg="orange",width=300,height=2)
        self.header1.place(x=0,y=0)
        self.h2 = tk.Label(self.root,text="Email Sender",bg="orange",fg="black",font=('verdana',13,'bold'))
        self.h2.place(x=175,y=5)

        self.logout = tk.Button(self.root,text="Logout",padx=20,bg="orange",relief=tk.RIDGE,borderwidth=1,font=('verdana',10,'bold'),cursor="hand2",command=self.Logout)
        self.logout.place(x=390,y=38)

        self.r = tk.Label(self.root,text="Recipient Email Address",font=('verdana',10,'bold'))
        self.r.place(x=130,y=130)
        self.recipient = tk.Entry(self.root,width=30,relief=tk.RIDGE,borderwidth=3)
        self.recipient.place(x=130,y=150)

        self.st = tk.Label(self.root,text="Subject",font=('verdana',10,'bold'))
        self.st.place(x=130,y=190)
        self.subject = tk.Entry(self.root,width=30,relief=tk.RIDGE,borderwidth=3)
        self.subject.place(x=130,y=210)

        self.m = tk.Label(self.root,text="Message",font=('verdana',10,'bold'))
        self.m.place(x=130,y=250)
        self.message = ScrolledText(self.root,width=40,height=5,relief=tk.RIDGE,borderwidth=3)
        self.message.place(x=130,y=270)

        self.send = tk.Button(self.root,text="Send",padx=30,relief=tk.RIDGE,borderwidth=1,bg="orange",font=('verdana',10,'bold'),cursor="hand2",command=lambda: self.Send(e, p))
        self.send.place(x=350,y=360)

        self.root.mainloop()

    def Logout(self):
        self.s.quit()
        self.root.destroy()

    def Send(self, e, p):
        r = self.recipient.get()
        st = self.subject.get()
        m = self.message.get('1.0',tk.END)
        if '@gmail.com' not in r or r == "":
            messagebox.showerror('Sending Mail error',"Please Write the Valid Email")
        elif m == "":
            messagebox.showerror('Sending Mail error',"Message shouldn't be Empty")
        else:
            try:
                self.s.sendmail(e,r,f'Subject :{st}\n\n {m}')
                messagebox.showinfo("Success","Your Message has been send successfully")
            except:
                messagebox.showerror('Sending Mail error',"Failed to Send Email")

if __name__ == "__main__":
    email_sender = EmailSender()
    email_sender.root.mainloop()
