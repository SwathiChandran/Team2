import sqlite3
import ConfigParser
def database_connectivity():
	try:
		database_name = raw_input('Enter the Database Name :')
		database_name = database_name+".db"
		conn = sqlite3.connect(database_name)
		c= conn.cursor()
		table_values = c.execute("SELECT * FROM movie")
		for i in table_values:
			print i
		return conn
	except Exception as error:
		print error
sample=database_connectivity()
if sample:
		print "connection successfull"	
else:
		print "no"
		
# configuration file reading	 	

def config_file_read():
	try:
		config = ConfigParser.ConfigParser()
		config_location = raw_input('Enter the Configuration file location :')
		config.read(config_location)
		table_src = config.get('test1','table_src')
		csv_name = config.get('test1','table_tgt')

		print "Source Table :",table_src
		print "Target File Name :",csv_name

	except Exception as error:
		print error

config_file_read()