from tkinter import *
import time

# creating root object
root = Tk()

# defining size of window
root.geometry("1450x680")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width = 1600)
Tops.pack(side = TOP)

f1 = Frame(root, width = 800, height = 700)
f1.pack(side = LEFT)


localtime = time.asctime(time.localtime(time.time()))

label_info = Label(Tops, font = ('', 30, 'bold'), text = "AR Messanger", fg = "Black", bd = 10, anchor='w').grid(row = 0, column = 0)

label_info = Label(Tops, font = ('', 7, 'bold'), text = "TG CyberLabs", fg = "Black", bd = 1, anchor='w').grid(row=1, column=0)

label_info = Label(Tops, font=('', 12, 'bold'), text = localtime, fg = "Steel Blue", bd = 10, anchor = 'w').grid(row = 2, column = 0)

rand = StringVar()
message = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# exit func
def qExit():
	root.destroy()

# window reset func
def Reset():
	rand.set("")
	message.set("")
	key.set("")
	mode.set("")
	Result.set("")


# reference
name = Label(f1, font = ('lucida console', 16, 'bold'), text = "Name:", bd = 16, anchor = "w").grid(row = 0, column = 0)

txtReference = Entry(f1, font = ('lucida console', 16, 'bold'), textvariable = rand, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right').grid(row = 0, column = 1)

# labels
label_msg = Label(f1, font = ('lucida console', 16, 'bold'), text = "MESSAGE:", bd = 16, anchor = "w").grid(row = 1, column = 0)

txt_msg = Entry(f1, font = ('lucida console', 16, 'bold'), textvariable = message, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right').grid(row = 1, column = 1)

label_key = Label(f1, font = ('lucida console', 16, 'bold'), text = "KEY:", bd = 16, anchor = "w").grid(row = 2, column = 0)

txt_key = Entry(f1, font = ('lucida console', 16, 'bold'), textvariable = key, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right').grid(row = 2, column = 1)

label_mode = Label(f1, font = ('lucida console', 16, 'bold'), text = "MODE('e' for encrypt, 'd' for decrypt)", bd = 16, anchor = "w").grid(row = 3, column = 0)

txt_mode = Entry(f1, font = ('lucida console', 16, 'bold'), textvariable = mode, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right').grid(row = 3, column = 1)

label_service = Label(f1, font = ('lucida console', 16, 'bold'), text = "The Result-", bd = 16, anchor = "w").grid(row = 2, column = 2)

txt_service = Entry(f1, font = ('lucida console', 16, 'bold'), textvariable = Result, bd = 10, insertwidth = 4, bg = "powder blue", justify = 'right').grid(row = 2, column = 3)


import base64  # Vigenere cipher


def encode(key, clear):
	enc = []
	
	for i in range(len(clear)):
		key_c = key[i % len(key)]
		enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
					
		enc.append(enc_c)
		
	return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key, enc):
	dec = []
	
	enc = base64.urlsafe_b64decode(enc).decode()
	for i in range(len(enc)):
		key_c = key[i % len(key)]
		dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
							
		dec.append(dec_c)
	return "".join(dec)


def Ref():
	print("Message= ", (message.get()))

	clear = message.get()
	k = key.get()
	m = mode.get()

	if (m == 'e'):
		Result.set(encode(k, clear))
	else:
		Result.set(decode(k, clear))

showmsg_button = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ('lucida console', 16, 'bold'), width = 10, text = "Show Message", bg = "powder blue", command = Ref).grid(row = 7, column = 1)

reset_button = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ('lucida console', 16, 'bold'), width = 10, text = "Reset", bg = "green", command = Reset).grid(row = 7, column = 2)

exit_button = Button(f1, padx = 16, pady = 8, bd = 16, fg = "black", font = ('lucida console', 16, 'bold'), width = 10, text = "Exit", bg = "red", command = qExit).grid(row = 7, column = 3)

root.mainloop()

# now we aill see the demonstration of the project.