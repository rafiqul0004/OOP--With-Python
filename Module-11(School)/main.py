from School import School, ClassRoom, Subject
from Person import Student, Teacher

def main():
    school = School('BBCHS', 'CTG')

    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    # add students
    rahat = Student('Rahat', ten)
    school.student_admission(rahat)
    mehek = Student('Mehek', ten)
    school.student_admission(mehek)
    hande = Student('Hande Ercel', ten)
    school.student_admission(hande)

    # subjects
    physics_teacher = Teacher('Shahjahan Tapon Sir')
    physics = Subject('physics', physics_teacher)
    ten.add_subject(physics)

    chemistry_teacher = Teacher('Haradon Nag Sir')
    chemistry = Subject('chemistry', chemistry_teacher)
    ten.add_subject(chemistry)
    
    biology_teacher = Teacher('Azmal Sir')
    biology = Subject('biology', biology_teacher)
    ten.add_subject(biology)

    ten.take_semester_final()


    print(school)

if __name__ == '__main__':
    main()