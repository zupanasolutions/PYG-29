### Naa Lamle version

from datetime import datetime, timedelta


def calculateWages(num_hours):
    return num_hours * 5

def determineHours(start_time, end_time):
    return end_time - start_time

def getDate():
    #set today's date as the default date
    date = datetime.now().strftime("%d/%m/%Y")

    date_accepted = False
    while(not date_accepted):
        try:
            date = input("Enter the date you worked (DD/MM/YYY): ")
            # convert date to datetime object
            date = datetime.strptime(date, "%d/%m/%Y")
            date_accepted = True
            print(date)
        except ValueError:
            print("Enter a valid date in the format DD/MM/YYYY")
    return date

def getTime():
    #set default start time to current time and end time to one hour from now
    start_time = datetime.now().strftime("%H:%M")
    end_time = '{:%H:%M}'.format(datetime.now() + timedelta(hours=1))

    start_time_accepted = False
    end_time_accepted = False

    while(not start_time_accepted):
        try:
            start_time = input("Start time (e.g.: 12:00): ")
            start_time = datetime.strptime(start_time, "%H:%M")
            start_time_accepted = True
        except ValueError:
            print("Enter the time in the format HH:MM")

    while (not end_time_accepted):
        try:
            end_time = input("End time (e.g.: 12:00): ")
            end_time = datetime.strptime(end_time, "%H:%M")
            if end_time < start_time:
                print("End time should not be before start time")
            else:
                end_time_accepted = True
        except ValueError:
            print("Enter the time in the format HH:MM")
    
    print("Start:", start_time, "End:", end_time)
    return start_time, end_time


def getInput(): 
    keep_asking = True
    while(keep_asking):
        record_more_hours = input("\nDo you have hours to add (y/n)? ")
        try:

            if (record_more_hours == "n"):
                keep_asking = False
            elif (record_more_hours == "y"):
                confirm_date = input("Are you entering hours for today (y/n)? ")
                if (confirm_date == "y"):
                    print("using today's date")
                    getTime()
                elif (confirm_date == "n"):
                    print("will ask for date")
                    date = getDate()
                    start_time, end_time = getTime()
                else:
                    raise ValueError("I do not understand that command. Please enter 'y' or 'n'")
            else:
                raise ValueError("I do not understand that command. Please enter 'y' or 'n'")
        
        except ValueError:
            print("Enter 'y' or 'n")
    
        

def main():
    print("Welcome to the time tracker. Enter the hours you have worked to calculate how much wages you have earned.")
    print("---------------------------------------------------------------------------------------------------------\n")
    getInput()
    print("\n\n---------------------------------------------------------------------------------------------------------")
    print("Thank you for using this program. Goodbye!")
    



main()