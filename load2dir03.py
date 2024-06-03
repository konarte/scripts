import os
import sys

i=0
number=0
name=''
liner = []
file_list=[]
name_file = os.getcwd()+'/БТСО-01-16.txt'
name_dir = os.getcwd()

# читаем все файлы в каталоге
file_list = [os.path.abspath(i) for i in os.listdir(name_dir) if os.path.isfile(os.path.join(name_dir, i))]

try:
    f = open(name_file,'r')
    for line in open(name_file):
        for word in line.split(' '):
            if len(word)<2:
                word='0'+word
            if word[-1]=='\n':
                word=word[0:-1]
            print(word)
            liner.append(word)
except:
    print ('Error')
f.close()

#print(len(liner))
print('--------------------------------')
print('------СОЗДАНИЕ ПАПОК------------')
print('--------------------------------')


for i in range(0,(len(liner)-3),4):
    print(i)
    print('liner[',i,']= ',liner[i])
    print('liner[',i,'+1]= ',liner[i+1])
    print('liner[',i,'+2]= ',liner[i+2])
    print('liner[',i,'+3]= ',liner[i+3])
    print('--------------------------------')
    try:
        #os.mkdir(liner[i]+'_'+liner[i+1]+'_'+liner[i+2][0]+liner[i+3][0])
        print(liner[i]+'_'+liner[i+1]+'_'+liner[i+2][0]+liner[i+3][0])
    except:
        print('Error')
    #здесь поиск файла по фамилии и перенос в директорию
                      


#print(liner[1])
#print(liner[4])
#print(liner)
#print(liner[2][0:1])
#print(liner[2][1:2])
#print(liner[2][2:3])
#print(liner[2][3:4])
#['3']
#['Бобков']
#['Сергей']
#['Михайлович\n']

