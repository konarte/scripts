import os
import sys

i=0
number=0
name=''
liner = []
number_str=''
name_dir='_'
name_file = 'D:/Denwer/БТСО-01-16.txt'
f = open(name_file,'r')
#for i in open(name_file).readlines():
    #lst.append(dict(number=i, name=))

#f.close()
#print (lst)

for line in open(name_file):
    liner.append(line.split(' '))
    number_str=liner[i][0:1]
    if len(number_str)<2:
        number_str='0'+number_str
    print(number_str)
    i+=1
    
                             

f.close()

print(liner[2][0:1])
print(liner[2][1:2])
print(liner[2][2:3])
print(liner[2][3:4])
#['3']
#['Бобков']
#['Сергей']
#['Михайлович\n']
