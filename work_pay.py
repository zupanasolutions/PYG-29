#Import the datetime module
import datetime

#Import the excel module in python with a workbook
import xlwt 
from xlwt import Workbook 
  
#Workbook is created 
wb = Workbook() 

# Specifying style 
style = xlwt.easyxf('font: bold 1') 
  
# Use add_sheet to create sheet. 
working_hour_sheet = wb.add_sheet('Working_Hours') 

working_hour_sheet.write(0, 0, 'Start_Date_Time', style)
working_hour_sheet.write(0, 1, 'End_Date_Time', style)
working_hour_sheet.write(0, 2, 'Pay_Amount_Due', style)


print('Enter the start date by following the prompts below:\n')

year = int(input('Enter a year:\t'))
month = int(input('Enter a month:\t'))
day = int(input('Enter a day:\t'))
hour = int(input('Enter an Hour:\t'))
minute = int(input('Enter an Minute:\t'))
second = int(input('Enter an Second:\t'))

start_date = datetime.datetime(year, month, day, hour, minute, second)


print('Enter the end date by following the prompts below:\t')

year = int(input('Enter a year:\t'))
month = int(input('Enter a month:\t'))
day = int(input('Enter a day:\t'))
hour = int(input('Enter an Hour:\t'))
minute = int(input('Enter an Minute:\t'))
second = int(input('Enter an Second:\t'))

end_date = datetime.datetime(year, month, day, hour, minute, second)
diff = end_date-start_date

diff_seconds = diff.seconds/60
diff_date_hours = diff_seconds/60

gross_pay = 5*diff_date_hours
gross_pay = '${}'.format(gross_pay)

#Write the details to excel file
working_hour_sheet.write(1, 0, start_date, style)
working_hour_sheet.write(1, 1, end_date, style)
working_hour_sheet.write(1, 2, gross_pay, style)

#Save the workbook
wb.save('xlwt work.xls')

#Print the resulst
print('You have worked for a total of {} hours on this task '.format(diff_date_hours))
print('Your total pay for working from {} to {} is ${} '.format(start_date, end_date, gross_pay))



 