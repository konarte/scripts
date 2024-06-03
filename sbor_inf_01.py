import os
import sys
import shutil

error_in_mkdir=0
error_in_groupfile=0
i=0
number=0
name=''
group=''
db_fils = [[],[]]
file_list=[]
name_file = ''
name_file_output = 'inf_fils.log'
name_dir = os.getcwd()

f_log = open(name_file_output,'w')


# читаем все файлы в каталоге
file_list = [os.path.abspath(i) for i in os.listdir(name_dir) if os.path.isfile(os.path.join(name_dir, i))]
print(file_list)

for name_file in file_list:
    i=i+1
    print(i,name_file)
    f = open(name_file,'r')
    for line in f:
        found = line.find("@", 1, 10)
        if found != -1:
            print(found)
    f.close()
        

     
f_log.close()

"""for word in line.split('@'):            
            db_fls.append(name_file,word)
            print(word)"""

'''f = open(name_file,'r')
for line in open(name_file):
    for word in line.split(' '):
        #print ('A----------->',word)       
        #проверка на пробелы, сюда добавить табуляторы
        if word.isspace():
            error_in_groupfile+=1
            break
        if len(word)<2:
            word='0'+word
        if word[-1]=='\n':
            word=word[0:-1]
        #print ('Z----------->',word)
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
        error_in_mkdir+=1
print('Обработано ',i, ' человек, ', 'ошибок в файле группы:', error_in_groupfile)
print('Каталоги созданы, подходящие файлы перенесены, ошибок создания:', error_in_mkdir)


'''
