# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combaine_strings = name1+name2
lower_case_string = combaine_strings.lower()

t = lower_case_string.count("t") 
r = lower_case_string.count("r") 
u = lower_case_string.count("u") 
e = lower_case_string.count("e")

true_total = t+r+u+e

l = lower_case_string.count("l") 
o = lower_case_string.count("o") 
v = lower_case_string.count("v") 
e = lower_case_string.count("e")

love_total = l+o+v+e

total = int(str(true_total)+str(love_total))

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >=40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")   