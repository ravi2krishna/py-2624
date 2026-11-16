# Student Management System

# Build Menu Based System -> In Future, Replace With UI Elements Like Buttons 

# System Setup -> READ ONLY (Tuple)
# system_info = ("Digital Tech","Student Management System","v1")
SYSTEM_INFO = ("Digital Tech","Student Management System","v1")

# Admin Info -> READ ONLY (Tuple)
ADMIN_INFO = ("9999999999","admin@digital.com")

# When this Application is Started, Display System Info 
print("=" * 50)
print(f"            Welcome To {SYSTEM_INFO[0]}")
print(f"        Software {SYSTEM_INFO[1]}-{SYSTEM_INFO[-1]}")
print("=" * 50)

# Core Functionalities (CRUD)
# Add Student -> ID, Name, Scores, Skills 
# Represent Student Data 
# ID - String 
# Name - String 
# Scores - Lists 
# Skills - Sets 

# students = {
#     "101": {
#         "name":"Ravi",
#         "scores":[90,90,80],
#         "skills":{"python","sql","reactjs"}
#     },
#     "102": {
#             "name":"John",
#             "scores":[80,70],
#             "skills":{"java","reactjs"}
#     }
# }

# Construct Data Structure To Store Above Students Data i.e Dictionary
students = {}

# Build Menu Based System For CRUD Operations 

while True:
    print("1 - Create Student") # Assume These Are Buttons 
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - Read Student")
    print("5 - Exit Application")

    choice = input("Enter Your Choice (1-5): ")
    
    if choice == "1":
        # Create Student 
        print("=" * 30)
        print("     Adding Student")
        print("=" * 30)
        
        student_id = input("Enter Student ID: ")
        
        if student_id in students:
            print("=" * 70)
            print(f"OOPS!!!! Student ID {student_id} Already Exists In System")
            print("=" * 70)
        else:
            name = input("Enter Student Name: ").title()
            scores = []
            while True:
                score_input = input("Enter Score or type done: ")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score_input = int(score_input)
                    if 0 <= score_input <= 100:
                        scores.append(score_input)
                    else:
                        print(f"Invalid Score {score_input} Given, Should Be (0-100) Only")
                else:
                    print(f"Invalid Score {score_input} Given, Should Be Digits Only")
                    
            skills = set()
            while True:
                skill_input = input("Enter Skill or type done: ")
                if skill_input == "done":
                    break
                else:
                    skills.add(skill_input)
                    
            print(students) # Before Adding Students 
            
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            
            print(students) # After Adding Students 
                   
    
    elif choice == "2":
        # Update Student 
        print("=" * 30)
        print("     Updating Student")
        print("=" * 30)
        
        student_id = input("Enter Student ID To Update: ")
        
        if student_id in students:
            new_name = input("Enter New Name: ").title()
            students[student_id]['name'] = new_name
            print("=" * 30)
            print(f"Student ID {student_id} Updated")
            print("=" * 30)
            
        else:
            print("=" * 70)
            print(f"OOPS!!!! Student ID {student_id} Doesn't Exist In System")
            print("=" * 70)
            
        print(students) # After Updating Students this is for confirmation
    
    elif choice == "3":
        # Delete Student 
        print("=" * 30)
        print("     Deleting Student")
        print("=" * 30)
        
        student_id = input("Enter Student ID To Delete: ")
        
        if student_id in students:
            
            students.pop(student_id)
            
            print("=" * 30)
            print(f"Student ID {student_id} Deleted")
            print("=" * 30)
            
        else:
            print("=" * 70)
            print(f"OOPS!!!! Student ID {student_id} Doesn't Exist In System")
            print("=" * 70)
            
        print(students) # After Delete Students this is for confirmation
        
        
    elif choice == "4":
        # Read Student 
        print("=" * 30)
        print("     Reading Student")
        print("=" * 30)
        
        student_id = input("Enter Student ID To Read: ")
                
        if student_id in students:
             
            # {'101': {'name': 'Ravi', 'scores': [90, 90, 80], 'skills': {'python', 'sql', 'react'}}}
            data = students[student_id] # assume student_id is 101
            # data = {'name': 'Ravi', 'scores': [90, 90, 80], 'skills': {'python', 'sql', 'react'}}
            name = data['name']
            
            # All Scores
            scores = data['scores'] 
            
            # Average Score
            total_score = 0
            count_scores = 0
            
            for score in scores:
                total_score += score
                count_scores += 1
            
            average_score = total_score / count_scores
            
            # Highest Score 
            high_score = scores[0]
            
            for score in scores:
                if score > high_score:
                    high_score = score
                    
            # Lowest Score 
            low_score = scores[0]
            
            for score in scores:
                if score < low_score:
                    low_score = score
            
            # All Skills 
            skills = data['skills'] 
            
            # Skills Count
            skill_count = 0
            for skill in skills:
                skill_count += 1
            
            # Displaying Student Information
            print("=" * 30)
            print("     Student Information")
            print("=" * 30)
            
            print(f"Student ID: {student_id}")
            print(f"Student Name: {name}")
            print(f"Student Scores: {scores}")
            print(f"Student Average Score: {average_score}")
            print(f"Student Highest Score: {high_score}")
            print(f"Student Lowest Score: {low_score}")
            print(f"Student Skills: {skills}")
            print(f"Student Skills Count: {skill_count}")

        else:
            print("=" * 70)
            print(f"OOPS!!!! Student ID {student_id} Doesn't Exist In System")
            print("=" * 70)
            
    elif choice == "5":
        # Exit Application 
        print("=" * 30)
        print("     Exiting Application")
        print("=" * 30)
        
        # When this Application is Closed, Display Admin Info 
        print("=" * 30)
        print(f"     Admin Contact Number {ADMIN_INFO[0]}")
        print(f"     Admin Email IS {ADMIN_INFO[-1]}")
        print("=" * 30)
        break
            
    else:
        print("=" * 60)
        print(f"     Invalid Choice Selected {choice} - Use Only (1-5)")
        print("=" * 60) 
        
