#Chocolate Distribution Problem

def Chocolate_Distribution(chocolates, number_of_chocolatespacket, number_of_student):
    if number_of_chocolatespacket == 0 or number_of_student == 0:
        return 0
    
    if number_of_chocolatespacket < number_of_student:
        return -1 
    
    start = 0
    end = number_of_student - 1
    min_difference = float('inf') 
    
    for i in range(number_of_chocolatespacket - number_of_student + 1):
        difference = chocolates[end] - chocolates[start]
        min_difference = min(min_difference, difference)
        start += 1
        end += 1
    
    return min_difference
    


def main():
    chocolates = [3, 4, 1, 9, 56, 7, 9, 12]
    number_of_chocolatespacket = len(chocolates)
    number_of_student = 5
    chocolates.sort()
    result = Chocolate_Distribution(chocolates, number_of_chocolatespacket, number_of_student)
    print(result)
    
main()

