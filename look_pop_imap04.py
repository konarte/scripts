import socket, sys

#domain = sys.argv[1]  # получаем доменное имя из командной строки
domain = 'microsoft.com'
ports = [110, 143, 993, 465, 587] 
# преобразуем доменное имя в список IP-адресов
ips = socket.getaddrinfo(domain, 0)
print (ips)

for ip in ips:
        for port in ports:
                #print (ip[4][0],'---------', port)
                # проверяем доступность каждого IP-адреса
                try:
                        telnet = socket.create_connection((ip[4][0], int(port)))
                        telnet.send('HELLO\r\n')
                        telnet.close()
                        print('IP-адрес доступен: ',ip[4][0], 'Порт открыт: ', port)
                except Exception as ex:
                        print('%s: %s' % (ip[4][0], ex))
