try:
    students = int(input('Введите количество студентов '))
except ValueError:
    print("Введено неверное значение")
    students = int(input("Введите целое число "))

marks = []

while students != len(marks):
    try:
        marks.append(float(input('Введите оценки студентов ')))
    except ValueError:
        print("Введено неверное значение")
        continue

def calculate_average(grades):
    middle = sum(grades) / len(grades) 
    return middle

def find_highest(grades):
    return max(grades)

def find_lowest(grades):  
    return min(grades)

print(calculate_average(marks))
print(find_highest(marks))
print(find_lowest(marks))