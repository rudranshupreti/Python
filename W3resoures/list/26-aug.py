"""Write a Python program to sum all the items in a list.
list = [1, 1, 23, 2, 2, 3, 2]
add = int()
for i in list:
    add += i
print(add)"""

"""Write a Python program to get the largest number from a list.


def check(list):
    list_max = list[0]
    for i in list:
        if i > list_max:
            list_max = i
    return list_max


print(check([1, 2, 3, 2, 2, 34]))"""
"""Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2


# matlab mujhe ek esa program banna he jo ye check kr ske ki jo value he string me usme per str me 2 ya do se jyada word he and unme se unka first or last element same he esa kitne element he
def check(list):
    f = int()
    for i in list:
        if len(i) <= 2 or i[0] == i[-1]:
            f += 1
    print(f)


check(["abc", "xyz", "aba", "1221"])"""

"""Write a Python program to remove duplicates from a list.
list = [1, 1, 23, 2, 2, 3, 2]
final = [0]
for i in list:
    if i not in final:
        final.append(i)
print(final)"""
"""Write a Python program to check if a list is empty or not.
l = []
if not l:
    print("empty")"""
"""Write a Python program to find the list of words that are longer than n from a given list of words.
def check(num, list):
    for i in list:
        if len(i) <= num:
            print(i)
check(3, ["asd", "adfs"])"""

"""Write a Python function that takes two lists and returns True if they have at least one common member.


def check(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                print("true")


check(
    [1, 4, 21, 3, 322, 11],
    [1, 23, 2, 23, 2, 23, 4],
)"""
