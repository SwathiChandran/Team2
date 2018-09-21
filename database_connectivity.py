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



#reading csv file
def reading_csv():
    csv_name=raw_input("enter the csv file name:")
    csv_list=[]
    with open(csv_name,"rb") as f:
        reader=csv.reader(f,delimiter=",")
        for line in reader:
            csv_list.append(line)
        print(csv_list)
    f.close()


#Comparing table and csv 
def table_csv_comparing():
	csv_list=[]
	table_list = []
	database_name = raw_input('Enter the Database Name :')
	csv_name=raw_input("enter the csv file name:")
	database_name = database_name+".db"
	conn = sqlite3.connect(database_name)
	c= conn.cursor()
	table_values = c.execute("SELECT * FROM cricket")
	for i in table_values:
		table_list.append(list(i))
	print table_list
	
	with open(csv_name,"rb") as f:
		reader=csv.reader(f,delimiter=",")
		for line in reader:
			csv_list.append(line)
	print(csv_list)
	
	flag = 0
		for i in csv_list:
			if i in table_list:
				flag+=1
		print "Flag is :",flag
		if flag == len(table_list):
			print "True"
		else:
			print "False"
			
	f.close()
	conn.close()
	
sample=database_connectivity()
if sample:
		print "connection successfull"	
else:
		print "no"	
config_file_read()
reading_csv()
table_csv_comparing()
