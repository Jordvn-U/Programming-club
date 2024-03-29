import time
from tkinter import *
from tkinter import messagebox 
import sqlite3
from tkinter import ttk 
##############################################

############################    setup      ##################

##########################################################3
root= Tk() 
root.geometry('700x700') 
root.title("Pomadoro Timer!")
root.configure(bg='salmon')
myLabel=Label(root, text="Welcome to Pomadoro Timer")
myLabel.pack()



#original sample data
# #sample = [
#     ["Algebra Quiz", "2023-01-08", "High", "Study for quiz","Completed"],
#     ["History Research", "2023-01-15", "Low", "Research and summarize","Not Completed"],
#     
# ]

###########################################################

###############        timerboxes    ######################

##########################################################
mins=StringVar(value='00')
seconds=StringVar(value='00')
minuteTextbox = Entry(root,width=2, font=("Calibri", 50, ""), textvariable=mins) #height set by text size!

minuteTextbox.place(x=250, y=50)
secondTextbox = Entry(root, width=2, font=("Calibri", 50, ""), textvariable= seconds)
secondTextbox.place(x=370, y=50)
minLabel=Label(root, text="Minutes")
minLabel.place(x=260,y=150)
secLabel=Label(root, text="Seconds")
secLabel.place(x=380,y=150)
#############################################################

##################   timer functions ###########################

######################################################################
def studyTimer():
    
    myTimer=25*60
   
    while(myTimer>-1):
        newmins ,newsecs= divmod(myTimer,60)
        mins.set("{0:2d}".format(newmins))
        seconds.set("{0:2d}".format(newsecs))
        root.update()
        time.sleep(1)
        if(myTimer==0):
            messegebox.showinfo('','Your 25 minute study is over, take a break :)')
        myTimer-=1


def tenTimer():
    myTimer=10*60

    while(myTimer>-1):
        newmins ,newsecs= divmod(myTimer,60)
        mins.set("{0:2d}".format(newmins))
        seconds.set("{0:2d}".format(newsecs))
        root.update()
        time.sleep(1)
        if(myTimer==0):
            messegebox.showinfo('','Your 10 minute break is over, Resume study')
        myTimer-=1


def fiveTimer():

    myTimer=5*60


    while(myTimer>-1):
        newmins ,newsecs= divmod(myTimer,60)
        mins.set("{0:2d}".format(newmins))
        seconds.set("{0:2d}".format(newsecs))
        root.update()
        time.sleep(1)
        if(myTimer==0):
            messegebox.showinfo('','Your 5 minute break is over, Resume study')
        myTimer-=1

def reset():
    myTimer=0
   
    while(myTimer>-1):
        newmins ,newsecs= divmod(myTimer,60)
        mins.set("00")
        seconds.set("00")
        root.update()

#############################################################

##################  #To Do list Database###########################

######################################################################


#conn= sqlite3.connect('todo_list.db')

#c=conn.cursor()  #conncects to data base, grabs data, bring back


# conn.commit()

# conn.close()



#
#creates database
conn= sqlite3.connect('todo_list.db')
#cursor
c=conn.cursor()  #conncects to data base, grabs data, bring back
 #table creation

c.execute("""CREATE TABLE if not exists todolist (task_name TEXT,          
           deadline TEXT,
           priority TEXT,
           notes TEXT,
          status TEXT)

""")







conn.commit()

conn.close()
def query_database():
    conn= sqlite3.connect('todo_list.db')
#cursor
    c=conn.cursor()
    c.execute("SELECT * FROM todolist ")
    listarray=c.fetchall()


    for stuff in listarray:
        tree.insert(parent='',index='end',text='',values=(stuff[0],stuff[1],stuff[2],stuff[3],stuff[4]),tag=('evenrow',))

    conn.commit()

    conn.close()
###################################

##############Treeview##################

####################################
style=ttk.Style()
style.theme_use('default')

tree_frame= Frame(root)
tree_frame.pack(pady=200)


tree_scroll =Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

tree=ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set,selectmode='extended')
tree.pack()

tree_scroll.config(command=tree.yview)
tree['columns']=('Task Name','Deadline','Priority','Notes','Status')
#format each column individually 
tree.column('#0',width=0,stretch=NO)
tree.column("Task Name", anchor=W,width=140)
tree.column("Deadline", anchor=W,width=140)
tree.column("Priority", anchor=W,width=90)
tree.column("Notes", anchor=W,width=140)
tree.column("Status", anchor=W,width=140)


#adding headings
tree.heading('#0',text='',anchor=W)
tree.heading("Task Name",text='Task Name',anchor=W)

tree.heading("Deadline",text='Deadline',anchor=W)

tree.heading("Priority",text='Priority',anchor=W)

tree.heading("Notes",text='Notes',anchor=W)
tree.heading("Status",text='Status',anchor=W)




    

#################################################

###############Enter task formating################

####################################################
df=LabelFrame(root,text='Assignment')
df.place(x=115,y=450)

tn_label= Label(df,text='Task Name')
tn_label.grid(row=0,column=0,padx=10,pady=10)
tn_entry=Entry(df)
tn_entry.grid(row=0,column=1,padx=10,pady=10)

dead_label= Label(df,text='Deadline')
dead_label.grid(row=0,column=2,padx=10,pady=10)
dead_entry=Entry(df)
dead_entry.grid(row=0,column=3,padx=10,pady=10)

prio_label= Label(df,text='Priority')
prio_label.grid(row=1,column=0,padx=10,pady=10)
selected_value = StringVar()
selected_value.set("Low")

prio_entry=OptionMenu(df, selected_value, "High", "Moderate", "Low")

prio_entry.grid(row=1,column=1,padx=10,pady=10)

notes_label= Label(df,text='Notes')
notes_label.grid(row=1,column=2,padx=10,pady=10)
notes_entry=Entry(df)
notes_entry.grid(row=1,column=3,padx=10,pady=10)

butselect =StringVar(value="Not Completed")


notbut = Radiobutton(df, text="Not Completed", variable=butselect, value="Not Completed")
compbut = Radiobutton(df, text="Completed", variable=butselect, value="Completed")

notbut.grid(row=2,column=1,padx=10,pady=10)
compbut.grid(row=2,column=2,padx=10,pady=10)


############################################################3

####todo list functions and data base munipulation##############

################################################################
def fetch():
    conn= sqlite3.connect('todo_list.db')

    c=conn.cursor()  #conncects to data base, grabs data, bring back

    c.execute("SELECT * FROM todolist ")
    rows=c.fetchall()
    return rows
    #conn.commit()

    #conn.close()

    
def load_student_data():
    for row in tree.get_children():
        tree.delete(row)
    for row in fetch():
        t=row[0] 
        d=row[1]
        p=row[2]
        n=row[3]  
        s=row[4]
        tree.insert("",'end',text=t,values=(t,d,p,n,s))
        tree.tag_configure('evenrow',background='lightgrey')


        

def clear_form():
    tn_entry.delete(0,END)
    dead_entry.delete(0,END)
    notes_entry.delete(0,END)
    selected_value.set("Low")

    prio_entry=OptionMenu(df, selected_value, "High", "Moderate", "Low")
    notbut.select()
    compbut.deselect()


def select(c):
    tn_entry.delete(0,END)
    dead_entry.delete(0,END)
    notes_entry.delete(0,END)

    highlighted=tree.focus()
    values=tree.item(highlighted,'values')

    tn_entry.insert(0,values[0])
    dead_entry.insert(0,values[1])
    notes_entry.insert(0,values[3])
    selected_value.set(values[2])
    prio_entry=OptionMenu(df, selected_value, "High", "Moderate", "Low")
    if values[4]=='Completed':
        notbut.deselect()
        compbut.select()
    elif values[4]=='Not Completed':
        compbut.deselect()

        notbut.select()


def moveselected():
    move=tree.selection()   #grabs rows that were selected by user
    for row in move:                   #for that row slected by move      
        tree.move(move, tree.parent(move),tree.index(move)-1)  #grab index move, parent is parent of the item in the database tree
                                                #subtracting 1 moves up ?
def remove():
    tree.delete(tree.selection())
    conn= sqlite3.connect('todo_list.db')

    c=conn.cursor()  #conncects to data base, grabs data, bring back
    c.execute("DELETE FROM todolist WHERE task_name=?",(tn_entry.get(),))



    conn.commit()

    conn.close()
    load_student_data()

    clear_form()



def updateit():
    highlight=tree.focus()
    tree.item(highlight,text='',values=(tn_entry.get(),dead_entry.get(),selected_value.get(),notes_entry.get(),butselect.get()))    

    conn= sqlite3.connect('todo_list.db')

    c=conn.cursor()  #conncects to data base, grabs data, bring back
    c.execute("""UPDATE todolist SET
              task_name=:tn,
              deadline=:dl,
              priority=:p,
              notes=:n,
              status=:s
               WHERE task_name = :tn""",
               {
               'tn':tn_entry.get(),
               'dl': dead_entry.get(),
               'p':selected_value.get(),
               'n':notes_entry.get(),
               's':butselect.get(),
               })

    conn.commit()

    conn.close()



def add():
    conn= sqlite3.connect('todo_list.db')

    c=conn.cursor()  #conncects to data base, grabs data, bring back
    c.execute("INSERT INTO todolist VALUES (:task,:deadline,:prio,:notes,:stat)",    {
                'task':tn_entry.get(),
                'deadline': dead_entry.get(),
                'prio':selected_value.get(),
                'notes':notes_entry.get(),
                'stat':butselect.get(),
                }) 


    conn.commit()

    conn.close()
    clear_form()
    tree.delete(*tree.get_children())
    #load_student_data()
    query_database()





###################################################################

#########################Time buttons#########################\

#####################################################################
studystart=Button(root,text='Study ',command=studyTimer)
studystart.place(x=500,y=50)
fivestart=Button(root,text='5 minute break',command=fiveTimer)
fivestart.place(x=500,y=80)
tenstart=Button(root,text='10 minute break',command=tenTimer)
tenstart.place(x=500,y=110)
resett=Button(root,text='Reset',command=reset)
resett.place(x=500,y=140)

####buttons for task stuff
add=Button(root,text='add task',command=add)
add.place(x=130,y=620)
update=Button(root,text='update task',command=updateit)
update.place(x=220,y=620)
removebut=Button(root,text='delete task',command=remove)
removebut.place(x=320,y=620)
moveup=Button(root,text='move up task',command=moveselected)
moveup.place(x=420,y=620)
Select=Button(root,text='Clear',command=clear_form)
Select.place(x=550,y=620)

######SELECTA ND DISPLAY
tree.bind("<ButtonRelease-1>",select)

query_database()
root.mainloop() #CLoses menu canvas to display
