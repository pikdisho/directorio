from tkinter import *
  
root = Tk() 
  
root.geometry("400x400") 
  
bg = PhotoImage(file = "Proyecto\media\TEXTOPNGPRUEBA.png") 
  
canvas1 = Canvas( root, width = 400, 
                 height = 400) 
  
canvas1.pack(fill = "both", expand = True) 
  
canvas1.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
  
canvas1.create_text( 200, 250, text = "Welcome") 
  
button1 = Button( root, text = "Exit") 
button3 = Button( root, text = "Start") 
button2 = Button( root, text = "Reset") 
  
button1_canvas = canvas1.create_window( 100, 10,  
                                       anchor = "nw", 
                                       window = button1) 
  
button2_canvas = canvas1.create_window( 100, 40, 
                                       anchor = "nw", 
                                       window = button2) 
  
button3_canvas = canvas1.create_window( 100, 70, anchor = "nw", 
                                       window = button3) 
  
root.mainloop()