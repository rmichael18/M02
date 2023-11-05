# Ryan Michael
# M02 Case Study
# Determines whether or not a student makes the honor roll or deans list based on entered GPA
while True:
    last_name = input("Enter the student's last name or 'ZZZ' to quit: ")
    
    if last_name == 'ZZZ':
        break
    
    gpa = float(input("Enter the student's GPA: "))
    
    if gpa >= 3.5:
        print(last_name, "has made the Dean's List.")
    
    elif gpa >= 3.25:
        print(last_name, "has made the Honor Roll.")