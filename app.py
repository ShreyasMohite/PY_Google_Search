from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from googlesearch import search 
import threading

class Googles:
    def __init__(self,root):
        self.root=root
        self.root.title("Google Search")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo66.ico")
        self.root.resizable(0,0)

        search_re=StringVar()
        num_result=IntVar()


#=================================================================================#

        def clear():
            search_re.set("")
            num_result.set(1)
            text.delete("1.0","end")

        def searchs():
            try:
                with open("C:/TEMP/results.txt","w") as f:

                    if search_re.get()!="":                  
                        for j in search(search_re.get(), tld="co.in", num=num_result.get(), stop=num_result.get(), pause=2): 
                            f.write(j+"\n\n")
     
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter Query for search")
                with open("C:/TEMP/results.txt","r") as f:
                    text.insert("end",f.read())

                
            except Exception as e:
                tkinter.messagebox.showerror("Error","No Internet Connection")

        def thread_search():
            t1=threading.Thread(target=searchs)
            t1.start()
                

#==================================================================================#
        def on_enter1(e):
            but_search['background']="black"
            but_search['foreground']="cyan"
  
        def on_leave1(e):
            but_search['background']="SystemButtonFace"
            but_search['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

#==================================================================================#
        mainframe=Frame(self.root,width=500,height=400,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,bd=3,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=243,bd=3,relief="ridge")
        secondframe.place(x=0,y=150)

#================================firstframe===================================================#

        lab_frame=LabelFrame(firstframe,width=488,height=145,text="Google Search",bg="#89b0ae",fg="white")
        lab_frame.place(x=0,y=0)
#==============================================================================================#

        lab=Label(lab_frame,text="Search",font=('times new roman',12),bg="#89b0ae")
        lab.place(x=0,y=5)

        ent_search=Entry(lab_frame,width=47,font=('times new roman',12),bd=3,relief="ridge",textvariable=search_re)
        ent_search.place(x=70,y=5)

        lab_results=Label(lab_frame,text="Number of Searchs Results:",font=('times new roman',12),bg="#89b0ae")
        lab_results.place(x=0,y=50)

        but_search=Button(lab_frame,width=13,text="Search",font=('times new roman',12),cursor="hand2",command=thread_search)
        but_search.place(x=50,y=90)
        but_search.bind("<Enter>",on_enter1)
        but_search.bind("<Leave>",on_leave1)

        fileselect=list(range(1,21))
        fileselect_combo=Combobox(firstframe,values=fileselect,font=('arial',12),width=20,state="readonly",textvariable=num_result)
        fileselect_combo.set(1)
        fileselect_combo.place(x=200,y=60)

        but_clear=Button(lab_frame,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=300,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=============================================================================================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)



if __name__ == "__main__":
    root=Tk()
    app=Googles(root)
    root.mainloop()


    