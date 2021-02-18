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
		new_contact = contact()
		new_contact = mycontact
		
	except Exception as e:
		print()
		print("Error occured while adding contact")
		return

	else:
		cursor = con.cursor()
		Query1 = f"""INSERT INTO `contact1` (Fname, Lname, Contact_no, Description, Age, Street, City, State, Country) 
   VALUES ("{new_contact.fname}", "{new_contact.lname}", "{new_contact.contactno}", "{new_contact.description}", {new_contact.age}
   , "{new_contact.street}", "{new_contact.city}", "{new_contact.state}", "{new_contact.country}")"""
		
		try:
			cursor.execute(Query1)
			con.commit()
		except Exception as e:
			print()
			print("Error occured !. Contact Number Already Present in Database")
			con.rollback()
			return 
		else:
			print("Record added successfully !")
	
	
	

def search_contacts(search_no):
	#pass
	try:
		contact_search = search_no
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `contact1` WHERE `Contact_no`={contact_search} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found !")
			return 0

	except Exception as e:
		print("Error occured during Search !")
		print()
		return 0
	
	else:
		return record

	

def showall_contacts():
	try:
		cursor = con.cursor()
		Query1 = """SELECT * from contact1"""
		cursor.execute(Query1)
		records = cursor.fetchall()
		

	except Exception as e:
		print("Error No data found")
	else:
		return records

def update_contacts(contact_update, updateobj):
	try:
		cursor = con.cursor()
		new_contact = contact()
		new_contact = updateobj
		##print(f"{new_contact.fname}  {new_contact.lname}  {new_contact.contactno} {new_contact.desciption}")
		Query1 = f"""UPDATE `contact1` SET `Fname`= "{new_contact.fname}", 
		`Lname` = "{new_contact.lname}", `Description` = "{new_contact.description}", `Age`={new_contact.age},
		`Street` = "{new_contact.street}", `City`="{new_contact.city}", `State`="{new_contact.state}",
		`Country`="{new_contact.country}" WHERE `Contact_no`="{contact_update}" """
		cursor.execute(Query1)
		con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not Updated",e)
		print()
		return 0
	
	
	else:
		print("Record Updated Successfully !") 
		


def delete_contacts(del_no):
	try:
		contact_delete = del_no
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `contact1` WHERE `Contact_no`={contact_delete} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found")
			return
		else:
			Query1 = f"""DELETE FROM `contact1` WHERE `Contact_no`={contact_delete}"""
			cursor.execute(Query1)
			con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not deleted")
		print()
		return
	
	
	else:
		print("Record deleted Successfully !") 
		

	

#update_contacts()
#search_contacts()
#delete_contacts()
#add_contacts()
#showall_contacts()
