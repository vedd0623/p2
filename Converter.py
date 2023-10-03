from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from requests import *
from datetime import *

root=Tk()
root.title('Practice')
root.geometry('750x700+50+50')
f=('arial',20)
F=('ALGERIAN',20,'underline')
lab=Label(root,text='CONVERTER',font=F)
lab.place(x=300,y=50)

d=datetime.now().time()
hr=d.hour
if hr<12:
	lab.configure(bg='yellow')
	root.configure(bg='yellow')
elif hr<16:
	lab.configure(bg='lightgreen')
	root.configure(bg='lightgreen')
elif hr<18:
	lab.configure(bg='green')
	root.configure(bg='green')
elif hr<24:
	lab.configure(bg='blue')
	root.configure(bg='blue')

l1=['in-cm','cm-in','m-km','km-m']
a1=['sqft-sqm','sqm-sqft','sqft-acres','acres-sqft']
v1=['l-ml','ml-l','cubic metres-cubic cm','cubic cm-cubic metres']
ang1=['deg-rad','rad-deg','deg-grad','grad-deg']
c1=['dol-inr','inr-dol']

def length():
	ent_l=Entry(root,font=f,bg='cyan')
	combol=ttk.Combobox(root,values=l1)
	ent_l.place(x=250,y=100)
	combol.place(x=250,y=150)

	def convl():
		if combol.get()=='':
			showerror('Issue','Select an option!')

		if combol.get()=='in-cm':
			try:
				a=float(ent_l.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			cm=a*2.54
			showinfo('Conversion',(round(cm,3),'cm'))

		if combol.get()=='cm-in':
			try:
				a=float(ent_l.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			i=a*0.39
			showinfo('Conversion',(round(i,3),'in'))

		if combol.get()=='m-km':
			try:
				a=float(ent_l.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			km=a* 1 * 10**(-3)
			showinfo('Conversion',(round(km,3),'km'))

		if combol.get()=='km-m':
			try:
				a=float(ent_l.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			m=a*1000
			showinfo('Conversion',(round(m,3),'m'))

	def backl():
		ent_l.destroy()
		combol.destroy()
		btn_convl.destroy()
		btn_backl.destroy()		
		
	btn_convl=Button(root,text='Convert',font=f,command=convl,bg='cyan')
	btn_convl.place(x=400,y=150)
	btn_backl=Button(root,text='Back',font=f,command=backl,bg='cyan')
	btn_backl.place(x=550,y=150)

btn_l=Button(root,text='Length',font=f,command=length,bg='cyan')
btn_l.place(x=100,y=100)

def area():
	ent_a=Entry(root,font=f,bg='cyan')
	comboa=ttk.Combobox(root,values=a1)
	ent_a.place(x=250,y=200)
	comboa.place(x=250,y=250)

	def conva():
		if comboa.get()=='':
			showerror('Issue','Select an option!')
		if comboa.get()=='sqft-sqm':
			try:
				a=float(ent_a.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			sqm=a*0.09
			showinfo('Conversion',(round(sqm,3),'sqm'))
		if comboa.get()=='sqm-sqft':
			try:
				a=float(ent_a.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			sqft=a*10.76
			showinfo('Conversion',(round(sqft,3),'sqft'))
		if comboa.get()=='sqft-acres':
			try:
				a=float(ent_a.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			ac=a* 23*10**(-5)
			showinfo('Conversion',(round(ac,3),'acres'))
		if comboa.get()=='acres-sqft':
			try:
				a=float(ent_a.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			sqft=a*43560
			showinfo('Conversion',(round(sqft,3),'sqft'))

	def backa():
		ent_a.destroy()
		comboa.destroy()
		btn_conva.destroy()
		btn_backa.destroy()		
		
	btn_conva=Button(root,text='Convert',font=f,command=conva,bg='cyan')
	btn_conva.place(x=400,y=250)
	btn_backa=Button(root,text='Back',font=f,command=backa,bg='cyan')
	btn_backa.place(x=550,y=250)

btn_a=Button(root,text='Area',font=f,command=area,bg='cyan')
btn_a.place(x=100,y=200)

def vol():
	ent_v=Entry(root,font=f,bg='cyan')
	combov=ttk.Combobox(root,values=v1)
	ent_v.place(x=250,y=300)
	combov.place(x=250,y=350)

	def convv():
		if combov.get()=='':
			showerror('Issue','Select an option!')
		if combov.get()=='l-ml':
			try:
				a=float(ent_v.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			ml=a*1000
			showinfo('Conversion',(round(ml,3),'ml'))
		if combov.get()=='ml-l':
			try:
				a=float(ent_v.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			l=a*10**(-3)
			showinfo('Conversion',(round(l,3),'l'))
		if combov.get()=='cubic metres-cubic cm':
			try:
				a=float(ent_v.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			ccm=a* 10**6
			w=str(ccm)
			w1=w.replace('e','*10 raised to ')
			showinfo('Conversion',(w1,'cubic cm'))
		if combov.get()=='cubic cm-cubic metres':
			try:
				a=float(ent_v.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			cubm=a* 10**(-6)
			new=str(cubm)
			new1=new.replace('e','*10 raised to ')
			showinfo('Conversion',(new1,'cubic metres'))
		
	def backv():
		ent_v.destroy()
		combov.destroy()
		btn_convv.destroy()
		btn_backv.destroy()		
		
	btn_convv=Button(root,text='Convert',font=f,command=convv,bg='cyan')
	btn_convv.place(x=400,y=350)
	btn_backv=Button(root,text='Back',font=f,command=backv,bg='cyan')
	btn_backv.place(x=550,y=350)

btn_v=Button(root,text='Volume',font=f,command=vol,bg='cyan')
btn_v.place(x=100,y=300)

def ang():
	ent_ang=Entry(root,font=f,bg='cyan')
	comboang=ttk.Combobox(root,values=ang1)
	ent_ang.place(x=250,y=400)
	comboang.place(x=250,y=450)

	def convang():
		if comboang.get()=='':
			showerror('Issue','Select an Option!')
		if comboang.get()=='deg-rad':
			try:
				a=float(ent_ang.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			r=a*0.02
			showinfo('Conversion',(round(r,3),'rad'))
		if comboang.get()=='rad-deg':
			try:
				a=float(ent_ang.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			d=a*57.3
			showinfo('Conversion',(round(d,3),'deg'))
		if comboang.get()=='deg-grad':
			try:
				a=float(ent_ang.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			g=a* 1.11
			showinfo('Conversion',(round(g,3),'grad'))
		if comboang.get()=='grad-deg':
			try:
				a=float(ent_ang.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			d=a* 0.9
			showinfo('Conversion',(round(d,3),'deg'))		
	def backang():
		ent_ang.destroy()
		comboang.destroy()
		btn_convang.destroy()
		btn_backang.destroy()		
		
	btn_convang=Button(root,text='Convert',font=f,command=convang,bg='cyan')
	btn_convang.place(x=400,y=450)
	btn_backang=Button(root,text='Back',font=f,command=backang,bg='cyan')
	btn_backang.place(x=550,y=450)

btn_ang=Button(root,text='Angle',font=f,command=ang,bg='cyan')
btn_ang.place(x=100,y=400)

def curr():
	ent_curr=Entry(root,font=f,width=30,bg='cyan')
	ent_curr.insert(0,'Data Connection Should Be On....')
	combocurr=ttk.Combobox(root,values=c1)
	ent_curr.place(x=250,y=500)
	combocurr.place(x=250,y=550)
	
	def convcurr():
		if combocurr.get()=='':
			showerror('Issue','Select an Option!')
		if combocurr.get()=='dol-inr':
			url='https://api.exchangerate-api.com/v4/latest/USD'
			timeout=10
			try:
				res=get(url)
				showinfo('Success','Data Connection is On')
			except:
				showerror('Error404','Data Connection is Off')
				return
			data=res.json()
			inr=data['rates']['INR']
			try:
				aid=float(ent_curr.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			air=aid*inr
			showinfo('Conversion',(round(air,2),'\u20B9'))
		if combocurr.get()=='inr-dol':
			url='https://api.exchangerate-api.com/v4/latest/USD'
			timeout=10
			try:
				res=get(url)
				showinfo('Success','Data Connection is On')
			except:
				showerror('Error404','Data Connection is Off')
				return
			data=res.json()
			inr=data['rates']['INR']
			try:
				air=float(ent_curr.get())
			except:
				showerror('Issue','Enter Valid Input')
				return
			aid=air/inr
			showinfo('Conversion',(round(aid,3),'$'))

	def backcurr():
		ent_curr.destroy()
		combocurr.destroy()
		btn_convcurr.destroy()
		btn_backcurr.destroy()		
		
	btn_convcurr=Button(root,text='Convert',font=f,command=convcurr,bg='cyan')
	btn_convcurr.place(x=400,y=550)
	btn_backcurr=Button(root,text='Back',font=f,command=backcurr,bg='cyan')
	btn_backcurr.place(x=550,y=550)

btn_curr=Button(root,text='Currency',font=f,command=curr,bg='cyan')
btn_curr.place(x=100,y=500)

root.mainloop()