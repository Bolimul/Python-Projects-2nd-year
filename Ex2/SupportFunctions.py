
'''
This py file contains functions for main program
'''


def get_the_average(st_list, st_name):
    '''

    This function calculates the average grade of specific student
    :param st_list - list of students, st_name - name of specific student
    :return the tuple that contains student id and average grade
            if student was not found, print the message and return None, because there is nothing to return
    '''
    studentName = list(filter(lambda x: x if x.name == st_name else None, st_list))
    if len(studentName) == 0:
        print("There is no such student in database\n")
        return None
    else:
        student_name = studentName[0]
        average = sum(list(map(lambda x: x.grade, student_name.courses))) / len(student_name.courses)
        return (student_name.getID(), average)


def get_course_average(st_list):
    '''
    This function calculates the average grade of all students about specific course

    :param st_list: list of students
    :return: the average grade
    '''
    course_name = input("Enter the course name: ")
    students = list(map(lambda x: x, st_list))
    courses = sum(list(map(lambda x: x.courses, students)), [])
    neededGrades = list(filter(lambda x: x.grade if x.course_name == course_name else None,courses))
    if len(neededGrades) == 0:
        print("There is not such course in database\n")
        return None
    neededGrades = list(map(lambda x: x.grade, neededGrades))
    average = sum(neededGrades)/len(neededGrades)
    return average


def write_students_average_in_db(st_list):
    '''
    This function makes a list of tuples to send to the map to write the data to output file
    Function writeInFile takes as argument specific tuple and writes in specific way to output file

    :param st_list: list of students
    :return: None, because this function only writes the data to specific file
    '''
    average_list = list(map(lambda x: get_the_average(st_list, x.name), st_list))
    def writeInFile(student):
            with open("averageDB.txt", 'a') as f:
                f.write(f'{student[0]} {student[1]}\n')
    list(map(writeInFile, average_list))
    return None

