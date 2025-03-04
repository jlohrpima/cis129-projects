# Josh Lohr, 03/03/25
# code collects data for a week of bottle collection, then calculates payout

# declare variables
totalBottles = 0
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

# loop to run program
while keepGoing == 'y':
    totalBottles = 0  # Reset the total bottles at the start of each week
    counter = 1
    while counter <= 7:
        # Get the number of bottles collected for each day
        todayBottles = int(input(f'Enter the number of bottles collected for day #{counter}: '))  # Convert input to int
        totalBottles += todayBottles
        counter += 1
    
    # Calculate the payout based on total bottles collected for the week
    totalPayout = 0.10 * totalBottles
    
    # Output results
    print('The total number of bottles collected is:', totalBottles)
    print(f'The total payout is ${totalPayout:.2f}')
    
    # Ask if user wants to enter another week's worth of data
    print('Do you want to enter another week\'s worth of data?')
    print('Enter y or n:')
    keepGoing = input().lower()  