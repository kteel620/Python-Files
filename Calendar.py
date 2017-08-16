'''Program that lets a user interact with a calendar-like app.'''

from time import sleep, strftime

const_var = 'Keshav'

calendar = {}


def welcome():
    print("Welcome to the calendar, " + const_var)
    sleep(1.0)
    print(strftime("%A, %B %d %Y"))
    print(strftime("%I:%M:%S %p"))
    sleep(1)
    print("What would you like to do? ")


def start_calendar():
    welcome()
    start = True
    while (start):
        user_choice = input("Enter 'A' to Add, 'U' to Update, 'V' to View, 'D' to Delete, or 'X' to Exit ")

        if (user_choice == 'V' or user_choice == 'v'):
            if (len(calendar.keys()) < 1):
                print('The calendar is empty.')
            else:
                print(calendar)

        elif (user_choice == 'U' or user_choice == 'u'):
            date = input("What date?")
            update = input("Enter the update: ")
            calendar[date] = update
            print("Update successful.")
            print(calendar)

        elif (user_choice == 'A' or user_choice == 'a'):
            event = input("Enter event: ")
            date = input("Enter date (MM/DD/YYYY): ")
            year = int(date[6:10])
            year1 = int(strftime("%Y"))
            if (len(date) > 10 or year < year1):
                print("Invalid date entered. ")
                try_again = input("Would you like to try again? 'Y' for Yes or 'N' for No. ")
                try_again = try_again.upper()
                if (try_again == 'Y'):
                    continue
                else:
                    start = False
            else:
                calendar[date] = event
                print("Calendar successfully updated.")
                print(calendar)

        elif (user_choice == 'D' or user_choice == 'd'):
            if (len(calendar.keys()) < 1):
                print("The calendar is empty already.")
            else:
                event = input("What event?")
                for date in list(calendar):
                    if (event == calendar[date]):
                        del calendar[date]
                        print("The event has been deleted.")
                        print(calendar)
                    else:
                        print("An incorrect event was specified.")


        elif (user_choice == 'X' or user_choice =='x'):
            start = False
        else:
            print("You entered garbage. Byeee!")
            start = False

start_calendar()
