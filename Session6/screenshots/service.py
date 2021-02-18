import mysql.connector as mysql

def connect():
	try:
		con = mysql.connect(user='root',password="",host='127.0.0.1',database='swabhav')
		status = str(con.is_connected())
		cursor = con.cursor()
		if status=="True":
			#print(con)
			return con
		
	except Exception as e:
		print("Connection Error : ",e)
		exit()

	finally:
		pass
