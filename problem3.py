lst = []
while True:
    x = input("Nhap vao so ban muon / end (de ket thuc): ")
    if x == "end":
        break
    else:
        x = int(x)
        lst.append(x)
unique_set = set(lst)
print(unique_set)