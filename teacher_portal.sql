create database teachers_portal;
use teachers_portal;

Create table Students (
studentId int not null unique auto_increment,
studentName varchar (45) Not Null,
enrolledInCourseID int default 1,
grade float null,
primary key (studentId)
);

Create table Courses (
courseId int not null unique auto_increment, 
courseName varchar (45) not null,
primary key (courseId)
);

Insert into Students (studentName, enrolledInCourseID, grade)
values ("Maria Jozef", 1, 90.0),
		("Linda Jones", 2, 89.0),
        ("John McGrail", 1, 98.0),
        ("Patty Luna", 2, 78.0);
        
Select * from Students;


Insert into Courses (courseName)
values ("Database Design"),
		("Calculus"),
        ("Physics I");
        
select * from Courses;

delimiter $$
create procedure studentsWithGrade()
begin
Select *
From Students
		LEFT JOIN Courses ON enrolledInCourseID = courseID;
end $$
delimiter ;
	
        
