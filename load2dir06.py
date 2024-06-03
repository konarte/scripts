import os
import sys
import shutil

i=0
number=0
name=''
group=''
liner = []
file_list=[]
name_file = ''
name_dir = os.getcwd()




# читаем все файлы в каталоге
file_list = [os.path.abspath(i) for i in os.listdir(name_dir) if os.path.isfile(os.path.join(name_dir, i))]
#file_list = [os.path.abspath(i) for i in os.listdir('D:/Denwer/') if os.path.isfile(os.path.join('D:/Denwer/', i))]
#print(file_list)
for name in file_list:# определяем файл списка по расширению
    if name [name.rfind('.'):] == '.list':
        name_file = name
        group=name[::-1]
        group = group[(group.find('\\')-1):4:-1]
        print('Найден список группы:',(group)) 
     
print('_________',name_file)    

'''

f = open(name_file,'r')
for line in open(name_file):
    for word in line.split(' '):
        if len(word)<2:
            word='0'+word
        if word[-1]=='\n':
            word=word[0:-1]
        liner.append(word)
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
    new_dir=liner[i]+'_'+liner[i+1]+'_'+liner[i+2][0]+liner[i+3][0]
    try:
        #os.mkdir(liner[i]+'_'+liner[i+1]+'_'+liner[i+2][0]+liner[i+3][0])
        os.mkdir(new_dir)
        print('Создание каталога======================================',new_dir)
        print('Ищу файлы для переноса.................')#здесь поиск файла по фамилии и перенос в директорию
        for j in range(0,(len(file_list))): #если есть фамилия в списке файлов
            if liner[i+1] in file_list[j]:
                print ('Нашлось: ',liner[i+1],' в ',file_list[j])
                #print (file_list[j],' ---------> ',(name_dir+'\\'+new_dir))
                shutil.move(file_list[j], (name_dir+'\\'+new_dir))
    except:
        print('Ошибка обработки')

# дальше проверям имя файла и записываем цифры с конца    
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

'''
