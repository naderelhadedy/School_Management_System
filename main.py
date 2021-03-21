# classes of school
available_classes = ['A', 'B', 'C']

# keys are teachers' names and values are number of students per teacher
available_teachers = {}

# message printed when there is no teacher in the available teachers list
alert_message = "There is no available teachers, Create one first"

class Teacher:
    ''' This class represents each teacher that has 0 students when created and gets the first class of available classes list '''

    def __init__(self, name):

        self.name = name

        # number of students
        available_teachers[self.name] = 0

        if len(available_classes) >= 1:
            self.Class = available_classes[0]
            available_classes.pop(0)
        else:
            raise ValueError('There is no available classes')

class Student:
    ''' This class represents each student that gets the first teacher at the available teachers list; once a teacher reaches
        the max number of students which is FIVE, it raises an error to create another teacher first '''

    def __init__(self, name):

        self.name = name

        if len(available_teachers) >= 1:

            target_key = list(available_teachers.keys())[0]
            if available_teachers.get(target_key) == 5:
                available_teachers.pop(target_key)

            if len(available_teachers) >= 1:
                new_target_key = list(available_teachers.keys())[0]
                self.teacher = new_target_key
                available_teachers[new_target_key] += 1

            else:
                raise ValueError(alert_message)

        else:
            raise ValueError(alert_message)

# instance of class Teacher
teacher_one = Teacher("Mr. Ahmed Ali")

# instances of class Student
student_one = Student("Rovan Mhana")
student_two = Student("Mohamed Ali")
student_three = Student("Mostafa Nabil")
student_four = Student("Nada Samir")
student_five = Student("Heba Shadoufa")

# instance of class Teacher
teacher_two = Teacher("Mrs. Mona Noureldeen")

# instances of class Student
student_six = Student("Nada Mohamed")
student_seven = Student("Hoda Mohamed")
student_eight = Student("Heba Mohamed")
student_nine = Student("Ghada Mohamed")
student_ten = Student("Noura Mohamed")

# instance of class Teacher
teacher_three = Teacher("Mrs. Rehab Abdelfattah")

# instances of class Student
student_eleven = Student("Mazen Mohamed")
student_twelve = Student("Khaled Mohamed")
student_thirteen = Student("Momen Mohamed")
student_fourteen = Student("Ziad Mohamed")
student_fifteen = Student("Suzan Mohamed")


# print(available_classes)
# print(available_teachers)

print(f"{student_three.teacher} teaches to {student_three.name} which is at class {teacher_one.Class}.")
print(f"{student_seven.teacher} teaches to {student_seven.name} which is at class {teacher_two.Class}.")
print(f"{student_twelve.teacher} teaches to {student_twelve.name} which is at class {teacher_three.Class}.")