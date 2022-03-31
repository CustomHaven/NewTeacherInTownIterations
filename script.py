# https://www.codecademy.com/courses/learn-intermediate-python-3/projects/new-teacher-in-town-project
# Q1
import itertools
from roster import student_roster
from classroom_organizer import ClassroomOrganizer
# Q1
print("task 1")
print("The full student roster (dictionary):")
new_student = ClassroomOrganizer()
student_roster_iterator = iter(student_roster)
print(len(student_roster))
for i in student_roster:
  print(next(student_roster_iterator))
  # print(i)

print("-----------------------------------------------")
# Q3
print()
print("task 3")
print("We only using __iter__ and __next__ of the class methods to try them out normally a normal for loop does the job")
print()
new_student.__iter__()
for each_name in range(len(new_student.sorted_names)-1): 
  print(new_student.__next__())

# Normally how I rather do it
print()
for each_name in new_student.sorted_names: 
  print(each_name)
print("-----------------------------------------------")
# Q4
print()
print("task 4 - 2 student combos")
print()
two_student_combos = new_student.two_students_seated()
print(two_student_combos)
print("-----------------------------------------------")
# Q5
print()
print("task 5 - combining all maths and science students into table of 4s")
print()
math_science_students = itertools.chain(new_student.get_students_with_subject('Math'), new_student.get_students_with_subject('Science'))
table_of_4 = itertools.combinations(math_science_students, 4)

print(list(table_of_4))
print("-----------------------------------------------")

# Q6
print()
print("task 6: student name, age, height and favorite_animal")
print()
new_student.get_student_info()
for student in new_student.student_infos:
  print(student)
print()
print(new_student.student_infos)