# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.142.245", "192.168.109.50", "192.168.108.70", "192.168.101.49", 
              "192.168.141.242", "10.0.0.6", "10.0.0.7", "10.0.0.8"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses_list = ["192.168.100.241", "192.168.107.106", "192.168.142.245", "192.168.109.50", 
                "10.0.0.9", "10.0.0.10"]

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
               
for i in ip_addresses_list:
	if i in allow_list:
		print("IP is allowed")
	else:
		print("IP is not allowed. Further investigatino of login activity required")
		break