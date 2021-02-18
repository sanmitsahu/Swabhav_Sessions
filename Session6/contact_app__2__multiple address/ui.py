from data_access import add_contacts,search_contacts,showall_contacts,update_contacts,delete_contacts,update_address,search_address,delete_one_address,add_address,contact,address

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
					
				except Exception as e:
					print()
					print("Incorrect Data type . Contact Not Created")
					print()
					choice = input("Do you want to try again (y/n) ? ")
					
				else:
					returned_value = add_contacts(new_contact)
					choice_address = 'y'
					if returned_value==0:
						choice_address = 'n'
					while choice_address=='y':
						try:
							print("Add address for contact no => ",new_contact.contactno)
							address_obj = address()
							print("Enter address details => ")
							address_obj.street = input("Enter Street  : ")
							address_obj.city = input("Enter City  : ")
							address_obj.state = input("Enter State  : ")
							address_obj.country = input("Enter Country  : ")
						except Exception as e:
							print("Incorrect Datatype")
						else:
							add_address(address_obj,new_contact.contactno)
							print()
							choice_address = input("Do you want to add more addresses (y/n) ? ")
							print()
					print()
					choice = input("Do you want to add more contacts (y/n) ? ")

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
					records = search_contacts(contact_search)
					if records!=0:
						print("Record found !")
						print()
						print("Contact Details =>")
						print("First Name : ",records[0][0])
						print("Last Name : ",records[0][1])
						print("Contact Number : ",records[0][2])
						print("Age : ",records[0][3])
						print("Description : ",records[0][4])
						i = 1
						for record in records: 
							print()
							print("Address id => ",record[9])
							print("Street : ",record[5])
							print("City : ",record[6])
							print("State : ",record[7])
							print("Country : ",record[8])
							i += 1
					print()
					choice = input("Do you want to keep searching (y/n) ? ")

		elif menu_choice==3:
			records = showall_contacts()
			i = 1
			for record in records:
				print()
				print(f"Record {i}=> ")
				print("First Name : ",record[0])
				print("Last Name : ",record[1])
				print("Contact Number : ",record[2])
				print("Description : ",record[3])
				print("Age : ",record[4])
				print("Address id => ",record[9])
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
								new_contact.desciption = record[0][4]
							
							new_contact.age = (input("Enter Age  : "))
							if new_contact.age == "":
								new_contact.age = record[0][3]
							else:
								new_contact.age = int(new_contact.age)
						
						except Exception as e:
							print("Incorrect Datatype ! Contact not edited")
						else:
							update_contacts(contact_update, new_contact)

						choice_address = 'y'
						while choice_address=='y':
							try:
								print()
								print("Address update")
								print()
								new_address = address()
								id = int(input("Enter id of address : "))
								
							except Exception as e:
								print("Incorrect Datatype")
							else:
								record = search_address(contact_update,id)
								if record!=0:
									print(f"Enter new details for address {id} of contact {contact_update} => ")
									print("Press enter to keep old value")
									print()
									print("Enter address details => ")
								
									new_address.street = input("Enter Street  : ")
									if new_address.street == "":
										new_address.street = record[0][2]
									
									new_address.city = input("Enter City  : ")
									if new_address.city == "":
										new_contact.city = record[0][3]
									
									new_address.state = input("Enter State  : ")
									if new_address.state == "":
										new_address.state = record[0][4]
									
									new_address.country = input("Enter Country  : ")
									if new_address.country == "":
										new_address.country = record[0][5]

									update_address(contact_update,new_address,id)
							
							print()
							choice_address = input("Do you want to keep updating addresses(y/n) ? ")

					print()
					choice = input("Do you want to keep updating (y/n) ? ")
			
		
		elif menu_choice==5:
			choice = 'y'
			while choice=='y':
				try:
					contact_delete = int(input("Enter contact number to be Deleted : "))
					delete_choice = int(input("1. Delte All addresses and Contact\n2. Delete single address for contact\n"))
					
				except Exception as e:
					print("Incorrect Datatype")
					print()
					choice = input("Do you want to try again (y/n) ? ")
				else:
					if delete_choice == 1:
						delete_contacts(contact_delete)
					elif delete_choice == 2:
						try:
							id = int(input("Enter id of address to Delete : "))
						except Exception as e:
							print("Incorrect Datatype")
						delete_one_address(contact_delete,id)

					else:
						print("Incorrect choice")
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

#`Street` = "{new_contact.street}", `City`="{new_contact.city}", `State`="{new_contact.state}",
#		`Country`="{new_contact.country}"

							