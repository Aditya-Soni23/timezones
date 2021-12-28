
from tkinter import*
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("600x900")
im_image = ImageTk.PhotoImage(Image.open("imap.jpg"))
um_image = ImageTk.PhotoImage(Image.open("umap.jpg"))
am_image = ImageTk.PhotoImage(Image.open("amap.jpg"))
jm_image = ImageTk.PhotoImage(Image.open("jmap.jpg"))


india_label = Label(root,text = "India")
india_label.place(relx = 0.2, rely = 0.01, anchor = CENTER)

india_im = Label(root)
india_im["image"]=im_image
india_im.place(relx = 0.2,rely = 0.23, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely= 0.46, anchor = CENTER)

usa_label = Label(root,text = "USA")
usa_label.place(relx = 0.7, rely = 0.01, anchor = CENTER)

usa_um = Label(root)
usa_um["image"]=um_image
usa_um.place(relx = 0.7, rely = 0.13, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.7, rely = 0.26, anchor = CENTER)

australia_label = Label(root,text = "Australia")
australia_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)

australia_am = Label(root)
australia_am["image"]=am_image
australia_am.place(relx = 0.2,rely = 0.70, anchor = CENTER)

australia_time = Label(root)
australia_time.place(relx = 0.2, rely= 0.85, anchor = CENTER)

japan_label = Label(root,text = "Japan")
japan_label.place(relx = 0.7, rely = 0.45, anchor = CENTER)

japan_jm = Label(root)
japan_jm["image"]=jm_image
japan_jm.place(relx = 0.7,rely = 0.65, anchor = CENTER)

japan_time = Label(root)
japan_time.place(relx = 0.7, rely= 0.85, anchor = CENTER)





class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S:")
        india_time["text"]="Time :"+ current_time
        india_time.after(200,self.times)
        
        
class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S:")
        usa_time["text"]="Time :"+ current_time
        usa_time.after(200,self.times)
        
class Australia():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S:")
        australia_time["text"]="Time :"+ current_time
        australia_time.after(200,self.times)
        
        
class Japan():
    def times(self):
        home = pytz.timezone('Asia/Tokyo')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S:")
        japan_time["text"]="Time :"+ current_time
        japan_time.after(200,self.times)
        
        
        
        
obj_india=India()
obj_usa=USA()
obj_australia=Australia()
obj_japan=Japan()
india_btn = Button(root,text="Show Time", command=obj_india.times)
india_btn.place(relx = 0.2, rely =0.50 , anchor = CENTER)
usa_btn = Button(root,text="Show Time", command=obj_usa.times)
usa_btn.place(relx = 0.7, rely = 0.30, anchor=CENTER)
australia_btn = Button(root,text="Show Time", command=obj_australia.times)
australia_btn.place(relx = 0.2, rely =0.90 , anchor = CENTER)
japan_btn = Button(root,text="Show Time", command=obj_japan.times)
japan_btn.place(relx = 0.7, rely = 0.90, anchor=CENTER)

root.mainloop()
