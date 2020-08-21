from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Affan Ch.")
win.geometry("500x400")



style = ttk.Style()


style.theme_use('clam')

print(style.element_options("arrowless.Vertical.TScrollbar.thumb"))

style.configure("arrowless.Vertical.TScrollbar", gripcount=0, background="#464647",troughcolor='#252526', borderwidth=0,
bordercolor='#252526', lightcolor='#252526', darkcolor='#252526')

#626263 #Pressed
#515151  #Mouse Over
#464647 Before

style.map('arrowless.Vertical.TScrollbar',
        foreground=[('disabled', '#464647'),('pressed', '#626263'),('active', '#515151')],
        background=[('disabled', '#464647'),('pressed', '!focus', '#626263'),('active', '#515151')],
        highlightcolor=[('focus', '#464647'),('!focus', '#464647')],
)

style.layout('arrowless.Vertical.TScrollbar',[('Vertical.Scrollbar.trough',
{'children': [('Vertical.Scrollbar.thumb',{'expand': '1', 'sticky': 'nswe'})],'sticky': 'ns'})])




main_frame = Frame(win, bg='#252526')
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame, bg='#252526', highlightbackground='#252526')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, style= 'arrowless.Vertical.TScrollbar', command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y) 

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor='nw')

for thing in range(100):
    Button(second_frame, text='Button', bg='#252526', fg='#cccccc', bd=0, width=20).grid(row=thing, column=0)


win.mainloop()