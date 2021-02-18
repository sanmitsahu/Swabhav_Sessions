from service import connect
con = connect()

class contact:
	fname = ""
	lname = ""
	contactno = 0
	description = ""
	age = ""
	street = ""
	city = ""
	state = ""
	country = ""


def add_contacts(mycontact):
	try:
		new_contact = contact(mycontact)
		
		#print(f"{new_contact.fname}  {new_contact.lname}  {new_contact.contactno} {new_contact.desciption}")
		#print(f"{new_contact.age} {new_contact.street} {new_contact.city}  {new_contact.state} {new_contact.country}")
	except Exception as e:
		print()
		print("Error occured while adding contact")

	else:
		cursor = con.cursor()
		Query1 = f"""INSERT INTO `contact1` (Fname, Lname, Contact_no, Description, Age, Street, City, State, Country) 
   VALUES ("{new_contact.fname}", "{new_contact.lname}", "{new_contact.contactno}", "{new_contact.desciption}", {new_contact.age}
   , "{new_contact.street}", "{new_contact.city}", "{new_contact.state}", "{new_contact.country}")"""
		
		try:
			cursor.execute(Query1)
			con.commit()
		except Exception as e:
			print()
			print("Error occured !. Contact Number Already Present in Database")
			con.rollback()
			print()
			choice = input("Do you want to try again (y/n) ? ")
			if choice=='y':
				print()
				add_contacts()
		else:
			print("Record added successfully !")
	
	#showall_contacts()
	
	
	

def search_contacts():
	#pass
	try:
		contact_search = int(input("Enter contact number to be searched : "))
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `contact1` WHERE `Contact_no`={contact_search} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found !")
			raise NameError("No such record found!")

	except Exception as e:
		print("Error occured during Search !")
		print()
		choice = input("Do you want to try again (y/n)? ")
		if choice=='y':
			print()
			search_contacts()
	
	else:
		print("Record found !")
		print()
		print("First Name : ",record[0][0])
		print("Last Name : ",record[0][1])
		print("Contact Number : ",record[0][2])
		print("Description : ",record[0][3])
		print("Age : ",record[0][4])
		print("Street : ",record[0][5])
		print("City : ",record[0][6])
		print("State : ",record[0][7])
		print("Country : ",record[0][8])


	

def showall_contacts():
	try:
		cursor = con.cursor()
		Query1 = """SELECT * from contact1"""
		cursor.execute(Query1)
		records = cursor.fetchall()
		

	except Exception as e:
		print("Error No data found")
	else:
		i = 0
		for record in records:
			print()
			print(f"Contact {i}=> ")
			print("First Name : ",record[0])
			print("Last Name : ",record[1])
			print("Contact Number : ",record[2])
			print("Description : ",record[3])
			print("Age : ",record[4])
			print("Street : ",record[5])
			print("City : ",record[6])
			print("State : ",record[7])
			print("Country : ",record[8])
			i+=1
	finally:
		pass

def update_contacts():
	try:
		contact_update = int(input("Enter contact number to be Updated : "))
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `contact1` WHERE `Contact_no`={contact_update} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found")
			raise NameError("No such record found!")
		else:
			print("Enter new details for contact : ",record[0][2])
			print("Press enter to keep old value")
			new_contact = contact()
			new_contact.fname = input("Enter First Name  : ")
			if new_contact.fname == "":
				new_contact.fname = record[0][0]
			new_contact.lname = input("Enter Last Name  : ")
			if new_contact.lname == "":
				new_contact.lname = record[0][1]
			new_contact.desciption = input("Enter person's Desciption  : ")
			if new_contact.desciption == "":
				new_contact.desciption = record[0][3]
			new_contact.age = (input("Enter Age  : "))
			if new_contact.age == "":
				new_contact.age = record[0][4]
			else:
				new_contact.age = int(new_contact.age)
			print("Enter address details => ")
			new_contact.street = input("Enter Street  : ")
			if new_contact.street == "":
				new_contact.street = record[0][5]
			new_contact.city = input("Enter City  : ")
			if new_contact.city == "":
				new_contact.city = record[0][6]
			new_contact.state = input("Enter State  : ")
			if new_contact.state == "":
				new_contact.state = record[0][7]
			new_contact.country = input("Enter Country  : ")
			if new_contact.country == "":
				new_contact.country = record[0][8]
			##print(f"{new_contact.fname}  {new_contact.lname}  {new_contact.contactno} {new_contact.desciption}")
			Query1 = f"""UPDATE `contact1` SET `Fname`= "{new_contact.fname}", 
			`Lname` = "{new_contact.lname}", `Description` = "{new_contact.desciption}", `Age`={new_contact.age},
			`Street` = "{new_contact.street}", `City`="{new_contact.city}", `State`="{new_contact.state}",
			`Country`="{new_contact.country}" WHERE `Contact_no`="{contact_update}" """
			cursor.execute(Query1)
			con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not Updated",e)
		print()
		choice = input("Do you want to try again (y/n)? ")
		if choice=='y':
			print()
			update_contacts()
	
	
	else:
		print("Record Updated Successfully !") 
		


def delete_contacts():
	try:
		contact_delete = int(input("Enter contact number to be Deleted : "))
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `contact1` WHERE `Contact_no`={contact_delete} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found")
			raise NameError("No such record found!")
		else:
			Query1 = f"""DELETE FROM `contact1` WHERE `Contact_no`={contact_delete}"""
			cursor.execute(Query1)
			con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not deleted")
		print()
		choice = input("Do you want to try again (y/n)? ")
		if choice=='y':
			print()
			delete_contacts()
	
	
	else:
		print("Record deleted Successfully !") 
		

	

#update_contacts()
#search_contacts()
#delete_contacts()
#add_contacts()
#showall_contacts()
