from tkinter import*
from tkinter.messagebox import*
from tkinter.scrolledtext import*
from sqlite3 import*

def f1():  
	task_string = task_field.get()  
	con = None
	if len(task_string) == 0:  
		showinfo('Error', 'Field is Empty.')  
	else:    
		try:
			con = connect("todo.db")
			cursor=con.cursor()
			sql = "insert into task values('%s')"
			cursor.execute(sql%(task_string))
			con.commit()
			showinfo("Sucess","Task added")
		except Exception as e:
			showerror("Issue",e)
			con.rollback()
		finally:
			if con is not None:
				con.close()
				task_field.delete(0,END)      
def f2():
	main_window.withdraw()
	view_window.deiconify()
	vw_st_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect("todo.db")
		cursor=con.cursor()
		sql="select * from task"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			info=info + str(d[0])+"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()
def f4():
	con=None
	try:
		con=connect("todo.db")
		sql="delete from task where tname='%s' "
		cursor =con.cursor()

		task_string = task_field.get() 
		cursor.execute(sql % (task_string))
	
		if cursor.rowcount==1:
			con.commit()
			showinfo("Sucess","Task deleted")
		else:
			showinfo("error","No such task")

	except Exception as e:
		print("their is an exception ",e)
		con.rollback()
	finally:
		if con is not None:	
			con.close()
			task_field.delete(0,END)
def f3():
	main_window.withdraw()
	upd_window.deiconify()

def f5():
	view_window.withdraw()
	main_window.deiconify()

def f6():
	con=None
	try:
		con=connect("todo.db")
		sql1="select * from task where tname='%s'"
		sql="update task set tname='%s' where tname='%s'"
		cursor =con.cursor()
		s1 = upd_ent_old.get() 
		s2 = upd_ent_new.get()
		cursor.execute(sql1 % (s1))
		data=cursor.fetchall()
		if len(data) == 0:
			showinfo("error","No such task")
		else:
			cursor.execute(sql % (s2,s1))
			con.commit()
			showinfo("Sucess","Task updated")
	except Exception as e:
		print("their is an exception ",e)
		con.rollback()
	finally:
		if con is not None:	
			con.close()
			upd_ent_old.delete(0,END)
			upd_ent_new.delete(0,END)
def f7():
	upd_window.withdraw()
	main_window.deiconify()

main_window=Tk()
main_window.title("Todo application")
main_window.geometry("700x700+100+100")
f=("Calibri",20,"bold")

task_lab = Label(main_window,text="enter task: ",font=f)
task_field = Entry(main_window , font=f)
task_lab.pack(pady=10)
task_field.pack(pady=10)
mw_btn_add=Button(main_window ,text="Add",font=f,width=8,command=f1)
mw_btn_vw=Button(main_window,text="view",font=f,width=8,command=f2)
mw_btn_upd=Button(main_window ,text="update",font=f,width=8,command=f3)
mw_btn_del=Button(main_window ,text="delete",font=f,width=8,command=f4)

mw_btn_add.pack(pady=10)
mw_btn_del.pack(pady=10)
mw_btn_upd.pack(pady=10)
mw_btn_vw.pack(pady=10)

view_window=Toplevel(main_window)
view_window.title("task's")
view_window.geometry("500x500+100+100")

vw_st_data =ScrolledText(view_window,width=30 ,height=10 ,font=f)
vw_btn_back= Button(view_window , text="Back",font=f,command=f5)
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
view_window.withdraw()

upd_window=Toplevel(main_window)
upd_window.title("update task")
upd_window.geometry("500x500+100+100")

upd_lab_old = Label(upd_window,text="enter previous task name: " , font=f)
upd_ent_old= Entry(upd_window , font=f)
upd_lab_new = Label(upd_window,text="enter new task name: " , font=f)
upd_ent_new= Entry(upd_window , font=f)
upd_btn_save= Button(upd_window , text="Save ",font=f,command=f6)
upd_btn_back= Button(upd_window , text="Back",font=f,command=f7)

upd_lab_old.pack(pady=10)
upd_ent_old.pack(pady=10)
upd_lab_new.pack(pady=10)
upd_ent_new.pack(pady=10)
upd_btn_save.pack(pady=10)
upd_btn_back.pack(pady=10)
upd_window.withdraw()

main_window.mainloop()