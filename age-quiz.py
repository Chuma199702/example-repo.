# Pseudocode:
# 1. Ask the user to enter their age.
# 2. Convert the input to an integer and store it in a variable called age.
# 3. Check if the age is greater than 100.
#    - If yes, print "Sorry, you're dead."
# 4. Else, check if the age is 65 or older.
#    - If yes, print "Enjoy your retirement!"
# 5. Else, check if the age is 40 or over.
#    - If yes, print "You're over the hill."
# 6. Else, check if the age is under 13.
#    - If yes, print "You qualify for the kiddie discount."
# 7. Else, check if the age is exactly 21.
#    - If yes, print "Congrats on your 21st!"
# 8. Otherwise, print "Age is but a number."

age = int(input("Enter your age: "))

if age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.")