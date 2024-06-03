import os # for functions: walk, path.join, remove, path.getsize, path.get[cam]time, mkdir
import fnmatch # fnmatch
import shutil # copy, move
import datetime # datetime.fromtimestamp
 
# копирование или перемещение, проверка на наличие уже существующего файла или каталога
def func_copymove(whatdo,l,dp):
    newdir = input('Имя каталога: ')
    newdir = os.path.join(dp,newdir)
    while os.path.isdir(newdir): # пока вводится имя существующего каталога
        print('Такой каталог уже есть!')
        newdir = input('Имя каталога: ')
        newdir = os.path.join(dp,newdir)
    os.mkdir(newdir)
    index = 0
    for i in l:
        future_file = i.split('/')
        future_file2 = future_file[-1].split('\\')
        future_file = future_file[0:-1] + future_file2
        if not os.path.isfile(newdir+'/'+future_file[-1]):
            if whatdo == 'c':
                shutil.copy(i,newdir)
            elif whatdo == 'm':
                shutil.move(i,newdir)
        else:
            newdir2 = newdir + '/' + future_file[-2]
            if not os.path.isdir(newdir2):                
                os.mkdir(newdir2) # каталог в каталоге
                if whatdo == 'c':
                    shutil.copy(i,newdir2)
                elif whatdo == 'm':
                    shutil.move(i,newdir2)
            else:
                if not os.path.isfile(newdir2+'/'+future_file[-1]):
                    if whatdo == 'c':
                        shutil.copy(i,newdir2)
                    elif whatdo == 'm':
                        shutil.move(i,newdir2)
                else:
                    newdir2 = newdir + '/'  + future_file[-2] + str(index)
                    index += 1
                    os.mkdir(newdir2)
                    if whatdo == 'c':
                        shutil.copy(i,newdir2)
                    elif whatdo == 'm':
                        shutil.move(i,newdir2)
 
# копирование, перемещение и удаление файлов
def func_whatdo(l,dp):
    whatdo = input('Действие (c-копировать,m-переместить,r-удалить,\
0-ничего не делать): ')
    if whatdo == 'c':
        print('Каталог с копиями будет находиться в', dp)
        func_copymove('c',l,dp)
    elif whatdo == 'm':
        print('Каталог для перемещаемых файлов будет находиться в', dp)
        func_copymove('m',l,dp)               
    elif whatdo == 'r':
        confirm = input('Запрашивать подтверждение на удаление каждого файла\
 (y/n): ')
        if confirm == 'n':
            for i in l:
                os.remove(i)
        else:
            for i in l:
                yes_no = input('Удалить файл ' + i + ' (y/n): ')
                if yes_no == 'y':
                    os.remove(i)
 
#поиск по шаблону
def func_pattern(dp,pat):
    l = []
    for r,d,f in os.walk(dp):
        for i in f:
            if fnmatch.fnmatch(i,pat):
                l.append(os.path.join(r,i))
    qty = len(l)
    print('Найдено',qty,'файлов')
    if qty > 0:
        func_whatdo(l,dp)
 
#поиск по размеру
def func_size(dp,ml,s):
    l = []
    for r,d,f in os.walk(dp):
        for i in f:
            filepath = os.path.join(r,i)
            filesize = (os.path.getsize(filepath)) // 1024
            if ml == '<' and filesize < s:
                l.append(filepath)
            elif ml == '>' and filesize > s:
                l.append(filepath)
    qty = len(l)
    print('Найдено',qty,'файла(ов)')
    if qty > 0:
        func_whatdo(l,dp)
 
#поиск по диапазону размеров
def func_size2(dp,lsize,usize):
    l = []
    for r,d,f in os.walk(dp):
        for i in f:
            filepath = os.path.join(r,i)
            filesize = (os.path.getsize(filepath)) // 1024
            if lsize <= filesize <= usize:                    
                l.append(filepath)
    qty = len(l)
    print('Найдено',qty,'файлов')
    if qty > 0:
        func_whatdo(l,dp)
 
#поиск по времени (три функции ниже)
def func_datetransform(datestring): # преобразование даты-строки в список чисел
    datelist = datestring.split('.')
    j = 0
    for i in datelist:
        datelist[j] = int(i)
        j += 1
    return datelist
 
def quantitydays(datelist): # подсчет количества дней от начала года
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    qdays = 0
    i = 1
    while i < datelist[1]:
        qdays = qdays + month[i-1]
        i += 1
    qdays = qdays + datelist[0]
    return qdays
 
def func_time(dp,fdate,sdate,typetime):
    l = []
    date1 = func_datetransform(fdate)
    date2 = func_datetransform(sdate)
    for r,d,f in os.walk(dp):
        for i in f:
            filepath = os.path.join(r,i)
            if typetime == 'c':
                time = os.path.getctime(filepath)
            elif typetime == 'a':
                time = os.path.getatime(filepath)
            elif typetime == 'm':
                time = os.path.getmtime(filepath)
            time = datetime.datetime.fromtimestamp(time)
            time = time.timetuple()
            datefile = []
            datefile.append(time[2])
            datefile.append(time[1])
            datefile.append(time[0])
            if date1[2] < datefile[2] < date2[2]:
                l.append(filepath)
            elif date1[2] == datefile[2] and date2[2] == datefile[2]:
                days1 = quantitydays(date1)
                days2 = quantitydays(date2)
                days = quantitydays(datefile)
                if days1 <= days <= days2:
                    l.append(filepath)
            elif date1[2] == datefile[2] and datefile[2] < date2[2]:
                days1 = quantitydays(date1)
                days = quantitydays(datefile)
                if days1 <= days:
                    l.append(filepath)
            elif date1[2] < datefile[2] and datefile[2] == date2[2]:
                days2 = quantitydays(date2)
                days = quantitydays(datefile)
                if days <= days2:
                    l.append(filepath)
    qty = len(l)
    print('Найдено',qty,'файла(ов)')
    if qty > 0:
        func_whatdo(l,dp)
 
#ИНТЕРФЕЙС
dirpath = input('Путь к каталогу | The path: ')
while not os.path.exists(dirpath) and not os.path.isdir(dirpath): #проверка пути
    print('Такого каталога нет | There is no this directory')
    dirpath = input('Путь к каталогу | The path: ')
 
option =  input('Параметр сортировки (1-шаблон,2-размер,3-диапазон,4-время)\
 | Search option (1-pattern,2-size,3-range,4-time): ')
 
print("Для отказа введите 'n'!")
if option == '1':
    pattern = input('Шаблон имени файла | Template for filename: ')
    while pattern != 'n':
        func_pattern(dirpath,pattern)
        pattern = input('Шаблон имени файла | Template for filename: ')
elif option == '2':
    moreless = input('Меньше или больше определенного размера (<-меньше,>-больше)\
 | Less or more then a certain size (<-less,>-more): ')
    size = int(input('Размер (в Кб) | The size (Kb): '))
    func_size(dirpath,moreless,size)
elif option == '3':
    minsize = int(input('Нижняя граница размера (в Кб)\
 | The lower limit of the size (Kb): '))
    maxsize = int(input('Верхняя граница размера (в Кб)\
 | The upper limit of the size (Kb): '))
    func_size2(dirpath,minsize,maxsize)
elif option == '4':
    fromdate = input('Начиная с даты | From the date of: ')
    enddate = input('Заканчивая датой | Ending the date: ')
    kinddate = input('Поиск по времени создания(c), открытия(a), изменения(m)\
 | Search by time of create(c), open(a), change(m): ')
    func_time(dirpath,fromdate,enddate,kinddate)
