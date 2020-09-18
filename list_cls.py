a = [23,45.67, 'python',34,"django"]
# print(type(a))
# print(a[0])
# print(a[4])
# print(a[1:5])
# print(a[-1:-4:-1])

# a = [23, 45.67, 'python', 34, "django"]
# print(a)
# a[1] = 76
# print(a)
# a[1:4] = [78,"datascience",67.43]
# print(a)
# del a[2]
# print(a)


#list methods

#append
# a = [34,'python','django',56]
# print(a)
# a.append('datascience')
# print(a)
# a.append([11,12,13])
# print(a)

#extend 
# a = [34,'python','django',56]
# a.extend('django')
# a.extend([11,12,13])
# print(a)

#insert
# a = [34,'python',"django",56]
# a.insert(2,45)
# a.insert(2,"datascience")
# a.insert(2,[45,46])
# print(a)

#remove 
# a = [34,'python',"django",56]
# a.remove('python')
# print(a)

#pop
# a = [34,'python',"django",56]
# a.pop(3)
# print(a)

#clear
# a = [34,'python',"django",56]
# a.clear()
# print(a)

#nested indexing
# a = [23, [11,12,13],"django", [51,52,53]]
# print(a[1][2])
# a[3].append(54)
# print(a)

#index
# a = [23, [11,12,13],"django", [51,52,53]]
# print(a.index('django'))

#count
# a = [23, [11,12,13],"django", [51,52,53]]
# print(a.count('django'))
# print(a.count('djan'))

#reverse
# a = [23, [11,12,13],"django", [51,52,53]]
# a.reverse()
# print(a)

#sort
# a = [34,24,67,54,89,54,75,12]
# a.sort()
# print(a)
# print(len(a))

# #looping example

# a = [64,63,82,54,96,79,32,55,65,96,31]
# even = []
# odd = []
# for j in a:
#     if j%2==0:
#         # print("even",j)
#         even.append(j)
#     else:
#         odd.append(j)
# print(even)
