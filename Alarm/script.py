import csv

filename = "./Alarm history/BSC_Alarm_history1.txt"
files = open(filename,"r")

## x = 0

instance = []
date = []
alarm_type = []
ne = []
alarm_no = []
desc = []
supp_info = []
cancel_time = []
star_rating = []
new_type = []

rows = []

lines = []

for line in files:
	if line.strip()	== "":
		rows += [lines]
		lines = []
	else:
		lines += [line]
##	if (x==0):
##		break

i = 0

## print rows[i][0].strip().split()

while i < (len(rows)):
	try:
		cur_instance = [ int(rows[i][2].strip().split()[0][1:-1]) ]
		cur_date = [ rows[i][0].strip().split()[4] + " " + rows[i][0].strip().split()[5] ]
		cur_type = [ rows[i][0].strip().split()[3] ]
		if( (rows[i][1].strip().split()[0][0] == '*') or (rows[i][1].strip().split()[0][0] == '.') ):
			cur_ne = [ rows[i][1].strip().split()[2] + " " + rows[i][1].strip().split()[3] + " " + rows[i][1].strip().split()[4] ]
		else:
			cur_ne = [ rows[i][1].strip().split()[1] + " " + rows[i][1].strip().split()[2] + " " + rows[i][1].strip().split()[3] ]
		cur_alarm_no = [ rows[i][2].strip().split()[1] ]
		cur_desc = [ rows[i][2].strip().split()[2] + " " + rows[i][2].strip().split()[3] + " " + rows[i][2].strip().split()[4] ]
		cur_supp_info = [ rows[i][3].strip().split()[0] + " " + rows[i][3].strip().split()[1] + " " + rows[i][3].strip().split()[2] ]
		# cur_cancle_time = 
		if( (rows[i][1].strip().split()[0][0] == '*') or (rows[i][1].strip().split()[0][0] == '.') ):
			cur_star_rating = [ rows[i][1].strip().split()[0] ]
		else:
			cur_star_rating = [""]
		if( (rows[i][1].strip().split()[0][0] == '*') or (rows[i][1].strip().split()[0][0] == '.') ):
			cur_new_type = [ rows[i][1].strip().split()[1] ]
		else:
			cur_new_type = [ rows[i][1].strip().split()[0] ]
		instance += cur_instance
		date += cur_date
		alarm_type += cur_type
		ne += cur_ne
		alarm_no += cur_alarm_no
		desc += cur_desc
		supp_info += cur_supp_info
		# cancel_time += cur_cancle_time
		star_rating += cur_star_rating
		new_type += cur_new_type
		i += 1
	except:
		rows = rows[:i]+rows[i+1:]

records = {}

## print new_type

##print len(instance)
##print len(date)
##print len(alarm_type)
##print len(ne)
##print len(alarm_no)
##print len(desc)
##print len(supp_info)
####print len(cancel_time)
##print len(star_rating)
##print len(new_type)

for i in range(len(alarm_no)):
	records[instance[i]] = {}
	records[instance[i]]['alarm_no'] = alarm_no[i]
	records[instance[i]]['alarm_type'] = alarm_type[i]
	records[instance[i]]['ne'] = ne[i]
	records[instance[i]]['desc'] = desc[i]
	records[instance[i]]['supp_info'] = supp_info[i]
	records[instance[i]]['star_rating'] = star_rating[i]
	##records[instance[i]]['start'] = ""
	##records[instance[i]]['end'] = ""

for i in range(len(alarm_no)):
	if(new_type[i] == 'ALARM'):
		records[instance[i]]['start'] = date[i]
	elif(new_type[i] == 'CANCEL'):
		records[instance[i]]['end'] = date[i]

##print new_type
##print records

s = "Instance, Start Time, Type, NE, Alarm No, Description, Supp Info, Cancle Time, Star Rating"

for key, value in records.iteritems():
	try:
		temp = "\n" + str(key) + "," + str(value['start']) + "," + str(value['alarm_type']) + ","  + str(value['ne']) + ","  + str(value['alarm_no']) + ","  + str(value['desc']) + ","  + str(value['supp_info']) + ","  + str(value['end']) + ","  + str(value['star_rating'])
		s += temp
	except:
		continue

print s

## print instance
## print date
