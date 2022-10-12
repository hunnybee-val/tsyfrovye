lst = [1,2,3]
lst.append(4)
lst.remove(3)
print(lst)
print(lst[2])
lst.remove(2)
if 2 in lst:
    print('2 is in da list')
else:
    print('2 is NOT in da list')

tup = (1, 2, 3)

print(tup)

first, second, third = tup
print("1", first)

eng_rus_dict = {
    "cat":"кот",
    "car":"машина"
}
print(eng_rus_dict['cat'])

if tup == None :
    print("hi!")
else :
    print("hi!!!")