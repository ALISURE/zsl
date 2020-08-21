import sys

student = [['Tom', 'A', 20], ['Jack', 'C', 18], ['Andy', 'B', 11]]
student.sort(key=lambda student: student[2])

print(student)
