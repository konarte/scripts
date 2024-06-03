import socket
import sys
import re
import urllib.request

def undotIPv4 (dotted):
    return sum (int (octet) << ( (3 - i) << 3) for i, octet in enumerate (dotted.split ('.') ) )

def dotIPv4 (addr):
    return '.'.join (str (addr >> off & 0xff) for off in (24, 16, 8, 0) )

def rangeIPv4 (start, stop):
    for addr in range (undotIPv4 (start), undotIPv4 (stop) ):
        yield dotIPv4 (addr)

print ("Поиск веб сайтов и веб мордочек в заданном диапазоне IP")
print ("У найденных ресурсов будет показан тег title")
print ("--------------------------------")
a = input("Введите начальный адрес IP диапазона: ")
b = input("Введите конечный адрес IP диапазона: ")
print ("--------------------------------")

for x in rangeIPv4 (a, b):
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((x, 80))
        print ("Соединяюсь с ",x)
    except socket.error:
        print ("Ошибка сокета на ",x)
        pass
    else:
        s.close
        try:
            doc = urllib.request.urlopen("http://"+x).read().decode('utf-8',errors='ignore')
            match = re.search( "<title>(.*)</title>", doc )
            if not(match is None):
                print (x + ": " + match.group())
                print ("----------")
        except Exception:
            pass

print ("--------------------------------")
print ("Процесс завершен")
