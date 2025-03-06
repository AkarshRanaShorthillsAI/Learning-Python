# Q-1 Classify a person age group : Less than 13 - Child, Less than 20 teen, Less than 60 adult, More than or equal to 60 senior citizen

age = input("Enter an age")
age = int(age)

if(age < 0):
    print("PLease Enter a valid age")
elif(age<13):
    print("Child")
elif(age<20):
    print("Teen")
elif(age<60):
    print("Adult")
else:print("Senior Citizen")


