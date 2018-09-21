import sqlite3
def database_connectivity():
	database_name = raw_input('Enter the Database Name :')
	database_name = database_name+".db"
	conn = sqlite3.connect(database_name)
	c= conn.cursor()
	table_values = c.execute("SELECT * FROM movie")
	for i in table_values:
		print i
	return conn

sample=database_connectivity()
if sample:
		print "connection successfull"	
else:
		print "no"