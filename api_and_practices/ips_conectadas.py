import nmap

scanner = nmap.PortScanner()

ip =  input("Please IP: ")
print("esta es la ip que escribiste", ip)
scanner.scan(ip)

print(scanner.all_hots())   


