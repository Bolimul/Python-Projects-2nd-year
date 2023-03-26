'''
This py file contains course class with its methods
'''

class Course:
    '''
    This class represents course object which contains course name and course grade
    '''
    def __init__(self, course_name):
        '''
        constructor for course object
        :param course_name: name of the course
        '''
        self.course_name = course_name
        self.grade = 101

    def setGrade(self, grade):
        '''
        This method sets a course grade if the one is valid
        :param grade: course grade
        :return: nothing, because this function only execute actions and not calculates specific value to return
        '''
        if 0 <= grade <= 100:
            self.grade = grade

