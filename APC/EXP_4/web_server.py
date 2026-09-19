server_ip = ("192.168.1.10",)

allowed_ips = ["192.168.1.1", "192.168.1.2"]

def update_ips(ip):
    allowed_ips.append(ip)

print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

new_ip = input("Enter new allowed IP: ")
update_ips(new_ip)

print("\nUpdated Configuration:")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)
