# Key assumptions:
    # Hours can be taken for dates before or after the current date
    # Hours do not run over from one day to the other, ie, night shifts from one day to the next Hours can only be entered for one day from 00:00 to 11:59
    # Hours are taken in 24 hour format 
    # There is not check for duplicate logs, ie, logging in the same hours more than once



from datetime import datetime, timedelta
import xlsxwriter

#set default wage per hour so it can be easily changed without altering function
WAGE_PER_HOUR = 5.00

total_hours = 0
total_wages = 0.00


def calculateWages(num_hours):
    wages = num_hours * WAGE_PER_HOUR
    print("You earned $", wages)
    return wages

def determineHours(start_time, end_time):
    total_hours = ((end_time - start_time).seconds)/3600
    print("You worked for ", total_hours, " hours.")
    return total_hours

def getDate():
    date_accepted = False
    while(not date_accepted):
        try:
            date = input("Enter the date you worked (DD/MM/YYYY): ")
            # convert date to datetime object
            date = datetime.strptime(date, "%d/%m/%Y")
            date_accepted = True
        except ValueError:
            print("Enter a valid date in the format DD/MM/YYYY")
    return date

def getTime():
    start_time_accepted = False
    end_time_accepted = False

    while(not start_time_accepted):
        try:
            start_time = input("Start time (e.g.: 12:00): ")
            start_time = datetime.strptime(start_time, "%H:%M")
            start_time_accepted = True
        except ValueError:
            print("Enter a valid time in 24-hour format as HH:MM")

    while (not end_time_accepted):
        try:
            end_time = input("End time (e.g.: 12:00): ")
            end_time = datetime.strptime(end_time, "%H:%M")
            if end_time <= start_time:
                print("End time should not be before or equal to start time")
            else:
                end_time_accepted = True
        except ValueError:
            print("Enter the time in the format HH:MM")
    
    return start_time, end_time


def recordLogs(): 

    global total_hours
    global total_wages

    #set today's date as the default date
    date = datetime.now()
    logs = []

    keep_asking = True
    while(keep_asking):
        record_more_hours = input("\nDo you have hours to add (y/n)? ")
        try:

            if (record_more_hours == "n"):
                keep_asking = False
            elif (record_more_hours == "y"):
                confirm_date = input("Are you entering hours for today (y/n)? ")
                if (confirm_date == "y"):
                    start_time, end_time = getTime()
                elif (confirm_date == "n"):
                    date = getDate()
                    start_time, end_time = getTime()
                else:
                    raise ValueError("I do not understand that command. Please enter 'y' or 'n'")
                start_date_time = datetime.combine(date, start_time.time())
                end_date_time = datetime.combine(date, end_time.time())
                hours = determineHours(start_date_time, end_date_time)
                total_hours += hours
                wages = calculateWages(hours)
                total_wages += wages
                log = (date.strftime('%m/%d/%Y'), start_time.time().strftime('%H:%M'), end_time.time().strftime('%H:%M'), hours, "{:.2f}".format(wages))                
                print(log)
                logs.append(log)
            else:
                raise ValueError("I do not understand that command. Please enter 'y' or 'n'")
    
        except ValueError:
            print("Enter 'y' or 'n")
    
    return logs
        

def main():
    wb = xlsxwriter.Workbook('salary_tracker.xlsx') 
    worksheet = wb.add_worksheet()
    bold_format = wb.add_format({'bold': True})
    
    #add headers
    header = ['Date', 'Start Time', 'End Time', 'Hours Worked', 'Wages Earned ($)'] 
    for i in range(len(header)):
        worksheet.write(0, i, header[i], bold_format)

    print("\nWelcome to the time tracker. Enter the hours you have worked to calculate how much wages you have earned.")
    print("---------------------------------------------------------------------------------------------------------\n")
 
    logs = recordLogs()
   
    if (logs):
        for row, line in enumerate(logs):
            for col, cell in enumerate(line):
                worksheet.write(row+1, col, cell)
        # write totals
        totals_row = ['TOTAL', '', '', total_hours, '{:.2f}'.format(total_wages)] 
        for i in range(len(totals_row)):
            worksheet.write(row+1, i, totals_row[i], bold_format)

    #close the workbook
    wb.close()
    print("\n\n---------------------------------------------------------------------------------------------------------")
    print("Thank you for using this program. Goodbye!\n")
    

main()
