name = input("Enter your name : ")
age = input("Enter your age : ")
major = input("Enter your major : ")
enrolled = input("Are you enrolled ? (True/False) : ")
if enrolled == "True":
    enrolled = True
else:
    enrolled = False
print("\n--- Student Profile ---")
print("Name : " , name)
print("Age : " , age)
print("Major : " , major)
print("Enrolled : " , enrolled)
days = int(input("\nHow many days do you want to track ? "))
study_hours = []
for i in range(days):
    while True:
        hours = float(input(f"Enter study hours for day {i+1}: "))
        if hours >= 0:
            study_hours . append(hours)
            break
        else:
            print("Hours cannot be negative . ")
total_hours = 0
for h in study_hours : 
    total_hours += h
average_hours = total_hours / days
if average_hours >= 6:
    performance = "Excellent"
elif average_hours >= 4:
    performance = "Good"
else:
    performance = "Bad"
print("\n--- Final Report ---")
print("Student Name : " , name)
print("Study Hours List : " , study_hours)
print("Total Study Hours : " , total_hours)
print("Average Study Hours : " , average_hours)
print("Performance Level : " , performance)