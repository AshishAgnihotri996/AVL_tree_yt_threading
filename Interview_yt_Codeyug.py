# import sys
#
# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))
# print(a is b)  # id is checked
# print(a==b) # value is checked


# min and max to find manually

# nums = [45,78,12,46,98,66,43,21,63,87,89,91]
# max = nums[0]
# for i in nums:
#     if i < max:
#         max = i
#     else:
#         i+=1
# print(max)
#
# lang1 = ['marathi','hindi','gujrati','urdu']
# lang2 = ['english','frech','japnese']
# #
# # for i in lang2:
# #     lang1.append(i)
# # print(lang1)
# lang1.extend(lang2)
# print(lang1)


# to fetch the last element in the dictionary
# dict = {'ashish':10,'choti':20,'mona':30,'akash':40}
# x = list(dict.items())
# print(x[-1])

# join
#
# a = ['ashish','agnihoatri']
#
# x = "-->".join(a)
# print(x)

#SPLIT

# msg = "i want to become a python programmer"
# cunt = "india,us,china,jpan"
# x = cunt.split(",",2) #--> by default its a white space
# print((x))


#recerse a content

#0 str1 = input('enter the strting')
# str1 =str1.split()
# li =[]
# for i in str1:
#     li.append(i[::-1])
# x = "->".join(li)
# print(x)
#
# def printDuplicates(arr):
#     d = []
#     for i in arr:
#         if arr.count(i) > 1 and i not in d:
#             d.append(i)
#     print(d)
# arr = ["hello",10,20,40,20,60,40,30]
# printDuplicates(arr)

# 2 method

# l = ['hello',10,20,30,40,50,60,40,10,20,20,30]
# d= []
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] == l[j] and l[i] not in d:
#             d.append(l[i])
# print(d)

#tp count the number of items having list as value

# dict = {'jay':['male',23,20000],'raj':25,'vicky':['male',22],'ram':['male',23]}
# count = 0
# for i in dict:
#     if isinstance(dict[i],list):
#         count +=1
# print(count)


#
# str1 = 'ashish agnihotri'
# vw=['a','e','i','o','u']
# count = 0
# for i in str1:
#     if i in vw:
#         count +=1
# print(count)


#reverse a string
# name = input('enter your name')
# r_name =" "
# count = len(name)
# # while count > 0:
# #     r_name = r_name + name[count-1]
# #     count -=1
# for i in name:
#     r_name = i + r_name
# print(r_name)

# while with else statement

# i =1
# while i <=3 :
#     print('outer loop')
#     j =1
#     while j <= 3:
#         print('inner loop')
#         j+=1
#     i+=1

# str1 = input('enter the string')
# n  = int(input('enter the count'))
# str1 = str1.split()
# count = dict()
# for word in str1:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word] =1
# word_list = []
# for key in count:
#     if count[key] >= n:
#         word_list.append(key)
# if len(word_list) > 0 :
#     print(word_list)

#menu driven

# while True:
#     num1 = int(input('enter the first no'))
#     num2 = int(input('enter the second no'))
#     print('1.addition \n 2.subs \n 3.mul \n 4.div')
#     choice = int(input('choose from above'))
#     if choice == 1:
#         print('addition is',num1 + num2)
#     elif choice==2:
#         print('subs is', num1 + num2)
#     else:
#         print('invlaid choice')
#     ans = input('do u eant to contiue')
#     ans = ans.lower()
#     if ans!='y':
#         break


#armstrong number  1- -100

# for i in range(1,1001):
#     num = i
#     n = len(str(i))
#     sum = 0
#     i = str(i)
#     for digit in i:
#         sum = sum + int(digit)**2
#     if sum == num:
#         print(num)

#perfect numbers
# num = int(input('enter the number to check wheather ists a perfect num or not'))
#
# def  perfectNum(num):
#     sum = 0
#     for i in range(1,num):
#         if num % i== 0:
#             sum = sum +i
#     if num ==sum:
#         print('perfect number')
#     else:
#         print('not a perfect number')
# perfectNum(num)

# 3b4f3f
#
# def Solution(arr):
#     output = ""
#     for char in arr:
#         if char.isalpha():
#             var = char
#         else:
#             num = int(char)
#             output = output+(var*num)
#     print(output)
# arr = 'b4f5g6h3t7'
# Solution(arr)