'''
This py file contains student class with its methods
'''




class Student:
    '''
    This class represents methods and variables of student object
    '''

    def __init__(self, name, id):
        '''
        contructor for student object
        :param name: student name
        :param id: student id
        '''
        self.name = name
        self.__id = id
        self.courses = []

    def getID(self):
        '''
        This method returns private data of particular student(id)
        :return: student id
        '''
        return self.__id

    def addCourse(self, course):
        '''
        This function adds a course object to course list if the grade is valid
        :param course: course object
        :return: nothing, because this function only execute actions and not calculates specific value to return
        '''
        if 0 <= course.grade <= 100:
            self.courses.append(course)



