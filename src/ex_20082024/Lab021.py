# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade
# for a given numerical score (e.g., A, B, C, D, or F)
# based on the following grading scale:
#
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = int(input("Enter your score\n"))
if 90 <= score <= 100:
    print("Your Grade is", "A")

elif 80 <= score <= 89:
    print("Your Grade is", "B")

elif 70 <= score <= 79:
    print("Your Grade is", "C")

elif 60 <= score <= 69:
    print("Your Grade is", "D")

else:
    print("Your Grade is", "F")
