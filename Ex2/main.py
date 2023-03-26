import SupportFunctions
import StudentClass
import CourseClass
'''
This py file where all the program, functions call
'''
x = input("Enter file name to open(without .txt): ")
if x == 'StudentDB':
    '''
    This part of code makes reading from Student.txt, makes data suitable
    for Student object constructor and its methods and creating a list of students  
    '''
    st_list = []
    with open("StudentDB.txt", 'r+') as f:
        f.seek(0)
        i = 0
        for line in f:
            y = line.rstrip().rsplit('\t')
            z = y[2].rstrip().rsplit(';')
            z = list(i.split('#') for i in z)#to delete a '#' between course name and course grade
            z = dict(i for i in z if 0 <= int(i[1]) <= 100)
            student = StudentClass.Student(y[0], y[1])
            for name, grade in z.items():
                course = CourseClass.Course(name)
                course.setGrade(int(grade))
                student.addCourse(course)
            st_list.append(student)
    '''
    This part of code represents a menu with options
    '''
    while True:
        print("Menu")
        print("Press 1 to know average grade of specific student")
        print("Press 2 to know the average to specific course")
        print("Press 3 to add to database average grades of all student")
        print("Press 4 to exit from the database")
        choice = input("Enter the choice number: ")
        if choice == '1':
            st_name = input("Enter the name of student: ")
            data = SupportFunctions.get_the_average(st_list, st_name)
            if data is not None:
                print(f'StudentID: {data[0]}, AverageGrade: {data[1]}\n')
        elif choice == '2':
            average = SupportFunctions.get_course_average(st_list)
            if average is not None:
                print(f' Course Average Grade: {average}')
        elif choice == '3':
            output_file_name = input("Enter file name(without .txt): ")
            if output_file_name == "averageDB":
                SupportFunctions.write_students_average_in_db(st_list)
            else:
                print("File name isn't correct, you will be redirected to the menu")
        elif choice == '4':
            print("Exit option is chosen. Goodbye")
            break
        else:
            print("The symbol is not correct.")
else:
    print("The file name is not correct")
