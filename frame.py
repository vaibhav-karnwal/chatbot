from tkinter import *

root=Tk()
root.title('V-Bot')
root.geometry('370x415')
root.minsize(370,416)

main_menu=Menu(root)

file_menu=Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save as..')
file_menu.add_command(label='Exit..')

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

def send():
    send="You :"+e.get()
    txt.insert(END,"\n"+send)
    
    
    
txt=Text(root,background="grey",foreground="white")
txt.grid(row=0,column=0,columnspan=50)
e=Entry(root,width=45,border=4)
send=Button(root,bg='gray',width=10,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)


root.mainloop()






