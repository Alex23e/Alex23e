# Simple GPA Calculator Starter
print("--- Level 100 GPA Calculator ---")

num_courses = int(input("How many courses did you take this semester? "))
total_points = 0
total_credits = 0

for i in range(num_courses):
    course_name = input(f"\nEnter name for course {i+1}: ")
    credits = int(input(f"Enter credit hours for {course_name}: "))
    score = float(input(f"Enter your score (0-100) for {course_name}: "))
    
    # Simple grading scale logic
    if score >= 80:
        grade_point = 4.0  # Grade 
    elif score >= 70:
        grade_point = 3.0  # Grade B
    elif score >= 60:
        grade_point = 2.0  # Grade C
    else:
        grade_point = 1.0  # Grade D/F
        
    total_points += (grade_point * credits)
    total_credits += credits

gpa = total_points / total_credits
print(f"\nYour Semester GPA is: {gpa:.2f}")
