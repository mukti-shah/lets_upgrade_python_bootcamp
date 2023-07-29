# You are tasked with creating a simple student grading program using Python. The program should take input from the user for the marks obtained by a student in a subject and then calculate and display the grade based on the following grading scale:

# 90 or above: A+
# 80 to 89: A
# 70 to 79: B
# 60 to 69: C
# 50 to 59: D
# Below 50: Fail

# Requirements:
# Use control statements (if-elif-else) to determine the grade based on the marks obtained by the student.
# Handle any potential errors in the user input (e.g., invalid marks) and display appropriate messages to the user.
# Implement a loop to allow the user to calculate the grade for multiple students until they decide to exit.
# Display the calculated grade for each student.


# Calculate and display grades for multiple students


method = int(input("\n1 for individual grade calculation, 2 for multiple simultaneous grade calculation: "))


if method==1:
    ex = "n"

    while ex=="n":
        marks = (input("\n\nEnter marks obtained by the student: "))
        
        try:
            marks = float(marks)
                
        except:
            print("Marks should be a number.")
            continue

        grade = ""

        if marks<=100 and marks>=0:
            marks = round(marks)
            if marks<=100 and marks>=90:
                grade = 'A+'
                
            elif marks<=89 and marks>=80:
                grade = 'A'
                
            elif marks<=79 and marks>=70:
                grade = 'B'
                
            elif marks<=69 and marks>=60:
                grade = 'C'
                
            elif marks<=59 and marks>=50:
                grade = 'D'
                
            else:
                grade = 'Fail'
                
            print("Grade: "+ grade)

        else:
            print("Enter valid marks.")
            
        
        ex = input("\nDo you want to exit? (y for yes, n for no): ").lower()
        


elif method==2:

    marks_list = []

    print("\n\nEnter all the marks. (enter 'exit' to exit)")

    while True:
        marks = input("\n>> ")
        if marks=="exit":
            break
        else:
            try:
                marks = float(marks)
                
            except:
                print("Marks should be a number.")
                
            else:
                    if marks<=100 and marks>=0:
                        marks_list.append(marks)
                    
                    else:
                        print("Marks should be between 0 and 100")


    print("\n\n{:<8} Grade".format("Marks"))
    print("-"*16)
        
    for marks in marks_list:

        grade = ""

        marks = round(marks)
        if marks<=100 and marks>=90:
            grade = 'A+'
                
        elif marks<=89 and marks>=80:
            grade = 'A'
                
        elif marks<=79 and marks>=70:
            grade = 'B'
                
        elif marks<=69 and marks>=60:
            grade = 'C'
                
        elif marks<=59 and marks>=50:
            grade = 'D'
                
        else:
            grade = 'Fail'
                
        print("{:<10} {}".format(marks,grade))
      
    

else:
    print("Invalid option")
    
print("")