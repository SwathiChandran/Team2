import ConfigParser
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