from tkinter import *
from tkinter import ttk
class Number:
	num=""
	name=""
	choice=""


class Binary(Number):
	def __init__(self):
		print("Binary object created")
	def setValue(self):
		self.num=input("enter a biniary number:")
	def bin_choice(self,c,n):
		self.choice=c	
		self.name=n
	def getChoice(self):
		return self.choice



		


class Decimal(Number):
	def __init__(self):
		print("Decimal object created")
	def setValue(self):
		self.num=input("enter a decimal number:")
	
	def bin_choice(self,c,n):
		self.choice=c	
		self.name=n
	def getChoice(self):
		return self.choice

	

	



class Octal(Number):
	def __init__(self):
		print("Octal object created")
		
	def setValue(self):
		self.num=input("enter a octal number:")
	
	def bin_choice(self,c,n):
		self.choice=c	
		self.name=n
	def getChoice(self):
		return self.choice	

class HexaDecimal(Number):
	def __init__(self):
		print("HexaDecimal object created")
	def setValue(self):
		self.num=input("enter a hexadecimal number:")
	
	def bin_choice(self,c,n):
		self.choice=c	
		self.name=n
	def getChoice(self):
		return self.choice			



def convert_toBinary(n):
		l=[]
		n=int(n)
		while n:
			l.append(str(n%2))
			n=n//2
		
		return l

def convert_toOctal(n):
	l=[]
	n=int(n)
	while n:
		l.append(str(n%8))
		n=n//8

	return l	

def convert_toHexaDecimal(n):
	a=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
	l=[]
	# i=0
	# t=0
	
	# print(m)
	# for x in m:
	# 	print(x)
	# 	t+=10**i+int(x)
	# 	i+=1

	while n:

		l.append(a[n%16])
		n=n//16

	return l	


def convert_toDecimal(n):
	a=n[::-1]
	i=0
	d={"0":0,"1":1,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
	sum=0
	k=0
	if var1.get()=="Binary":
		k=2
	elif var1.get()=="Octal":
		k=8
	elif var1.get()=="HexaDecimal":
		k=16


	for x in a:
		if k==16:
			sum+=k**i *d[x]
		else:
			sum+=k**i * int(x)
		i+=1

	return sum	

obj=""
l2=""
choice=""
done=""
l3=""
l4=""
entry=""
convert=""
back1=""
back2=""
l5=""
l7=""
def perform():
	global l5,l7
	if not l5=="":
		l5.pack_forget() 
	if not l7=="":
		l7.pack_forget() 


	if var1.get()=="Decimal":
		try:
			if int(var3.get())<0:
				raise ValueError
				
		except ValueError:
			if not l5=="":
				l5.pack_forget() 
			l7=Label(app,text="oops... negative value",font=3,bg="cyan",fg="gray")
			l7.pack(padx=2,pady=3)
	
		else:
			if var2.get()=="toBinary":
							
				value=convert_toBinary(var3.get())
					
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toOctal":
				value=convert_toOctal(var3.get())
				print(value)
				print("".join(value))
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toHexaDecimal":
				value=convert_toHexaDecimal(var3.get())
				print(value)
				print("".join(value))
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)

	elif var1.get()=="Binary":
		try :
			for x in var3.get():
				if int(x)==0 or int(x)==1:
					pass
				else:
					raise ValueError	

		except ValueError:
			if not l5=="":
				l5.pack_forget() 
			l7=Label(app,text="oops... not a binary number",font=3,bg="cyan",fg="gray")
			l7.pack(padx=2,pady=3)
		else:
			if var2.get()=="toDecimal":
				value=convert_toDecimal(var3.get())
				
				l5=Label(app,text=str(value),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toOctal":
				temp=convert_toDecimal(var3.get())
				value=convert_toOctal(temp)
				
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toHexaDecimal":
				temp=convert_toDecimal(var3.get())
				value=convert_toHexaDecimal(temp)
				
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)	

	elif var1.get()=="Octal":
		try :
			for x in var3.get():
				if int(x)>=0 and int(x)<8:
					pass
				else:
					raise ValueError	

		except ValueError:
			if not l5=="":
				l5.pack_forget() 
			l7=Label(app,text="oops... not a octal number",font=3,bg="cyan",fg="gray")
			l7.pack(padx=2,pady=3)

		else:	
			if var2.get()=="toBinary":
				t=convert_toDecimal(var3.get())
				value=convert_toBinary(t)
				print(value)
				print("".join(value))
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toDecimal":
				value=convert_toDecimal(var3.get())
				
				l5=Label(app,text=str(value),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toHexaDecimal":
				t=convert_toDecimal(var3.get())
				value=convert_toHexaDecimal(t)
				print(value)
				print("".join(value))
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)

	elif var1.get()=="HexaDecimal":
		try :
			for x in var3.get():
				if (int(x)>=0 and int(x)<=9) or (x>="A" and x<="F"):
					pass
				else:
					print(x)
					raise ValueError	

		except ValueError:
			if not l5=="":
				l5.pack_forget() 
			l7=Label(app,text="oops... not a hexadecimal number",font=3,bg="cyan",fg="gray")
			l7.pack(padx=2,pady=3)
		else:	
			if var2.get()=="toBinary":
				t=convert_toDecimal(var3.get())
				value=convert_toBinary(t)
				
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toDecimal":
				value=convert_toDecimal(var3.get())
				
				l5=Label(app,text=str(value),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)
			elif var2.get()=="toOctal":
				t=convert_toDecimal(var3.get())
				value=convert_toOctal(t)
				
				l5=Label(app,text=str("".join(value)[::-1]),font=3,bg="cyan",fg="gray")
				l5.pack(padx=2,pady=3)						

			

		

def goto_back():
	global l3,l5,l4,entry,convert,back1
	l3.pack_forget()
	l4.pack_forget()

	entry.pack_forget()
	convert.pack_forget()
	back1.pack_forget()
	l5.pack_forget()
	createObject()

def conversion():
	global l3,l4,entry,convert,back
	l3=Label(app,text=f"from {var1.get()} {var2.get()}",font=3,bg="cyan",fg="red")
	l3.pack(padx=2,pady=3)
	l4=Label(app,text="enter value for conversion",font=3,bg="cyan",fg="red")
	l4.pack(padx=2,pady=3)

	entry=Entry(app,textvariable=var3,width=10,font=3,bg="cyan",fg="red")
	entry.pack(padx=2,pady=3)
	convert=Button(app,text="Done",command=perform)
	convert.pack(padx=2,pady=3)
	back1=Button(app,text="Back",command=goto_back)
	back1.pack(padx=2,pady=3)

def pur_choice():
	global var2,obj,l2,choice
	global done
	obj.bin_choice(var2.get(),var1.get())
	print(obj.getChoice())
	conversion()
	l2.pack_forget()
	choice.pack_forget()
	done.pack_forget()
	




def createObject():
	global var1,obj
	global l2,var2,choice,done
	if var1.get()=="Binary":
		obj=Binary()
		
		l2=Label(app,text="from Binary",font=3,bg="cyan",fg="red")
		l2.pack(padx=2,pady=3)
		var2=StringVar()
		choice=ttk.Combobox(app,font=10,textvariable=var2)
		choice['values']=("toDecimal","toOctal","toHexaDecimal")
		choice.current()
		choice.pack()
		done=Button(app,text="Done",command=pur_choice)
		done.pack(padx=2,pady=3)



	elif var1.get()=="Decimal":
		obj=Decimal()
		
		l2=Label(app,text="from Decimal",font=3,bg="cyan",fg="red")
		l2.pack(padx=2,pady=3)
		var2=StringVar()
		choice=ttk.Combobox(app,font=10,textvariable=var2)
		choice['values']=("toBinary","toOctal","toHexaDecimal")
		choice.current()
		choice.pack()
		done=Button(app,text="Done",command=pur_choice)
		done.pack(padx=2,pady=3)
	elif var1.get()=="Octal":
		obj=Octal()
		
		l2=Label(app,text="from Octal",font=3,bg="cyan",fg="red")
		l2.pack(padx=2,pady=3)
		var2=StringVar()
		choice=ttk.Combobox(app,font=10,textvariable=var2)
		choice['values']=("toDecimal","toBinary","toHexaDecimal")
		choice.current()
		choice.pack()
		done=Button(app,text="Done",command=pur_choice)
		done.pack(padx=2,pady=3)
	else:
		obj=HexaDecimal()
		
		l2=Label(app,text="from HexaDecimal",font=3,bg="cyan",fg="red")
		l2.pack(padx=2,pady=3)
		var2=StringVar()
		choice=ttk.Combobox(app,font=10,textvariable=var2)
		choice['values']=("toDecimal","toOctal","toBinary")
		choice.current()
		choice.pack()
		done=Button(app,text="Done",command=pur_choice)
		done.pack(padx=2,pady=3)
		
def pur_createObject():
	createObject()
	global l1
	global next
	global options

	l1.pack_forget()
	next.pack_forget()
	options.pack_forget()







app=Tk()



var1=StringVar()
var2=StringVar()
var3=StringVar()


l1=Label(app,text="WELCOME",font=3,bg="cyan",fg="red")
l1.pack(padx=2,pady=3)

options=ttk.Combobox(app,font=10,textvariable=var1)
options['values']=("Binary","Decimal","Octal","HexaDecimal")
options.current()
options.pack()


next=Button(app,text="Next",command=pur_createObject)
next.pack(padx=2,pady=3)
app.geometry("300x350")
app.mainloop()