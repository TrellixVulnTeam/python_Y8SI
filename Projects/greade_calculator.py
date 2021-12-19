# create greade calculator in python using dictionary and function 

# Bikky sir Dictionary
Bickky = {
    'name' : 'Bikky Sahani',
    'projects' : [90, 95, 94, 98, 100],
    'test' : [99, 98],
} 

# khusilal dictionary 
khusilal = {
    'name' : 'khusilal',
    'projects' : [80, 70, 90, 85, 88],
    'test' : [80, 85]
}

# Ramesh dictionary 
ramesh = {
    'name' : 'Ramesh Thapa Magar',
    'projects' : [60, 70, 80, 85, 84], 
    'test' : [80, 75]
}

# yogesh dictionary 
yogesh = {
    'name' : 'Yogesh Khanal',
    'projects' : [80, 84, 90, 60, 70],
    'test' : [80, 85]
}

# average of marks 
def average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)


# total average 
def calculate_total_average(students):
    projects = average(students['assignment'])
    test = average(students['test'])

    return (0.1 * projects + 0.2 * test)

# grade 
def assign_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    elif score >= 50: return 'E'

# average of whole class 
def class_average(student_list):
    result_list = []

    for student in student_list:
        stud.avg = calculate_total_average(student)
        result_list.append(stud.avg)
        return average(result_list)

students = [Bickky, khusilal, yogesh, ramesh]

for i in students:
    print(i['name'])
    print('Average marks of %s : %s', i['name'],calculate_total_average[i])
    print()
    class_av= class_average(students)
    print('class average is %s' %(class_av))
    print('letter grade of class is %s', (assign_letter_grade(class_av)))
