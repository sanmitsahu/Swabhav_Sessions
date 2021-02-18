import mysql.connector as mysql

try:
	con = mysql.connect(user='root',password="",host='127.0.0.1',database='world')
	print("connected : "+str(con.is_connected()))
	cursor = con.cursor()
	Query1 = """SELECT * from country"""
	cursor.execute(Query1)
	records = cursor.fetchall()
	print("Total rows are:  ", len(records))
	for record in records:
		print("Country : ",record)
except Exception as e:
	print(e)

finally:
	print("finally")
	print(con)
	if con.is_connected():
		con.close()
	print("Connection closed")

print("end")
print(con)
