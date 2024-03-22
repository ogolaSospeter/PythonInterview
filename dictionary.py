students = [
{"id":1, "details": {"name": "John", "age":25,"gender":"Male","courses":["Math","Science"]}},
{"id":2, "details": {"name": "Jane", "age":20,"gender":"female","courses":["Math","Science"]}},
{"id":3, "details": {"name": "Tom", "age":22,"gender":"Male","courses":["Math","Kiswahili"]}}
]

def get_students():
    for student in students:
        print("-----------------------------------------------")
        print(student["id"])
        print(student["details"]["name"])
        print(student["details"]["age"])
        print(student["details"]["gender"])
        for course in student["details"]["courses"]:
            print("\t" + course)
        print("\n")
        print("-----------------------------------------------")

def add_student(**student):
    students.append(student)
    return students

def remove_student(*unique_student):
    for student in students:
        if student['id'] == unique_student:
            students.remove(student)
            return students
        else:
            return "Student not found"
        
def update_student(id, **student):
    for student in students:
        if student['id'] == id:
            student.update(student)
            return students
        else:
            return "Student not found"
        

if __name__ == "__main__":
    on_start = "Welcome to the System simulator. Please select an option from the following:\n1. View students\n2. Add student\n3. Remove student\n4. Update student\n5. Exit"
    on_exit  = "Thank you for using the system simulator. Goodbye!"
    on_error = "Invalid option. Please select a valid option."
    on_success = "Operation successful"
    on_failure = "Operation failed"

    print(on_start)
    option = input("Select an option from the above.:\n ")
    if option == "1":
        get_students()
    elif option == "2":
        student_id = students[-1]["id"] + 1
        name = input("\nEnter student name: ")
        age = input("\nEnter student age: ")
        gender = input("Enter your gender: ")
        courses = input("Enter the courses you are taking : ").split(" ")

        student = {"id":student_id, "details": {"name": name, "age":age,"gender":gender,"courses":courses}}
        add_student(student)
        print(on_success)
    elif option == "3":
        student_id = input("Enter student id: ")
        on_confirm = input("Are you sure you want to remove this student? (yes/no): ")
        if on_confirm == "yes":
            remove_student(student_id)
            print(on_success)
        else:
            print(on_failure)
    elif option == "4":
        student_id = input("Enter student id: ")
        name = input("\nEnter student name: ")
        age = input("\nEnter student age: ")
        gender = input("Enter your gender: ")
        courses = input("Enter the courses you are taking : ").split(" ")

        student = {"id":student_id, "details": {"name": name, "age":age,"gender":gender,"courses":courses}}

        update_student(student_id, **student)
        print(on_success)
    elif option == "5":
        print(on_exit)
    else:
        print(on_error)


                    
        remove_student(student_id)
        print(on_success)

