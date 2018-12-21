import sqlite3
import Tkinter  as tk
import re

# preparer l expression reguliere
regexp1=r"/(\%27)|(\')|(\-\-)|(\%23)|(#)|/ix"
regexp2=r"/((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))|/i"
regexp3=r"/\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))|/ix"

L=[regexp1,regexp2,regexp3]


# la fonction test sert a tester controler les entres d'utilisateur 
def test(mot):
	for i in L:
		if re.match(i,mot) is not None:
			return True
	return False

# la fonction connect nous permet de se connecter a la base de donnes 
def connect():
	
	conn = sqlite3.connect('test.db')
	c = conn.cursor()
	l=(login.get(),password.get())
	# controler login et password 
	if test(login.get()) or test(password.get()): 
		label3=tk.Label(f, text="impossible", background="red", fg="white")
		label3.pack( padx = 5, pady = 5)
		return
	
	
	c.execute("SELECT * FROM client WHERE login=? AND password=?",l)
	# si la requette revoient  des esultats no null dans ce cas nous aurons connecter 	
	if c.fetchone() is not None:
		label3=tk.Label(f, text="connect", background="green", fg="white")
		label3.pack( padx = 5, pady = 5)
	# si non donc login ou password est incorrecte
	else:
		label3=tk.Label(f, text='Login / password incorrect', background="green", fg="white")
		label3.pack( padx = 5, pady = 5)

# un petit  interface grafique 
f=tk.Tk()
f.title("InjectionSQL")
f.geometry("200x200")
label=tk.Label(f, text="Enter your login: ")
label.pack()
login = tk.Entry ( f , textvariable = "" , width =30)
login. pack ()

label2=tk.Label(f, text="Enter your password: ")
label2.pack()
password = tk.Entry(f ,textvariable = "" , width =30)
password.pack()
b = tk.Button(f,text='      connect       ',command=connect)
b.pack()
f.mainloop()
