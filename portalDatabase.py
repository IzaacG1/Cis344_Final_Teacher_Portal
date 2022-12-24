import mysql.connector
from mysql.connector import Error
import cgi

class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='insert password'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
    

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID , grade=0):
        add_student = ("INSERT INTO Students (studentName, enrolledInCourseID, grade)"
                       "VALUES (\""+name+ "\", "+courseID+", "+grade+")")
        cursor = self.connection.cursor()
        cursor.execute(add_student)
        self.connection.commit()
        cursor.close()
    def addCourse(self, name):
        self.cursor = self.connection.cursor()
        add_course = "insert into courses(courseName) values (%s)"
        self.cursor.execute(add_course, (name,))
        self.connection.commit()
        self.connection.close()
    def modifyGrade(self, studentID, grade):
        ''' Complete the method to update the grade of the student'''
        pass
    def showCourses(self, studentid):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("showStudent", args= (studentid,))
            records = self.cursor.stored_results()
            return records
