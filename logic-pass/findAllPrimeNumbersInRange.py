minNum = int(input("Enter 1st Number: "))
maxNum = int(input("Enter 2nd Number: "))

print("this program find all prime numbers between", minNum, "and", maxNum)
for num in range(minNum, maxNum +1):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        break
    else:
      print(num)