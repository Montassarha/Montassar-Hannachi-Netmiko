from netmiko import ConnectHandler

def acces_netmiko():
    router = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    connection = ConnectHandler(**router)

    # Affiche la date côté routeur
    clock = connection.send_command("show clock")
    print("Date du routeur :")
    print(clock)

    # Affiche les interfaces et les sauvegarde dans un fichier
    interfaces = connection.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

    connection.disconnect()

def dire_bonjour():
    print("Hello, Git!")

if __name__ == "__main__":
    dire_bonjour()
    acces_netmiko()
