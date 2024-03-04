#Check if it is possible to survive on Island

#n – Maximum unit of food you can buy each day.
#s – Number of days you are required to survive.
#m – Unit of food required each day to survive.

def survival(s, n, m):
    sunday = s / 7  # Calculate the amount of food consumed on Sundays
    buyingDays = s - sunday  # Calculate the number of days you can buy food
    total_food = s * m  # Calculate the total amount of food you have

    # Check if the total food can be evenly distributed among the number of people
    if total_food % n == 0:
        ans = total_food / n
    else:
        ans = total_food / n - 1

    # Check if the available food is enough for the number of days you can buy food
    if ans <= buyingDays:
        return ans
    else:
        return -1  # Return -1 if the available food is not enough for survival

def main():
    #n = int(input("Enter the maximum unit of food you can buy each day: "))
    #s = int(input("Enter the number of days you are required to survive: "))
    #m = int(input("Enter the unit of food required each day to survive: "))
    
    #    result = survival(s, n, m)
    result = survival(20, 2, 1)
    
    if result != -1:
        print("It is possible to survive on the island for", result, "weeks.")
    else:
        print("It is not possible to survive on the island.")

main()
