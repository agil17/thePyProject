import tkinter as tk

from PIL import Image
from PIL import ImageTk


def packNext0():
    l_list[0].pack_forget()
    next0.pack_forget()
    
    l_list[1].pack()
    
    
    next1.pack(side = tk.RIGHT)
    prev1.pack(side = tk.LEFT)
    

def packNext1():
    l_list[1].pack_forget()
    next1.pack_forget()
    prev1.pack_forget()
    
   
    l_list[2].pack()


    next2.pack(side = tk.RIGHT)
    prev2.pack(side = tk.LEFT)

def packNext2():
    l_list[2].pack_forget()
    next2.pack_forget()
    prev2.pack_forget()
   
    l_list[3].pack()


    next3.pack(side = tk.RIGHT)
    prev3.pack(side = tk.LEFT)

def packNext3():
    l_list[3].pack_forget()
    next3.pack_forget()
    prev3.pack_forget()
   
    l_list[4].pack()


    next4.pack(side = tk.RIGHT)
    prev4.pack(side = tk.LEFT)

def packNext4():
    l_list[4].pack_forget()
    next4.pack_forget()
    prev4.pack_forget()
    
    l_list[5].pack()

    next5.pack(side = tk.RIGHT)
    prev5.pack(side = tk.LEFT)
    
def packNext5():
    l_list[5].pack_forget()
    next5.pack_forget()
    prev5.pack_forget()
    
    l_list[6].pack()


    next6.pack(side = tk.RIGHT)
    prev6.pack(side = tk.LEFT)

def packNext6():
    l_list[6].pack_forget()
    next6.pack_forget()
    prev6.pack_forget()
    
    l_list[7].pack()

    next7.pack(side = tk.RIGHT)
    prev7.pack(side = tk.LEFT)

def packNext7():
    l_list[7].pack_forget()
    next7.pack_forget()
    prev7.pack_forget()
    
    l_list[8].pack()

    next8.pack(side = tk.RIGHT)
    prev8.pack(side = tk.LEFT)

def packNext8():
    l_list[8].pack_forget()
    next8.pack_forget()
    prev8.pack_forget()
    
    l_list[9].pack()

    next9.pack(side = tk.RIGHT)
    prev9.pack(side = tk.LEFT)

def packNext9():
    l_list[9].pack_forget()
    next9.pack_forget()
    prev9.pack_forget()
    
    l_list[10].pack()
    prev10.pack()

def packPrev1():
    l_list[1].pack_forget()
    next1.pack_forget()
    prev1.pack_forget()

    l_list[0].pack()
    next0.pack()

def packPrev2():
    l_list[2].pack_forget()
    next2.pack_forget()
    prev2.pack_forget()

    l_list[1].pack()
    next1.pack(side=tk.RIGHT)
    prev1.pack(side=tk.LEFT)

def packPrev3():
    l_list[3].pack_forget()
    next3.pack_forget()
    prev3.pack_forget()

    l_list[2].pack()
    next2.pack(side=tk.RIGHT)
    prev2.pack(side=tk.LEFT)

def packPrev4():
    l_list[4].pack_forget()
    next4.pack_forget()
    prev4.pack_forget()

    l_list[3].pack()
    next3.pack(side=tk.RIGHT)
    prev3.pack(side=tk.LEFT)

def packPrev5():
    l_list[5].pack_forget()
    next5.pack_forget()
    prev5.pack_forget()

    l_list[4].pack()
    next4.pack(side=tk.RIGHT)
    prev4.pack(side=tk.LEFT)


def packPrev6():
    l_list[6].pack_forget()
    next6.pack_forget()
    prev6.pack_forget()

    l_list[5].pack()
    next5.pack(side=tk.RIGHT)
    prev5.pack(side=tk.LEFT)

def packPrev7():
    l_list[7].pack_forget()
    next7.pack_forget()
    prev7.pack_forget()

    l_list[6].pack()
    next6.pack(side=tk.RIGHT)
    prev6.pack(side=tk.LEFT)

def packPrev8():
    l_list[8].pack_forget()
    next8.pack_forget()
    prev8.pack_forget()

    l_list[7].pack()
    next7.pack(side=tk.RIGHT)
    prev7.pack(side=tk.LEFT)

def packPrev9():
    l_list[9].pack_forget()
    next9.pack_forget()
    prev9.pack_forget()

    l_list[8].pack()
    next8.pack(side=tk.RIGHT)
    prev8.pack(side=tk.LEFT)

def packPrev10():
    l_list[10].pack_forget()
    
    prev10.pack_forget()

    l_list[9].pack()
    next9.pack(side=tk.RIGHT)
    prev9.pack(side=tk.LEFT)


root = tk.Tk()

import glob
img_list1 = []
img_list2 = []
f_list = []
l_list = []



img = ['1.png', '2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png','10.png','11.png']

for filename in img:
    im = Image.open(filename)
    img_list1.append(im)

#for filename in glob.glob('*.png'): #assuming gif
   # im=Image.open(filename)
    #img_list1.append(im)

#width, height = img_list1[0].size
#width = int(round(width)/4)
#height = int(round(height)/4)



for im in img_list1:
    width, height = im.size
    width = int(round(width)/7)
    height = int(round(height)/7)
    img = im.resize((width, height), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img)
    img_list2.append(img1)

    

for i in range(len(img_list2)):
    l_list.append(tk.Label(root, image = img_list2[i]))

l_list[0].pack()


next0 = tk.Button(root, text="Next", command=lambda: packNext0())
next1 = tk.Button(root, text="Next", command=lambda: packNext1())
next2 = tk.Button(root, text="Next", command=lambda: packNext2())
next3 = tk.Button(root, text="Next", command=lambda: packNext3())
next4 = tk.Button(root, text="Next", command=lambda: packNext4())
next5 = tk.Button(root, text="Next", command=lambda: packNext5())
next6 = tk.Button(root, text="Next", command=lambda: packNext6())
next7 = tk.Button(root, text="Next", command=lambda: packNext7())
next8 = tk.Button(root, text="Next", command=lambda: packNext8())
next9 = tk.Button(root, text="Next", command=lambda: packNext9())

prev1 = tk.Button(root, text="Prev", command=lambda: packPrev1())
prev2 = tk.Button(root, text="Prev", command=lambda: packPrev2())
prev3 = tk.Button(root, text="Prev", command=lambda: packPrev3())
prev4 = tk.Button(root, text="Prev", command=lambda: packPrev4())
prev5 = tk.Button(root, text="Prev", command=lambda: packPrev5())
prev6 = tk.Button(root, text="Prev", command=lambda: packPrev6())
prev7 = tk.Button(root, text="Prev", command=lambda: packPrev7())
prev8 = tk.Button(root, text="Prev", command=lambda: packPrev8())
prev9 = tk.Button(root, text="Prev", command=lambda: packPrev9())
prev10 = tk.Button(root, text="Prev", command=lambda: packPrev10())


next0.pack()




tk.mainloop()
