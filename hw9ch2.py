# 9. 10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.


nums = int(input("Enter the count of the numbers that needs to be summed: "))
total = []
for i in range(1, nums + 1):
   y = int(input("Enter the number: "))
   total.append(y)

Sum_of_Numbers = sum(total)
print(Sum_of_Numbers)