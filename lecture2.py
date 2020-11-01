from copy import deepcopy
# prod1 = "Iphone12"
# prod2 = "Samsung"
# karzina = [prod1, prod2, 1,2,3]

# nums = [1,[2,3,4,[5,6,7]],3,4]
# nums.append(6)
# print(nums)
# nums.pop()
# print(nums[1][3][1])

# spisok1 = [1,2,3]
# name = 'bakyt nurbek makers'
# spisok2 = list(name)
# print(spisok2)

# spisok = ['name', 'makers', True, 2, [3,2,4,5],2, 'name',2]
# spisok = [4,2,7,9,0,2,6,4,7,8,1]
spisok = ['abc', 'bcd', 'sdgdf', 'dsgf', 'dsfgdd', 'f']
# spisok2 = [9,8,7,6,2, 'word1']
# name = 2
# spisok.append('word')
# new_spisok = spisok.copy()
# spisok.append('second word')
# new_spisok[4][0] = 'new word'
# print(new_spisok)
# print(spisok)
# new_spisok = deepcopy(spisok)
# spisok[4][1] = 'word'
# print(spisok)
# print(new_spisok)
# num = spisok.count()
# print(num)
# spisok.extend(spisok2)
# spisok3 = spisok2 + spisok
# print(spisok3)
# num = spisok.index(2, 5)
# print(num)
# spisok.insert(3, 'indexed')
# item = spisok.pop(10)
# print(item)
# spisok.remove([3,2,4,5])
# spisok.reverse()
spisok.sort(key=len, reverse=True)
print(spisok[1:3])



