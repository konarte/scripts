import socket
ip=[]
def check_mail_servers(ip):
    
    for port in (110, 143, 993, 465, 587):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((ip, port))
                print(f"Successfully connected to {port} on {ip}")
                break
        except Exception as e:
            print(f"{e} when connecting to {ip}:{port}")
    else:
        return True
    return False

def domen_lookup_ip(domain):
    ip = socket.gethostbyname_ex(domain)
    if ip is None:
        print(f"Error resolving IP address for {domain}")
        return False
    return ip
    
# Пример использования
if __name__ == "__main__":
    #domain = input("Enter domain name (example.com): ")
    domain = 'microsoft.com'
    domen_lookup_ip(check_mail_servers(ip))
    
    #result = check_mail_servers(domain)
    #print(f"Result: {result}")
