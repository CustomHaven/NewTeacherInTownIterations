# Q2
from roster import student_roster
import itertools
# Import modules above this line
class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)

# Q3
  def __iter__(self):
    self.index = 0
    return self
  # Q3
  def __next__(self):
    each_student = self.sorted_names[self.index]
    self.index += 1
    if self.index >= len(student_roster):
      raise StopIteration
    return each_student
# Q4
  def two_students_seated(self):
    two_list = []
    twos = itertools.combinations(self.sorted_names, 2)
    for two in twos:
      two_list.append(two)
    return two_list

  def _sort_alphabetically(self,students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students
  # Q6
  def get_student_info(self):
    self.student_infos = []
    for student in student_roster:
      self.student_infos.append({student['name']: {
        'age': student['age'],
        'height': student['height'],
        'favorite animal': student['favorite_animal']
      }})
    return self.student_infos