lst = []
while True:
    x = input("nhap so ban mong muon vao list / end(de ket thuc): ")
    if x == "end":
        break
    else:
        x = int(x)
        lst.append(x)
print(lst)

avr = float(sum(lst)/len(lst))
print(avr)

nearest = []
for i in lst:
    nearst = abs(avr-i)
    nearest.append(nearst)
print(nearest)
min_value = min(nearest)
print(min_value)
indx = nearest.index(min_value)
print(indx)