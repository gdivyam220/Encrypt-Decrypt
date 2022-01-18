from tkinter import *
from turtle import bgcolor

rt = Tk()

# Main method to encrypt the data entered..
def change(s):
    ans=""
    for i in range(0,len(s)):
        if(ord(s[i])<=90 and ord(s[i])>64):
            ans = ans + chr(92-(ord(s[i])-63))
        elif(ord(s[i])>96 and ord(s[i])<123):
            ans = ans + chr(123-(ord(s[i])-96))
	else:
		ans = ans + s[i]
    return ans	

# Method to fetch from "plain text" field and
#                       output the data in "Cipher text" field
def for_e():
	et = change( e1.get())
	e2.insert(0, et)

# Method to fetch from "Cipher text" field and
#                       output the data in "plain text" field
def for_p():					
	pt = change(e2.get())
	e1.insert(0, pt)

#Method to desplay result "DATA ENCRYPTED"
def op():
    l3 = Label(rt, text ="DATA ENCRYPTED",bg='Light Yellow')		
    l3.grid(row = 40, column = 10)

#Method to desplay result "DATA DECRYPTED"
def op2():
    l3 = Label(rt, text ="DATA DECRYPTED",bg='Light Yellow')		
    l3.grid(row = 40, column = 10)

#Setting title of the window
rt.title("Divyam Gupta (19165020) Encoder/Decoder")
#Setting size of the window
rt.geometry("600x500")
#Setting background image in the window
bg = PhotoImage(file="bg.png")
lm2=Label(rt, image=bg)
lm2.place(x=0,y=0,relheight=1,relwidth=1)

#printing the heading
lm = Label(rt, text ="Encoder/Decoder",bg='Light yellow',fg="green",font=("",20))			
lm.grid(row = 1, column = 10)
#printing the label "Plain text"
l1 = Label(rt, text ="Plain text",bg='Light Yellow')			
l1.grid(row = 20, column = 2)
#printing the label "Cipher text"
l2 = Label(rt, text ="Cipher text",bg='light Yellow')
l2.grid(row = 20, column = 20)


l3 = Label(rt, text ="",bg='DARK GREEN')
l3.grid(row = 100, column = 1)
#Making a field to enter and recieve the plain data
e1 = Entry(rt,bg='Light Yellow')
e1.grid(row = 24, column = 2)

#Making a field to enter and recieve the cipher data
e2 = Entry(rt,bg='Light Yellow')
e2.grid(row = 24, column = 20)

#button to encrypt the imput data and simultaneously clearing any pre-existing entry in the field
enc = Button(rt,fg='green', text = "Encrypt", pady=0,padx=0, command = lambda:[e2.delete(0, END),for_e(),op()])
enc.grid(row = 27, column = 2)

#button to decrypt the imput data and simultaneously clearing any pre-existing entry in the field
dec = Button(rt,fg='green', text = "Decrypt", pady=0,padx=0, command = lambda:[e1.delete(0, END),for_p(),op2()])
dec.grid(row = 27, column = 20)

rt.mainloop()
