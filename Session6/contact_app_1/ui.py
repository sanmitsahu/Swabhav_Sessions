from data_access import add_contacts,search_contacts,showall_contacts,update_contacts,delete_contacts,contact

def contact_app_controller():
	try:
		print()
		menu_choice = int(input("""Contact List App.\nMENU =>
		1. Add Contact
		2. Search Contact 
		3. Show All contacts
		4. Update Contacts
		5. Delete Contact\n"""))
	except Exception as e:
		print("Incorrect option chosen !")
		want_to_retry = input("Want to try again (y/n) ?")
		if want_to_retry=='y':
			contact_app_controller()

	else:

		if menu_choice==1:
			choice = 'y'
			while choice=='y':
				try:
					new_contact = contact()
					print()
					print("Creating new contact .")
					print("Please enter contact details => ")
					new_contact.fname = input("Enter First Name  : ")
					new_contact.lname = input("Enter Last Name  : ")
					new_contact.contactno = int(input("Enter Contact Number  : "))
					new_contact.desciption = input("Enter person's Desciption  : ")
					new_contact.age = int(input("Enter Age  : "))
					print("Enter address details => ")
					new_contact.street = input("Enter Street  : ")
					new_contact.city = input("Enter City  : ")
					new_contact.state = input("Enter State  : ")
					new_contact.country = input("Enter Country  : ")
				except Exception as e:
					print()
					print("Incorrect Data type . Contact Not Created")
					print()
					choice = input("Do you want to try again (y/n) ? ")
					
				else:
					choice='n'
					add_contacts(new_contact)
					print()
					choice = input("Want to keep adding contacts(y/n) ? ")


		elif menu_choice==2:
			choice = 'y'
			while choice=='y':
				try:
					print()
					contact_search = int(input("Enter contact number to be searched : "))
				except Exception as e:
					print("Incorrect Datatype")
					print()
					choice = input("Do you want to try again (y/n) ? ")
				else:
					record = search_contacts(contact_search)
					if record!=0:
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

					print()
					choice = input("Do you want to keep searching (y/n) ? ")

		elif menu_choice==3:
			records = showall_contacts()
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

		elif menu_choice==4:
			choice = 'y'
			while choice=='y':
				try:
					contact_update = int(input("Enter contact number to be Updated : "))
				except Exception as e:
					print("Incorrect Datatype")
					print()
					choice = input("Do you want to try again (y/n) ? ")
				else:
					#ask for new data
					record = search_contacts(contact_update)
					if record !=0:
						try:
							new_contact = contact()
							print("Enter new details for contact : ",contact_update)
							print("Press enter to keep old value")
							
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
						
						except Exception as e:
							print("Incorrect Datatype")
						else:
							update_contacts(contact_update, new_contact)

					print()
					choice = input("Do you want to keep updating (y/n) ? ")
			
		
		elif menu_choice==5:
			choice = 'y'
			while choice=='y':
				try:
					contact_delete = int(input("Enter contact number to be Deleted : "))
				except Exception as e:
					print("Incorrect Datatype")
					print()
					choice = input("Do you want to try again (y/n) ? ")
				else:
					delete_contacts(contact_delete)
					print()
					choice = input("Do you want to keep deleting (y/n) ? ")


		else:
			print("Incorrect choice !")

		print()
		want_to_continue = input("Want to continue managing Contacts (y/n) ?")
		if want_to_continue=='y':
			contact_app_controller()
	
if __name__ == "__main__":
	contact_app_controller()