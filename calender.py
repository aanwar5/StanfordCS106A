NUM_MONTHS = 12
NUM_DAYS_IN_WEEK = 7

def main():

    year = int(input("Enter year for calender: "))
    first_day = first_day_of_year(year)

    for month in range(1, NUM_MONTHS + 1):
        first_day = print_month(first_day, month, year)


def is_leap_year(year):
    ''' This function returns a boolean indicating whether a given year
is a leap year or not. What defines a leap year is if a year is divisible
by 4, but not divisible by 100
        OR
        divisible by 400!'''
    return (year % 4 ==0) and (year % 100 !=0) or (year % 400 == 0)



def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month ==11:
        return 30
    else:
        return 31
def print_month_header(month):

    print("Month Number: " + str(month))
    print("Sun Mon Tue Wed Thu Fri Sat")

def format_number(num):
    result = " " + str(num)
    if num < 10:
        result = result + " "
    return result

#which is the first day of the month is print_month definition
def print_month(first_day, month, year):

    print_month_header(month)
    days=days_in_month(month, year)
    #prints leading space before the first day in this month
    for i in range(first_day):
        print("    ", end ="")
        #prints numbers for all days in the week
    for i in range(0, days):
        print(format_number(i+1), end ="")

        if((first_day +i) % NUM_DAYS_IN_WEEK) == (NUM_DAYS_IN_WEEK -1):
            print("")

    print("")

    return (first_day + days) % NUM_DAYS_IN_WEEK

def first_day_of_year(year):
    year -=1
    return(year + year//4) - (year //100) + (year //400 + 1) % NUM_DAYS_IN_WEEK

if __name__ == '__main__':
    main()




