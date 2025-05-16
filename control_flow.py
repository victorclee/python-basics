"""
A: 70+
B: 60-69
C: 50-59
F: less than 50
"""

grade = 52

if grade >= 70:
    print("A")
elif grade >= 60:
    print("B")
elif grade >= 50:
    print("C")    
else:
    print("you failed")

print("Grading done")
