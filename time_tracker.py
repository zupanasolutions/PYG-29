### Naa Lamle version

from datetime import datetime


def calculateWages(num_hours):
    return num_hours * 5

def determineHours(start_time, end_time):
    return end_time - start_time

def getDateAndTime():
    #set today's date as the default date
    default_date = datetime.now().strftime("%d/%m/%Y")

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
                elif (confirm_date == "n"):
                    print("will ask for date")
                    getDateAndTime()
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