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

# Main function for calculating annual income
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


end = ''
while end.lower() != 'x':
    calculateYearly()
    print('Press x to exit the progam or any other key to start over')
    end = input()
