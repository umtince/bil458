# Mehmet Umut İNCEER 21995537 BİL458 HW1

n = int(input("Enter a number: "))

temp = ""

for i in range(0,n+1):
    for k in range(0,n-i):
        temp += " "
    for j in range(0,i):
        temp += "*"
    print(temp)
    temp = ""
