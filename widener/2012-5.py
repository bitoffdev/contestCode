#Complete in 59 minutes and 37 seconds on November 11, 2013
import math
def getmin(minutes, hour, day, month, year): #hour is 0-23, month is 1-12
	time_from_years = (year-1)*525600+(math.floor((year-1)/4)-(math.floor((year-1)/100)-math.floor((year-1)/400)))*24*60 #normal year + leap year day
	if isleapyear(year): time_from_year = sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month-1])*24*60
	else: time_from_year = sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month-1])*24*60
	time_since_month_start = (day-1)*24*60 + hour*60 + minutes
	return time_from_years+time_from_year+time_since_month_start
def isleapyear(year):
	return year%4==0 and (year%400 == 0 or year%100 != 0)

#Define variables
cycletime = 42524 #cycle in minutes
todayphase = ""
phases = [
	0, #New Moon
	3*24*60+16*60+35, #Waxing Crescent - 5315
	7*24*60+9*60+11, #First Quater - 10631
	11*24*60+1*60+46, #Waxing Gibbous - 15946
	14*24*60+18*60+22, #Full Moon - 21262
	18*24*60+10*60+58, #Waning Gibbous - 26578
	22*24*60+3*60+33, #Third Quarter
	25*24*60+20*60+9, #Waning Crescent
	29*24*60+12*60+44 #Next New Moon
	]
phasenames = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", "Full Moon", "Waning Gibbous", "Third Quarter", "Waning Crescent", "Next New Moon"]
#Main program
inputmonth, inputday, inputyear = map(int, raw_input().split())
timepast = getmin(0, 0, inputday, inputmonth, inputyear) - getmin(23, 12, 25, 12, 2000)
timeSinceCycleStart = timepast%cycletime
print timeSinceCycleStart
for i in range(len(phases)):
	if timeSinceCycleStart<=phases[i]<timeSinceCycleStart+24*60:
		if i==len(phasenames)-1: i=0
		todayphase = phasenames[i]
if todayphase == "":
	for i in range(len(phases)-1):
		if phases[i]<timeSinceCycleStart<phases[i+1]:
			print "Between %s and %s" %(phasenames[i], phasenames[i+1])
else:
	print todayphase