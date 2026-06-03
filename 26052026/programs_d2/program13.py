y=int(input("enter year:"))
if y%400 and y%100==0:
  print(f"{y} is a leap year")
elif y%4==0 and y%100!=0:
    print(f"{y} is a leap year")
else:
    print(f"{y} is not leap year")
