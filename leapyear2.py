# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
hundred = float(year)
if hundred % 100 == 0 and hundred % 400 != 0:
    print("Not a leap year.")
elif hundred % 4 == 0:
    print("Leap year.")
else:
    print("Not leap year.")