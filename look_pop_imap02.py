import socket

def check_all_mail_servers():
    all_ports = [110, 143, 993, 465, 587]
    ips = []
    
    def get_ips():
        for p in all_ports:
            try:
                with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
                    s.connect(("localhost", p))
                    ips.append(s.getsockname()[0])
            except Exception as e:
                print("Error when connecting to {}:{}".format(p, e))
    
    get_ips()
    
    return ips

# Проверка доступности всех почтовых серверов
ips = check_all_mail_servers()
print(f"Available mail servers:")
print("\t" + " ".join(str(ip) for ip in ips))
