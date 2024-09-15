from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Times of India")
root.geometry("600x400")
def every_100(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="/n"
    return final_text
texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))
    image=Image.open(f"{i+1}.png")
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root,width=800,height=70)
Label(f0,text="Code with Harry News",font="lucida 33 bold").pack()
Label(f0,text="January 19 2025",font="lucida 18 bold").pack()
f0.pack()
f1=Frame(root,width=900,height=200)
Label(f1,text=texts[0],padx=22,pady=22).pack(side=LEFT)
Label(f1,image=photos[0],anchor="w").pack()
f1.pack(anchor="w")
root.mainloop()
