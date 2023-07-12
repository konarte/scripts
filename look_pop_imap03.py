import socket, sys

#domain = sys.argv[1]  # получаем доменное имя из командной строки
domain = 'microsoft.com'
# преобразуем доменное имя в список IP-адресов
ips = socket.getaddrinfo(domain, 0)

for ip in ips:
    # проверяем доступность каждого IP-адреса
    try:
        telnet = socket.create_connection((ip[4][0], int(ip[4][1])))
        telnet.send('HELLO\r\n')
        telnet.close()
        print('IP-адрес %s доступен' % ip[4][0])
    except Exception as ex:
        print('%s: %s' % (ip[4][0], ex))
