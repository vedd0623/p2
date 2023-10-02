from tkinter import *
from tkinter.messagebox import *
from datetime import *

root=Tk()
root.title('Calculator')
root.geometry('700x700+50+50')
f=("Arial",15,'bold')
F=('Arial',15,'bold','underline')
F1=('Comic Sans MS',15,'bold','underline')
new=('Algerian',30,'bold','underline')

lab=Label(root,text='Converter',font=new)
lab.pack(pady=10)

lab_area=Label(root,text='AREA:-',font=F1,fg='cyan')
lab_angle=Label(root,text='ANGLE:-',font=F1,fg='cyan')
lab_data=Label(root,text='DATA:-',font=F1,fg='cyan')
lab_volume=Label(root,text='VOLUME:-',font=F1,fg='cyan')
lab_length=Label(root,text='LENGTH:-',font=F1,fg='cyan')

d=datetime.now().time()
hr=d.hour
if hr<12:
	root.configure(bg='Yellow')
	lab.configure(bg='Yellow')
	lab_area.configure(bg='yellow')
	lab_angle.configure(bg='yellow')
	lab_data.configure(bg='yellow')
	lab_volume.configure(bg='yellow')
	lab_length.configure(bg='yellow')
elif hr<16:
	root.configure(bg='lightgreen')
	lab.configure(bg='lightgreen')
	lab_area.configure(bg='lightgreen')
	lab_angle.configure(bg='lightgreen')
	lab_data.configure(bg='lightgreen')
	lab_volume.configure(bg='lightgreen')
	lab_length.configure(bg='lightgreen')
elif hr<18:
	root.configure(bg='darkgreen')
	lab.configure(bg='darkgreen')
	lab_area.configure(bg='darkgreen')
	lab_angle.configure(bg='darkgreen')
	lab_data.configure(bg='darkgreen')
	lab_volume.configure(bg='darkgreen')
	lab_length.configure(bg='darkgreen')
elif hr<24:
	root.configure(bg='Blue')
	lab.configure(bg='Blue')
	lab_area.configure(bg='Blue')
	lab_angle.configure(bg='blue')
	lab_data.configure(bg='blue')
	lab_volume.configure(bg='blue')
	lab_length.configure(bg='blue')

#This is for Area Converter
def f1():
	root.withdraw()
	sq_to_acre.deiconify()

def f2():
	root.withdraw()
	acre_to_sqft.deiconify()

def f3():
	sq_to_acre.withdraw()
	root.deiconify()

def f4():
	acre_to_sqft.withdraw()
	root.deiconify()

lab_area.place(x=100,y=105)

btn_sq_to_acre=Button(root,text='Square Feet to Acres',font=f,command=f1,bg='cyan')
btn_sq_to_acre.place(x=245,y=100)
btn_acre_to_sqft=Button(root,text='Acres to Square Feet',font=f,command=f2,bg='cyan')
btn_acre_to_sqft.place(x=470,y=100)

sq_to_acre=Tk()
sq_to_acre.title('Square Feet To Acres')
sq_to_acre.geometry('500x500')
sq_to_acre.configure(bg='magenta')
lab_sa=Label(sq_to_acre,text='Square Feet',font=F,bg='magenta')
ent_sa=Entry(sq_to_acre,font=f,bg='magenta')
lab_sa.place(x=50,y=50)
ent_sa.place(x=200,y=50)
def sq_to_ac():
	try:
		sq=float(ent_sa.get())
		if sq<0:
			showerror('Wrong!','No Negative Input')
			ent_sa.delete(0,END)
			ent_sa.focus()
			return
		if sq<=1 or sq>=2613600:
			showerror('Wrong!','Limit Exceeded')
			ent_sa.delete(0,END)
			ent_sa.focus()
			return
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_sa.delete(0,END)
		ent_sa.focus()
		return
	a=sq * 23 * 10**(-5)
	showinfo('Acres',round(a,5))
	ent_sa.delete(0,END)
	ent_sa.focus()
	
btn_sa_conv=Button(sq_to_acre,text='Convert',font=f,command=sq_to_ac,bg='magenta')
btn_sa_main=Button(sq_to_acre,text='Back To Main',font=f,command=f3,bg='magenta')
lab_sa_ans=Label(sq_to_acre,font=f,bg='magenta')
lab_sa_ans1=Label(sq_to_acre,font=f,bg='magenta')
btn_sa_conv.place(x=150,y=100)
btn_sa_main.place(x=280,y=100)
sq_to_acre.withdraw()

acre_to_sqft=Tk()
acre_to_sqft.title('Acres To Square Feet')
acre_to_sqft.geometry('500x500')
acre_to_sqft.configure(bg='magenta')
lab_a=Label(acre_to_sqft,text='Acres',font=F,bg='magenta')
ent_a=Entry(acre_to_sqft,font=f,bg='magenta')
lab_a.place(x=120,y=50)
ent_a.place(x=200,y=50)
def ac_to_sq():
	try:
		a=float(ent_a.get())
		if a<0:
			showerror('Wrong!','No Negative Input')
			ent_a.delete(0,END)
			ent_a.focus()
			return
		if a<=1 or a>=60:
			showerror('Wrong!','Limit Exceeded')
			ent_a.delete(0,END)
			ent_a.focus()
			return
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_a.delete(0,END)
		ent_a.focus()
		return
	sq=a * 43560
	showinfo('Square Feet',round(sq,5))
	ent_a.delete(0,END)
	ent_a.focus()

btn_a_conv=Button(acre_to_sqft,text='Convert',font=f,command=ac_to_sq,bg='magenta')
btn_a_main=Button(acre_to_sqft,text='Back To Main',font=f,command=f4,bg='magenta')
lab_a_ans=Label(acre_to_sqft,font=f,bg='magenta')
lab_a_ans1=Label(acre_to_sqft,font=f,bg='magenta')
btn_a_conv.place(x=150,y=100)
btn_a_main.place(x=280,y=100)
acre_to_sqft.withdraw()
#It ends here

#This is for Angle Converter
lab_angle.place(x=100,y=210)

def f5():
	root.withdraw()
	d_to_r.deiconify()

def f6():
	root.withdraw()
	rad_to_deg.deiconify()

def f7():
	d_to_r.withdraw()
	root.deiconify()

def f8():
	rad_to_deg.withdraw()
	root.deiconify()

btn_deg_to_rad=Button(root,text='Degrees To Radians',font=f,command=f5,bg='cyan')
btn_deg_to_rad.place(x=245,y=180)
btn_rad_to_deg=Button(root,text='Radians To Degrees',font=f,command=f6,bg='cyan')
btn_rad_to_deg.place(x=245,y=230)

d_to_r=Tk()
d_to_r.title('Degrees To Radians')
d_to_r.geometry('500x500')
d_to_r.configure(bg='yellow')
lab_dr=Label(d_to_r,text='Degrees',font=F,bg='yellow')
ent_dr=Entry(d_to_r,font=f,bg='yellow')
lab_dr.place(x=50,y=50)
ent_dr.place(x=200,y=50)
def deg_to_rad():
	try:
		d=float(ent_dr.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_dr.delete(0,END)
		ent_dr.focus()
		return
	r=d * 0.02
	showinfo('Radians',round(r,5))
	ent_dr.delete(0,END)
	ent_dr.focus()
	
btn_dr_conv=Button(d_to_r,text='Convert',font=f,command=deg_to_rad,bg='yellow')
btn_dr_main=Button(d_to_r,text='Back To Main',font=f,command=f7,bg='yellow')
btn_dr_conv.place(x=150,y=100)
btn_dr_main.place(x=280,y=100)
d_to_r.withdraw()

rad_to_deg=Tk()
rad_to_deg.title('Radians To Degrees')
rad_to_deg.geometry('500x500')
rad_to_deg.configure(bg='yellow')
lab_rd=Label(rad_to_deg,text='Radians',font=F,bg='yellow')
ent_rd=Entry(rad_to_deg,font=f,bg='yellow')
lab_rd.place(x=110,y=50)
ent_rd.place(x=200,y=50)
def r_to_d():
	try:
		r=float(ent_rd.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_rd.delete(0,END)
		ent_rd.focus()
		return
	d=r * 57.3
	showinfo('Degrees',round(d,5))
	ent_rd.delete(0,END)
	ent_rd.focus()

btn_rd_conv=Button(rad_to_deg,text='Convert',font=f,command=r_to_d,bg='yellow')
btn_rd_main=Button(rad_to_deg,text='Back To Main',font=f,command=f8,bg='yellow')
btn_rd_conv.place(x=150,y=100)
btn_rd_main.place(x=280,y=100)
rad_to_deg.withdraw()
#It ends here

#This is for Data Converter
lab_data.place(x=100,y=320)

def f9():
	root.withdraw()
	gb_to_mb.deiconify()

def f10():
	root.withdraw()
	mb_to_gb.deiconify()

def f11():
	gb_to_mb.withdraw()
	root.deiconify()

def f12():
	mb_to_gb.withdraw()
	root.deiconify()

btn_gb_to_mb=Button(root,text='Gigabytes To Megabytes',font=f,command=f9,bg='cyan')
btn_gb_to_mb.place(x=245,y=300)
btn_mb_to_gb=Button(root,text='Megabytes To Gigabytes',font=f,command=f10,bg='cyan')
btn_mb_to_gb.place(x=245,y=350)

gb_to_mb=Tk()
gb_to_mb.title('Gigabytes To Megabytes')
gb_to_mb.geometry('500x500')
gb_to_mb.configure(bg='grey')
lab_gm=Label(gb_to_mb,text='Gigabytes',font=F,bg='grey')
ent_gm=Entry(gb_to_mb,font=f,bg='grey')
lab_gm.place(x=50,y=50)
ent_gm.place(x=200,y=50)
def g_to_m():
	try:
		d=float(ent_gm.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_gm.delete(0,END)
		ent_gm.focus()
		return
	m=d * 1000
	showinfo('Megabytes',m)
	ent_gm.delete(0,END)
	ent_gm.focus()
	
btn_gm_conv=Button(gb_to_mb,text='Convert',font=f,command=g_to_m,bg='grey')
btn_gm_main=Button(gb_to_mb,text='Back To Main',font=f,command=f11,bg='grey')
lab_gm_ans=Label(gb_to_mb,font=f)
lab_gm_ans1=Label(gb_to_mb,font=f)
btn_gm_conv.place(x=150,y=100)
btn_gm_main.place(x=280,y=100)
gb_to_mb.withdraw()

mb_to_gb=Tk()
mb_to_gb.title('Megabytes To Gigabytes')
mb_to_gb.geometry('500x500')
mb_to_gb.configure(bg='grey')
lab_mg=Label(mb_to_gb,text='Megabytes',font=F,bg='grey')
ent_mg=Entry(mb_to_gb,font=f,bg='grey')
lab_mg.place(x=50,y=50)
ent_mg.place(x=200,y=50)
def m_to_g():
	try:
		r=float(ent_mg.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_mg.delete(0,END)
		ent_mg.focus()
		return
	g=r * 0.001
	showinfo('Gigabytes',g)
	ent_mg.delete(0,END)
	ent_mg.focus()

btn_mg_conv=Button(mb_to_gb,text='Convert',font=f,command=m_to_g,bg='grey')
btn_mg_main=Button(mb_to_gb,text='Back To Main',font=f,command=f12,bg='grey')
lab_mg_ans=Label(mb_to_gb,font=f)
lab_mg_ans1=Label(mb_to_gb,font=f)
btn_mg_conv.place(x=150,y=100)
btn_mg_main.place(x=280,y=100)
mb_to_gb.withdraw()
#It ends here

#This is for Volume Converter
lab_volume.place(x=100,y=450)

def f13():
	root.withdraw()
	l_to_ml.deiconify()

def f14():
	root.withdraw()
	ml_to_l.deiconify()

def f15():
	l_to_ml.withdraw()
	root.deiconify()

def f16():
	ml_to_l.withdraw()
	root.deiconify()

btn_l_to_ml=Button(root,text='Litres To Millilitres',font=f,command=f13,bg='cyan')
btn_l_to_ml.place(x=245,y=420)
btn_ml_to_l=Button(root,text='Millilitres To Litres',font=f,command=f14,bg='cyan')
btn_ml_to_l.place(x=245,y=470)

l_to_ml=Tk()
l_to_ml.title('Litres To Millilitres')
l_to_ml.geometry('500x500')
l_to_ml.configure(bg='lightgreen')
lab_lml=Label(l_to_ml,text='Litres',font=F,bg='lightgreen')
ent_lml=Entry(l_to_ml,font=f,bg='lightgreen')
lab_lml.place(x=50,y=50)
ent_lml.place(x=200,y=50)
def lit_to_ml():
	try:
		l=float(ent_lml.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_lml.delete(0,END)
		ent_lml.focus()
		return
	ml=l * 1000
	showinfo('Success',(round(ml,5),'ml'))
	ent_lml.delete(0,END)
	ent_lml.focus()
	
btn_lml_conv=Button(l_to_ml,text='Convert',font=f,command=lit_to_ml,bg='lightgreen')
btn_lml_main=Button(l_to_ml,text='Back To Main',font=f,command=f15,bg='lightgreen')
btn_lml_conv.place(x=150,y=100)
btn_lml_main.place(x=280,y=100)
l_to_ml.withdraw()

ml_to_l=Tk()
ml_to_l.title('Millilitres To Litres')
ml_to_l.geometry('500x500')
ml_to_l.configure(bg='lightgreen')
lab_mll=Label(ml_to_l,text='Millilitres',font=F,bg='lightgreen')
ent_mll=Entry(ml_to_l,font=f,bg='lightgreen')
lab_mll.place(x=50,y=50)
ent_mll.place(x=200,y=50)
def m_to_l():
	try:
		ml=float(ent_mll.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_mll.delete(0,END)
		ent_mll.focus()
		return
	l=ml * 10**(-3)
	showinfo('Success',(round(l,5),'litres'))
	ent_mll.delete(0,END)
	ent_mll.focus()

btn_mll_conv=Button(ml_to_l,text='Convert',font=f,command=m_to_l,bg='lightgreen')
btn_mll_main=Button(ml_to_l,text='Back To Main',font=f,command=f16,bg='lightgreen')
btn_mll_conv.place(x=150,y=100)
btn_mll_main.place(x=280,y=100)
ml_to_l.withdraw()
#It ends here

#This is for Length Converter
lab_length.place(x=100,y=550)

def f17():
	root.withdraw()
	i_to_cm.deiconify()

def f18():
	root.withdraw()
	cm_to_i.deiconify()

def f19():
	i_to_cm.withdraw()
	root.deiconify()

def f20():
	cm_to_i.withdraw()
	root.deiconify()

btn_i_to_cm=Button(root,text='Inches To Centimetres',font=f,command=f17,bg='cyan')
btn_i_to_cm.place(x=245,y=540)
btn_cm_to_i=Button(root,text='Centimetres To Inches',font=f,command=f18,bg='cyan')
btn_cm_to_i.place(x=245,y=590)

i_to_cm=Tk()
i_to_cm.title('Inches To Centimetres')
i_to_cm.geometry('500x500')
i_to_cm.configure(bg='brown')
lab_icm=Label(i_to_cm,text='Inches',font=F,bg='brown')
ent_icm=Entry(i_to_cm,font=f,bg='brown')
lab_icm.place(x=50,y=50)
ent_icm.place(x=200,y=50)
def in_to_cm():
	try:
		i=float(ent_icm.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_icm.delete(0,END)
		ent_icm.focus()
		return
	cm=i * 2.54
	showinfo('Success',(round(cm,2),'cm'))
	ent_icm.delete(0,END)
	ent_icm.focus()
	
btn_icm_conv=Button(i_to_cm,text='Convert',font=f,command=in_to_cm,bg='brown')
btn_icm_main=Button(i_to_cm,text='Back To Main',font=f,command=f19,bg='brown')
btn_icm_conv.place(x=150,y=100)
btn_icm_main.place(x=280,y=100)
i_to_cm.withdraw()

cm_to_i=Tk()
cm_to_i.title('Centimetres To Inches')
cm_to_i.geometry('500x500')
cm_to_i.configure(bg='brown')
lab_cmi=Label(cm_to_i,text='Centimetres',font=F,bg='brown')
ent_cmi=Entry(cm_to_i,font=f,bg='brown')
lab_cmi.place(x=50,y=50)
ent_cmi.place(x=200,y=50)
def cm_to_in():
	try:
		cm=float(ent_cmi.get())
	except:
		showerror('Wrong!','Enter Valid Input')
		ent_cmi.delete(0,END)
		ent_cmi.focus()
		return
	i=cm * 0.39
	showinfo('Success',(round(i,5),'inches'))
	ent_cmi.delete(0,END)
	ent_cmi.focus()

btn_cmi_conv=Button(cm_to_i,text='Convert',font=f,command=cm_to_in,bg='brown')
btn_cmi_main=Button(cm_to_i,text='Back To Main',font=f,command=f20,bg='brown')
btn_cmi_conv.place(x=150,y=100)
btn_cmi_main.place(x=280,y=100)
cm_to_i.withdraw()
#It ends here

def exit():
	if askokcancel('Quit','Do U Want To Exit?'):
		root.destroy()
		sq_to_acre.destroy()
		acre_to_sqft.destroy()
		d_to_r.destroy()
		rad_to_deg.destroy()
		gb_to_mb.destroy()
		mb_to_gb.destroy()		
		l_to_ml.destroy()
		ml_to_l.destroy()
		cm_to_i.destroy()
		i_to_cm.destroy()

root.protocol('WM_DELETE_WINDOW',exit)
sq_to_acre.protocol('WM_DELETE_WINDOW',exit)
acre_to_sqft.protocol('WM_DELETE_WINDOW',exit)
d_to_r.protocol('WM_DELETE_WINDOW',exit)
rad_to_deg.protocol('WM_DELETE_WINDOW',exit)
gb_to_mb.protocol('WM_DELETE_WINDOW',exit)
mb_to_gb.protocol('WM_DELETE_WINDOW',exit)
l_to_ml.protocol('WM_DELETE_WINDOW',exit)
ml_to_l.protocol('WM_DELETE_WINDOW',exit)
cm_to_i.protocol('WM_DELETE_WINDOW',exit)
i_to_cm.protocol('WM_DELETE_WINDOW',exit)

root.mainloop()
