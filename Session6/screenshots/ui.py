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
					if choice=='y':
						print()
						add_contacts()
				else:
					choice='n'
					add_contacts(new_contact)


		elif menu_choice==2:
			search_contacts()
		elif menu_choice==3:
			showall_contacts()
		elif menu_choice==4:
			update_contacts()
		elif menu_choice==5:
			delete_contacts()
		else:
			print("Incorrect choice !")

		print()
		want_to_continue = input("Want to continue (y/n) ?")
		if want_to_continue=='y':
			contact_app_controller()
	

contact_app_controller()