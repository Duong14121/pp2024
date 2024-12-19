# Input student information
def input_student_info(student_number):
    students = {}
    for _ in range(student_number):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD-MM-YYYY): ")
        students[student_id] = {"name": name, "dob": dob}
    return students

# Input course information.
def input_course_info(number_of_courses):
    courses = {}
    for _ in range(number_of_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

# Input marks for students in a selected course
def input_marks(student, courses):
    marks = {}
    print("The courses are:")
    for course_id, course_name in courses.items():
        print(f"{course_id}: {course_name}")

    selected_course_id = input("Select a course ID to enter marks for: ")

    if selected_course_id not in courses:
        print("Invalid course ID.")
        return

    marks[selected_course_id] = {}

    for student_id, student_info in student.items():
        student_name = student_info["name"]
        mark = input(f"Enter marks for {student_name} (ID: {student_id}) in {courses[selected_course_id]}: ")
        marks[selected_course_id][student_id] = mark

    return marks

# List all courses
def list_courses(courses):
    print("\nList of Courses:")
    for course_id, course_name in courses.items():
        print(f"{course_id}: {course_name}")

# List all students
def list_students(students):
    print("\nList of Students:")
    for student_id, student_info in students.items():
        print(f"ID: {student_id}, Name: {student_info['name']}, DoB: {student_info['dob']}")

# Show student marks
def show_student_marks(marks, students, courses):
    course_id = input("Enter the course ID: ")
    if course_id not in marks:
        print("This course has no marks availble.")
        return

    print(f"\nMarks for Course: {courses[course_id]}")
    for student_id, mark in marks[course_id].items():
        print(f"Student: {students[student_id]['name']} (ID: {student_id}) - Marks: {mark}")

def main():
    students = input_student_info(int(input("Enter number of students: ")))
    courses = input_course_info(int(input("Enter number of courses: ")))
    
    marks = input_marks(students, courses)
    
    list_courses(courses)
    
    list_students(students)
    
    show_student_marks(marks, students, courses)

main()