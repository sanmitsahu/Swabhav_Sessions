from service import connect
con = connect()

class contact:
	fname = ""
	lname = ""
	contactno = 0
	description = ""
	age = ""

class address:
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
		return 0

	else:
		cursor = con.cursor()
		Query1 = f"""INSERT INTO `contact2` (Fname, Lname, Contact_no, Age,Description) 
   VALUES ("{new_contact.fname}", "{new_contact.lname}", "{new_contact.contactno}", {new_contact.age},"{new_contact.description}" )"""
		
		try:
			cursor.execute(Query1)
			con.commit()
		except Exception as e:
			print()
			print("Error occured !. Contact Number Already Present in Database")
			con.rollback()
			return 0
		else:
			print()
			print("Record added successfully !")
			print()
			return 1;
	

def add_address(address_add,contact_no):
	try:
		new_address = address()
		new_address = address_add
		
	except Exception as e:
		print()
		print("Error occured while adding address")
		return

	else:
		cursor = con.cursor()
		Query1 = f"""INSERT INTO `address_contact2` (Contact_no,Street, City, State, Country) 
   VALUES ({contact_no},"{new_address.street}", "{new_address.city}", "{new_address.state}", "{new_address.country}")"""
		
		try:
			cursor.execute(Query1)
			con.commit()
		except Exception as e:
			print()
			print("Error occured !.")
			con.rollback()
			return 
		else:
			print("Record added successfully !")
		

def search_contacts(search_no):
	try:
		contact_search = search_no
		cursor = con.cursor()
		Querysearch = f"""SELECT Fname,Lname,`contact2`.Contact_no,Age,Description,Street,City,State,Country,id FROM  `contact2` 
						  INNER JOIN `address_contact2`
						  ON `contact2`.Contact_no = `address_contact2`.Contact_no
						  WHERE `contact2`.`Contact_no`={contact_search};"""
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found !")
			return 0

	except Exception as e:
		print("Error occured during Search !",e)
		print()
		return 0
	
	else:
		return record

def search_address(search_no,id):
	try:
		contact_search = search_no
		cursor = con.cursor()
		Querysearch = f"""SELECT id,`address_contact2`.Contact_no,Street,City,State,Country FROM  `address_contact2` 
						  WHERE `address_contact2`.`Contact_no`={contact_search} AND `address_contact2`.id={id} ;"""
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found !")
			return 0

	except Exception as e:
		print("Error occured during Search !",e)
		print()
		return 0
	
	else:
		return record

def showall_contacts():
	try:
		cursor = con.cursor()
		Query1 = """SELECT Fname,Lname,`contact2`.Contact_no,Description,Age,Street,City,State,Country,id FROM  `contact2` 
					INNER JOIN `address_contact2`
					 ON `contact2`.Contact_no = `address_contact2`.Contact_no;"""
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
		Query1 = f"""UPDATE `contact2` SET `Fname`= "{new_contact.fname}", 
		`Lname` = "{new_contact.lname}",`Age`={new_contact.age}, `Description` = "{new_contact.description}"
		WHERE `Contact_no`={contact_update} """
		cursor.execute(Query1)
		con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not Updated",e)
		print()
		return 0
	
	
	else:
		print("Record Updated Successfully !") 
		
def update_address(contact_update, updateobj,id):
	try:
		cursor = con.cursor()
		new_address = contact()
		new_address = updateobj
		Query1 = f"""UPDATE `address_contact2` SET `Street`= "{new_address.street}", 
		`City` = "{new_address.city}",`State`="{new_address.state}", `Country` = "{new_address.country}"
		WHERE `Contact_no`={contact_update} AND `id`={id}"""
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
		Querysearch = f"""SELECT * FROM  `contact2` WHERE `Contact_no`={contact_delete} """
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found")
			return
		else:
			Query1 = f"""DELETE FROM `contact2` WHERE `Contact_no`={contact_delete}"""
			cursor.execute(Query1)
			con.commit()
			Query2 = f"""DELETE FROM `address_contact2` WHERE `Contact_no`={contact_delete}"""
			cursor.execute(Query2)
			con.commit()

	except Exception as e:
		con.rollback()
		print("Error occured ! Record not deleted")
		print()
		return
		
	else:
		print("Record deleted Successfully !") 
		

	
def delete_one_address(del_no,id):
	try:
		contact_delete = del_no
		cursor = con.cursor()
		Querysearch = f"""SELECT * FROM  `address_contact2` WHERE `Contact_no`={contact_delete} AND `id`={id}"""
		cursor.execute(Querysearch)
		record = cursor.fetchall()
		if len(record)<1:
			print("No such record found")
			return
		else:
			Query2 = f"""DELETE FROM `address_contact2` WHERE `Contact_no`={contact_delete} AND `id`={id}"""
			cursor.execute(Query2)
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
