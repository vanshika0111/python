import numpy as np
Students_Data = {'s1':{'id':1,'name':'Vanshika','marks':10},
                 's2':{'id':2,'name':'Rishika','marks':20},
                 's3':{'id':3,'name':'Pooja','marks':30},
                 's4':{'id':4,'name':'Tejas','marks':40},
                 's5':{'id':5,'name':'Meet','marks':50}}
print(Students_Data.keys())
Students_Data['s6']={'id':6,'name':'pointer','marks':60}
Students_Data['s3'].get('name')
search = input("enter the key no. : ")
# updating through update and looping
for i in Students_Data :
 if i == search :
  id = int(input("enter the id : "))
  name = input("enter the name : ")
  marks = int(input("enter the marks : "))
  Students_Data[i].update({'id':id,'name':name,'marks':marks})
# adding values into list
Students_list = []
for i in Students_Data:
  lis = []
  for j in Students_Data[i].values():
    lis.append(j)
  Students_list.append(lis)
print(Students_list)
# adding values in list through constructor
Students_list_constructor = []
for i in Students_Data:
  lis2 = list(Students_Data[i].values())
  Students_list_constructor.append(lis2)
print(Students_list_constructor)
# count and display number of students
print(len(Students_Data))
# remove all details from dictionary
Students_Data.clear()
# adding array in dictionary
name = ['Ruchita','Sakshi','Bansari','Vishwa','Janvi']
score = [10,20,30,40,50]
attempts = [1,2,3,4,1]
qualify = ['yes','no','yes','no','yes']
arrname = np.array(name)
arrscore = np.array(score)
arrattempts = np.array(attempts)
arrqualify = np.array(qualify)
exam_data_array={'name':arrname,'score':arrscore,'attempts':arrattempts,'qualify':arrqualify}
exam_data_array
# adding list in dictionary
lisname = ['Vanshika','Lily','Ryle','Atlas']
lisscore = [10,20,30,40]
lisattempts = [1,2,3,4]
lisqualify = ['no','yes','no','yes']
exam_data_array2 ={'name':lisname,'score':lisscore,'attempts':lisattempts,'qualify':lisqualify}
exam_data_array2