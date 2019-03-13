# hourlyRate.py - A simple program that returns yearly income based on hourly wages

# Function that places commas in monetary amount
def putInCommas(income):
    count = len(str(income))
    n = income
    result = ''
    for i in range(count):
        if i % 3 == 0 and (i != 0 and i != count):
            result = ',' + result
        digit = n % 10
        result = str(digit) + result
        n = n // 10
    return result

# Function for calculating annual and biweekly income given hourly wage
# and work hours per week
def calculateYearly():
    print('Please enter your hourly income rate: ')
    hourlyRate = int(input())
    print('Please enter the number of hours you work per week: ')
    hours = int(input())
    
    # Calculate annual and bi-weekly income rate
    yearly = hours * hourlyRate * 52
    biWeekly = hours * hourlyRate * 2
    print('Your annual income is: $' + putInCommas(yearly))
    print('Your bi-weekly income is: $' + putInCommas(biWeekly))

# Function that calculates hourly and biweekly wage given annual income
# and work hours per week
def calculateHourly():
    print('Please enter your annual income rate: ')
    annualRate = int(input())
    print('Please enter the number of hours you work per week: ')
    hours = int(input())

    # Calculate hourly and biweekly income rate
    biWeekly = round(annualRate / 26, 2)
    hourly = round((biWeekly / 2) / hours, 2)
    print('Your hourly income rate is: $' + str(hourly))
    print('Your bi-weekly income is: $' + str(biWeekly))
    
    


end = ''
while end.lower() != 'x':
    print('Would you like to calculate your annual income or hourly rate? (Press 1 for annual income, 2 for hourly rate, and any other key to quit.')
    try:
        answer = int(input())
    except ValueError:
        break
    if answer == 1:
        calculateYearly()
    elif answer == 2:
        calculateHourly()
    else:
        break
    print('Press x to exit the progam or any other key to start over')
    end = input()
