def removeChar():
  strLine = input("Enter String: ")
  print(strLine)
  while True:
    removech = input("Enter character you want delete it: ")
    if not removech:
      break
    newStr = strLine.replace(removech, "")
    print(newStr)

removeChar()