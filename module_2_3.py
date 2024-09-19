my_list = [42, 0, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []

n = 0
while n < len(my_list) and my_list[n] >= 0:
    new_list.append(my_list[n])
    if my_list[n] == 0:
        new_list.remove(0)
    n = n + 1

n = 0
while n < len(new_list):
    print(new_list[n])
    n = n + 1