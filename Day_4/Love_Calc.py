print("The Love Calculator is calculating your score...")
name1 = input("Enter your name: ") # What is your name?
name2 = input("Enter your crush's name: ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

T_C = (name1+name2).lower().count("t")
R_C = (name1+name2).lower().count("r")
U_C = (name1+name2).lower().count("u")
E_C = (name1+name2).lower().count("e")
L_C = (name1+name2).lower().count("l")
O_C = (name1+name2).lower().count("o")
V_C = (name1+name2).lower().count("v")

total_true = str(T_C + R_C + U_C + E_C)
total_love = str(L_C + O_C + V_C + E_C)

total_true += total_love
love_score = int(total_true)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")