import tkinter as tk
import os
from PIL import (
    ImageTk,
    Image
)
from auth import (
    login,
    User
)
from blocker import (
    unblock,
    block
)
from db import (
    read_data,
    push_bugs
)
from models import (
    write_details,
    check_status,
    get_current_user,
    change_status,
    write_details,
    write_session_details
)


def app_start():
    global status,current_user,session
    status,session=check_status()
    if status == True :
        user=get_current_user()
        current_user=User(user,True)


def login_handler():
    '''This function handles the authentication of a user'''
    app_start()
    if status:
        homepage()
    else :    

        def login_call():
            global status
            if nam_entry and pass_entry:
                logged_in,message=login(nam_entry,pass_entry)
                if logged_in:
                    app_start()
                    window.destroy()
                    homepage()
                else :
                    err_lbl=tk.Label(window,text=message)
                    err_lbl.pack(anchor="center",pady=(10,5))       
            else :
                print("fill the field")

        '''Setting up the window'''
        window=tk.Tk()
        window.configure(background="#23272A")
		#window.iconbitmap("./img/doughnut.ico")
        window.geometry("450x650")
        root_path=os.path.dirname(os.path.abspath(__file__))
        window.title("Login")
        window.resizable(False,False)
        '''Label'''
        login_lbl=tk.Label(window,text="Login",background="#23272A",foreground="#ffffff",font=("Sans serif", 40))
        name_lbl=tk.Label(window,text="Employee ID",background="#23272A",foreground="#ffffff",font=(25))
        pass_lbl=tk.Label(window,text="Passcode",background="#23272A",foreground="#ffffff",font=(25))
        '''entries'''
        nam_entry=tk.Entry(window,bd=1,width=38,font=(16))
        pass_entry=tk.Entry(window,bd=1,width=38,font=(16),show="*")
        '''image label'''
        img=Image.open(root_path+"//img//teacher_avatar.jpg")
        img=ImageTk.PhotoImage(img)
        img_label=tk.Label(window,image=img)
        '''button'''
        sub_buttn=tk.Button(window,text="Submit",command=login_call)
        '''positioning of label'''
        login_lbl.pack(anchor="center",pady=15,padx=10)
        img_label.pack(anchor="center",pady=10)
        name_lbl.pack(anchor="nw",padx=(60,10),pady=(20,5))
        nam_entry.pack(anchor="nw",padx=(60,10))
        pass_lbl.pack(anchor="nw",padx=(60,10),pady=(20,5))
        pass_entry.pack(anchor="nw",padx=(60,10))
        sub_buttn.pack(anchor="center",pady=15,padx=10)

        window.mainloop()


def homepage():
    '''Landing Page Of The App Afer The Login'''
    if status:
        def redirect_logout():
            window.destroy()
            logout()

        def redirect_session():
            logout_btn.pack_forget()
            session_btn.pack_forget()
            for bug_btns in bugOperations:
                bug_btns.pack(anchor="center",pady=(25,20))
            start_session() 

        def open_my_bugs():
            window.destroy()
            bugView(my_bug=True)
        
        def open_all_bugs():
            window.destroy()
            bugView(all_bug=True)

        def add_new_bugs():
            window.destroy()
            bugView(add_bug=True)

        '''window'''
        window=tk.Tk()
        window.geometry("1200x780+450+126")        
        window.title("Home | AllSafe")
		#window.iconbitmap("./img/doughnut.ico")
        window.resizable(False,False)
        '''Image'''
        img=Image.open("./img/sarthak.jpg")
        IMG=img.resize((300,300),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(IMG)
        '''Two Frames Set Up'''
        sidebar=tk.Frame(window,bg="#2C2F33",width=250,height=780)
        sidebar.pack(anchor="nw",side="left",fill="both",expand=True)
        main=tk.Frame(window,bg="#23272A",width=950,height=780)
        main.pack(anchor="ne",side="right",fill="both",expand=True)
        sidebar.pack_propagate(0)
        main.pack_propagate(0)
        '''Label'''
        welcome_lbl=tk.Label(main,text=f"Welcome, {current_user.name}",fg="white",bg="#23272A",font=("Sans Serif",33))
        welcome_lbl.pack(anchor="center",pady=(25,0),padx=(0,15))
        img_label=tk.Label(main,image=img)
        name_lbl=tk.Label(main,text=f"Name : {current_user.name}",fg="white",bg="#23272A",font=("bold italic",18))
        code_lbl=tk.Label(main,text=f"Code : #{current_user.code}",fg="white",bg="#23272A",font=("bold italic",18))
        dept_lbl=tk.Label(main,text=f"Department : {current_user.dept.title()}",fg="white",bg="#23272A",font=("bold italic",18))
        img_label.pack(anchor="center",pady=(30,0),padx=(0,15))
        name_lbl.pack(anchor="center",pady=(20,0),padx=(0,15))
        code_lbl.pack(anchor="center",pady=(10,0),padx=(0,15))
        dept_lbl.pack(anchor="center",pady=(10,0),padx=(0,15))
        '''Buttons'''
        mybug_btn = tk.Button(sidebar,text="Your Bugs",bg="#2C2F33",fg="#ffffff",bd=1,font=(6),cursor="hand2",command=open_my_bugs)
        allbug_btn = tk.Button(sidebar,text="All Bugs",bg="#2C2F33",fg="#ffffff",bd=1,font=(6),cursor="hand2",command=open_all_bugs)
        addbug_btn = tk.Button(sidebar,text="Add A Bug",bg="#2C2F33",fg="#ffffff",bd=1,font=(6),cursor="hand2",command=add_new_bugs)
        bugOperations = [mybug_btn,allbug_btn,addbug_btn]
 
        
        if not session:
            session_btn=tk.Button(sidebar,text="Start Session",bg="#2C2F33",fg="#ffffff",bd=1,font=(6),cursor="hand2",command=redirect_session)
            session_btn.pack(anchor="center",pady=(40,20)) 
            logout_btn=tk.Button(sidebar,text="Logout",bg="#2C2F33",fg="#ffffff",bd=1,font=(6),cursor="hand2",command=redirect_logout)
            logout_btn.pack(anchor="center",pady=(30,20))
        else :
            for bug_btns in bugOperations:
                bug_btns.pack(anchor="center",pady=(25,20))

        window.mainloop()

def start_session():
    '''This function will start the session when start session button is clicked'''
    if status:
        global session
        '''Changing the status in the file and the program'''
        change_status([True,True])  
        session=True
        '''Blocking the required sites and Starting the Session'''
        block()
        data=write_session_details(start=True)
        '''Creating the closing protocol'''
        def closeWindow():
            global session
            window.destroy()
            print("Window closing")
            unblock()
            write_session_details(end=True)
            change_status([True,False])
            session=False

        ''' Creating the window'''
        window=tk.Tk()
        window.geometry("500x220")        
        window.title("Session | AllSafe ")
        window.configure(background="#2C2F33")
		#window.iconbitmap("./img/doughnut.ico")
        window.protocol("WM_DELETE_WINDOW",closeWindow)
        window.resizable(False,False)

        name_lbl=tk.Label(window,text=f"{current_user.name}",fg="#ffffff",bg="#2C2F33",font=('bold italic',25))
        session_lbl=tk.Label(window,text=f"Session Started At - {data['session_start'][0]} hours {data['session_start'][1]} minutes",fg="#ffffff",bg="#2C2F33")
        hour_lbl=tk.Label(window,text=f"Hours worked Weekly - {data['weekly_hour']}",fg="#ffffff",bg="#2C2F33")
        name_lbl.pack(anchor="center",pady=(10,20))
        session_lbl.pack(anchor="center",pady=(0,20))
        hour_lbl.pack(anchor="center",pady=(0,20))
        window.mainloop()

    else :
        raise ValueError("Cuurent Status is not logged in")    

def bugView(**kwargs):
    '''Display bugs to the employee and allows to add more bugs'''
    global session
    if session:
        mybug_query = f"SELECT content,raised_by FROM bugs WHERE raised_by='{current_user.code}';"
        allbug_query=f"SELECT content,raised_by FROM bugs;"
        '''Creating The Window'''
        window=tk.Tk()
        scrollbar = tk.Scrollbar(window) 
        window.geometry("1050x780+450+126")        
        window.title("Bugs | AllSafe ")
        window.configure(background="#2C2F33")
        window.iconbitmap("./img/doughnut.ico")
        window.resizable(False,False)
        scrollbar.pack(fill='y',side="right")

        if kwargs.get("my_bug",False) == True:
            bugs = read_data(mybug_query) 
        elif kwargs.get("all_bug",False) == True:
            bugs = read_data(allbug_query)

        def redirect_homepage():
            window.destroy()
            homepage()

        def redirect_push_bug():
            bug = bug_entry.get("1.0",'end-1c')
            if bug :
                print(bug)
                window.destroy()
                push_bugs(bug=bug,user_code=current_user.code)
                homepage()


        if kwargs.get("my_bug",False) or kwargs.get("all_bug",False):
            lbl=tk.Label(window,text="Your Bugs To Fix",fg="#ffffff",bg="#2C2F33",font=('bold italic',30))
            home_btn = tk.Button(window,text="Home",bg="#2C2F33",fg="#ffffff",bd=0.1,font=(6),cursor="hand2",command=redirect_homepage)
            lbl.pack(anchor="center",pady=(30,20))
            home_btn.pack(anchor="center",pady=(10,20))
            if bugs:
                for bug in bugs:
                    bug_frame=tk.Frame(window,bg="#23272A",width=900,height=100)
                    bug_frame.pack(anchor="center",pady=(20,0),fill="both")
                    text_bug = tk.Label(bug_frame,text=bug[0],fg="#ffffff",bg="#23272A",font=('bold',15),wraplength=900)
                    raiser_bug = tk.Label(bug_frame,text=f"Raised By-{bug[1]}",fg="#ffffff",bg="#23272A",font=('italic',12))
                    text_bug.pack(anchor="nw",pady=(15,15),padx=(20,0))
                    raiser_bug.pack(anchor="center",pady=(15,5))
            else :
                nobug_lbl = tk.Label(window,text="No Bugs To Solve",fg="#ffffff",bg="#2C2F33",font=('bold italic',20))
                nobug_lbl.pack(anchor="center",pady=(30,30))    
        elif kwargs.get("add_bug",False):
            lbl=tk.Label(window,text="Raise A Bug For Other Employees",fg="#ffffff",bg="#2C2F33",font=('bold italic',30))
            home_btn = tk.Button(window,text="Home",bg="#2C2F33",fg="#ffffff",bd=0.1,font=(6),cursor="hand2",command=redirect_homepage)
            lbl.pack(anchor="center",pady=(30,20))
            home_btn.pack(anchor="center",pady=(10,20))
            bug_entry = tk.Text(window,bd=1,font=(20))
            bug_entry.place(width=700,height=100)
            bug_entry.pack(anchor="center",pady=(30,0))
            push_btn = tk.Button(window,text="Push My Bug",bg="#2C2F33",fg="#ffffff",bd=1,font=(12),cursor="hand2",command=redirect_push_bug)
            push_btn.pack(anchor="center",pady=(30,0))
                

        window.mainloop()        



def logout():
    '''Handles the logout of a particular employee'''
    if status:
        change_status([False,False])
        write_session_details(reset=True)

if __name__=="__main__":
    login_handler()

