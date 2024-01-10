#Problem 2
def a_den_f(diem):
    if diem >= 8.5 and diem <= 10:
        return 'A'
    if diem >= 7 and diem <= 8.4:
        return 'B'
    if diem >= 5.5 and diem <= 6.9:
        return 'C'
    if diem >= 4 and diem <= 5.4:
        return 'D'
    if diem >= 0 and diem < 4:
        return 'F'
    
def gpa(diem):
    if diem >= 8.5 and diem <= 10:
        return '4'
    if diem >= 7 and diem <= 8.4:
        return '3'
    if diem >= 5.5 and diem <= 6.9:
        return '2'
    if diem >= 4 and diem <= 5.4:
        return '1'
    if diem >= 0 and diem < 4:
        return '0'
    
try:
    n = float(input("Enter the grade in decimal system: "))
    if n >= 0 and n <= 10:
        chucai = a_den_f(n)
        gpa = gpa(n)
        print(f"the corresponding grade in alphabetic: {chucai}")
        print(f"the corresponding grade in 4th system: {gpa}")
    else:
        print("Grade must be from 0 to 10 !")
except ValueError:
    print("Please enter a valid grade !")
    