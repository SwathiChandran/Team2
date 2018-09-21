
#import config as conf
import ConfigParser
import csv
import sqlite3

"""
Creating a class named Database with four methods namely __init__(),decorator_fun(),table(),comparision()
"""


class Database:
    """
    Called on object ceation for Database Class
    """

    def __init__(self):
        database_name = raw_input('Enter the Database Name :')
        database_name = database_name + ".db"
        self.conn = sqlite3.connect(database_name)
        self.c = self.conn.cursor()
        try:
            # Reading configuration.ini file
            self.config = ConfigParser.ConfigParser()
            config_location = raw_input(
                'Enter the Configuration file location :')
            self.config.read(config_location)
        except Exception as error:
            print error
    """
    Decorator Method
	"""

    def decorator_fun(self, func, name):
        print "==============================="
        print name
        print "==============================="
        func()

    """
    Used to fetch data from tables and CSV and will call comparision()
	"""

    def table(self):
        try:
            # Reading sections in ini file
            table_section = self.config.sections()

            for i in table_section:
                table_src = self.config.get(i, 'table_src')
                self.csv_name = self.config.get(i, 'table_tgt')
                self.table_values = self.c.execute(
                    "SELECT * FROM '{}'".format(table_src))
                self.comparision(i)
        except Exception as error:
            print error
        finally:
            self.conn.close()

    """
	compares Table values and CSV values and writes the result to "Test_Results.csv" file
	"""

    def comparision(self, sec_name):
        self.csv_list = []
        self.table_list = []
        flag = 0
        with open(self.csv_name, "rb") as f_csv:
            self.reader = csv.reader(f_csv, delimiter=",")
            self.csv_list = [line for line in self.reader]
        f_csv.close()
        self.table_list = [list(i) for i in self.table_values]
        if (len(self.csv_list) == len(self.table_list)):
            for i in self.csv_list:
                if i in self.table_list:
                    flag += 1
            if flag == len(self.table_list):
                print sec_name + " " + " =>Pass -- Same Records in Table and CSV"
                with open('Test_Results.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow([sec_name, "Pass"])
                csvFile.close()
            else:
                print sec_name + " " + " =>Fail -- Mismatch Records in Table and CSV"
                with open('Test_Results.csv', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow([sec_name, "Fail"])
                csvFile.close()
        else:
            print sec_name + " " + " =>Fail -- Different Record Lengths in Table and CSV"
            with open('Test_Results.csv', 'a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([sec_name, "Fail"])
            csvFile.close()


if __name__ == "__main__":
    obj = Database()
    obj.decorator_fun(obj.table, "Comparing Tables and CSV Files")
