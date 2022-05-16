# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_names = name1 + name2
low_name = combined_names.lower()
t = low_name.count("t")
r = low_name.count("r")
u = low_name.count("u")
e = low_name.count("e")
l = low_name.count("l")
o = low_name.count("o")
v = low_name.count("v")
trues = t + r + u + e
loves = l + o + v + e
score = str(trues) + str(loves)
if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")