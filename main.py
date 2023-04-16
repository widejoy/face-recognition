import face_recognition
from tkinter import *
from tkinter import ttk
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

for j in range(image_2_loc):
 encoding_image_1 = face_recognition.face_encodings(image_1)[j]
 for i in range(image_1_loc):
  encoding_image_2 = face_recognition.face_encodings(image_2)[i]
  results = face_recognition.compare_faces([encoding_image_1],encoding_image_2,tolerance=0.5)
  if results[0]:
    flag = 1
  else:
    flag = 0
if flag == 1:
  print("the faces are same")
else:
  print("the faces are not same")