import re

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

## print rows[0][0].strip().split()

while i < (len(rows)):
	try:
		cur_instance = [ int(rows[i][2].strip().split()[0][1:-1]) ]
		cur_date = [ rows[0][0].strip().split()[4] + " " + rows[0][0].strip().split()[5] ]
		cur_type = [ rows[0][0].strip().split()[3] ]
		if( (rows[0][1].strip().split()[0][0] == '*') or (rows[0][1].strip().split()[0][0] == '.') ):
			cur_ne = [ rows[0][1].strip().split()[2] + " " + rows[0][1].strip().split()[3] + " " + rows[0][1].strip().split()[4] ]
		else:
			cur_ne = [ rows[0][1].strip().split()[1] + " " + rows[0][1].strip().split()[2] + " " + rows[0][1].strip().split()[3] ]
		cur_alarm_no = [ rows[0][2].strip().split()[1] ]
		cur_desc = [ rows[0][2].strip().split()[2] + " " + rows[0][2].strip().split()[3] + " " + rows[0][2].strip().split()[4] ]
		cur_supp_info = [ rows[0][3].strip().split()[0] + " " + rows[0][3].strip().split()[1] + " " + rows[0][3].strip().split()[2] ]
		# cur_cancle_time = 
		if( (rows[0][1].strip().split()[0][0] == '*') or (rows[0][1].strip().split()[0][0] == '.') ):
			cur_star_rating = [ rows[0][1].strip().split()[0] ]
		else:
			cur_star_rating = [""]
		instance += [cur_instance]
		date += [cur_date]
		alarm_type += [cur_type]
		ne += [cur_ne]
		alarm_no += [cur_alarm_no]
		desc += [cur_desc]
		supp_info += [cur_supp_info]
		# cancel_time += [cur_cancle_time]
		star_rating += [cur_star_rating]
		i += 1
	except:
		rows = rows[:i]+rows[i+1:]

## print instance
## print date
