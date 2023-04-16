import face_recognition
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageDraw
win= Tk()

win.geometry("750x250")

def display_text():
   global entry
   global string
   string= entry.get()
   

   
label=Label(win, text="enter location of the first image", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)


win.mainloop()
win= Tk()

win.geometry("750x250")

def display_text():
   global entry
   global string_1
   string_1= entry.get()
   

   
label=Label(win, text="enter location of the second image", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)


win.mainloop()
image_1 = face_recognition.load_image_file(string)
image_2 = face_recognition.load_image_file(string_1)
image_1_loc = face_recognition.face_locations(image_1)
image_2_loc = face_recognition.face_locations(image_2)

for j in range(len(image_1_loc)):
 encoding_image_1 = face_recognition.face_encodings(image_1)[j]
 for i in range(len(image_2_loc)):
  encoding_image_2 = face_recognition.face_encodings(image_2)[i]
  results = face_recognition.compare_faces([encoding_image_1],encoding_image_2,tolerance=0.5)
  if results[0]:
    flag = 1
    break
  else:
    flag = 0
if flag == 1:
  a="Both the following faces are same"
else:
  a = "the faces are not same"
root = Tk()
frm = ttk.Frame(root, padding=50)
frm.grid()
ttk.Label(frm, text=a).grid(column=0, row=0)
root.mainloop()


top_1 = image_2_loc[i][0]
right_1 = image_2_loc[i][1]
bottom_1 = image_2_loc[i][2]
left_1 = image_2_loc[i][3]


top = image_1_loc[j][0]
right = image_1_loc[j][1]
bottom = image_1_loc[j][2]
left = image_1_loc[j][3]


image_1_pil = Image.fromarray(image_1)
image_2_pil = Image.fromarray(image_2)
draw = ImageDraw.Draw(image_1_pil)
draw.rectangle((left,top,right,bottom),outline=(250,7,0))
draw_1 = ImageDraw.Draw(image_2_pil)
draw_1.rectangle((left_1,top_1,right_1,bottom_1),outline=(250,7,0))
image_1_pil.show()
image_2_pil.show()
