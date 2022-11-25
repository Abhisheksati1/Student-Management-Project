import os
from os import system
import mysql.connector as msc
	
mydb=msc.connect(host="localhost",user="root",passwd="", database="pythonbatch")
mycur=mydb.cursor()
	
def main():
    ch=''
    
    while ch!= 'x' or ch!='X':
        system('cls')
        print("\n\n\t\tMAIN MENU")
        print("\n A --> Add Student")
        print("\n E --> Edit Student")
        print("\n D --> Delete Student")
        print("\n V --> View Student")
        print("\n X --> Exit ")
        ch=input("\nEnter Your Choice...")
        if ch=='a' or ch=='A':
            add()
        elif ch=='e' or ch=='E':
            edit()
        elif ch=='d' or ch=='D':
            delete()
        elif ch=='v' or ch=='V':
            view()
        elif ch=='x' or ch=='X':
            print("\n THANKS FOR USING SOFTWARE...")
            break;

def add():
	system('cls')
	try:
		rn=int(input("Enter Roll NO "))
		na=input("Enter Name ")
		age=int(input("Enter Age "))
		mycur.execute("insert into stu values ({},'{}',{})".format(rn,na,age))
		mydb.commit()
		print("Data Added Successfully......")
	except:
		print("Error in D/b")
	finally:
		mydb.close()
	c=input("\n\n\nPress Any Key to Continuee....")

def edit():
	system('cls')
	rn=int(input("Enter Roll NO to Edit "))
	mycur.execute("select * from stu where rn={}".format(rn))
	results = mycur.fetchall()
	for row in results:
		rn = row[0] #row[col no]
		lname = row[1]
		age = row[2]
		print (str(rn),"\t", lname,"\t", str(age) )
	print("Enter New Data ...")
	print("*"*40)
	na=input("Enter New Name ")
	age=int(input("Enter New Age "))
	q="Update stu set na='{}',age={} where rn={}".format(na,age,rn)
	mycur.execute(q)
	mydb.commit()
	print("Data Modified Successfully...")
	c=input("\n\n\nPress Any Key to Continuee....")
def delete():
	system('cls')
	try:
		rn=int(input("Enter Roll NO to Delete "))
		mycur.execute("select * from stu where rn={}".
		format(rn))
		results = mycur.fetchall()
		for row in results:
			rn = row[0] #row[col no]
			lname = row[1]
			age = row[2]
			print (str(rn),"\t", lname,"\t", str(age) )
		ans=input("Delete This Record (Y/N)? ")
		if ans=='y' or ans=='Y':
			mycur.execute("delete from stu where rn={}".format(rn))
			mydb.commit()
			print("Data Deleted Successfully...")
		else:
			print("Data Not Deleted ...")
	except:
		print("Error in D/b")
	mydb.close()
	c=input("\n\n\n Press Any Key to Continuee....")
    
def view():
	system('cls')
	chh=''
	while chh!= 'x' or chh!='X':
		system('cls')
		print("\n\n\t\tVIEW MENU")
		print("\n S --> Single Student")
		print("\n A --> All Students")
		print("\n X --> Exit ")
		chh=input("\nEnter Your Choice...")
		if chh=='s' or chh=='S':
			print("\n\n\n \tStudent Data Record\n\n\n ")
			rn=int(input("Enter Roll NO to View "))
			mycur.execute("select * from stu where rn={}".format(rn))
			results = mycur.fetchall()
			for row in results:
				rn = row[0] #row[col no]
				lname = row[1]
				age = row[2]
				print ("Roll No : ",str(rn),"\n","Name : ",lname,"\n","Age : ", str(age))
			c=input("Press Any Key to Continuee....")
		elif chh=='a' or chh=='A':
			system('cls')
			print("\n\n\n \tStudent Data Record\n\n\n ")
			mycur.execute("select * from stu")
			results = mycur.fetchall()
			print("Roll NO\tName\t\t Age")
			for row in results:
				rn = row[0] #row[col no]
				lname = row[1]
				age = row[2]
				print (str(rn),"\t",lname,"\t",str(age))
			c=input("\n\n\nPress Any Key to Continuee....")
		elif chh=='x' or chh=='X':
			break           

    

#_main_
main()
