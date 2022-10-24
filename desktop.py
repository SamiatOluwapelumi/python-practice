import tkinter as tk
# create a window 
window=tk.Tk()  
# give window a title
window.title('Desktop App')
# define d geometry of d app(width and height)
window.geometry('600x400')
# print something on the window,we can add a text by using the label() method and pass d string to a parameter called text
newlabel=tk.Label(text='visit my website to improve your python skill')
# placing on a grid
newlabel.grid(column=0,row=0)
window.mainloop()