number = input("Nhập vào 1 dãy số, cách nhau bởi dấu ' ': ")
list_number = number.split()

print("Dãy số vừa nhập theo chiều ngược: ")
for i in reversed(list_number):
    print(i)
