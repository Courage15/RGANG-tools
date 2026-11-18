import os, socket, random, string, time

def banner():
    os.system("clear")
    print("="*40)
    print("  R G A N G   T O O L S  v2.0")
    print("  by Courage15")
    print("="*40)

while True:
    banner()
    print("[1] Check IP")
    print("[2] System Info")
    print("[3] Password Generator")
    print("[4] Port Scanner")
    print("[5] WiFi / Network Info")
    print("[0] Exit")
    print("")
    choice = input("Choose > ")

    if choice == "1":
        print("\nYour IP:")
        os.system("curl -s ifconfig.me; echo")

    elif choice == "2":
        os.system("uname -a")
        os.system("uptime")

    elif choice == "3":
        try:
            length = int(input("Password length (e.g 12) > "))
        except:
            length = 12
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        pwd = "".join(random.choice(chars) for _ in range(length))
        print(f"\nGenerated: {pwd}")

    elif choice == "4":
        host = input("Host to scan (e.g 127.0.0.1 or google.com) > ")
        print(f"Scanning {host}...")
        for port in [21,22,23,53,80,443,8080]:
            s = socket.socket()
            s.settimeout(1)
            try:
                s.connect((host, port))
                print(f"[OPEN] Port {port}")
            except:
                print(f"[CLOSED] Port {port}")
            s.close()

    elif choice == "5":
        os.system("ip addr | grep inet")
        os.system("termux-wifi-connectioninfo 2>/dev/null || echo 'WiFi info not available'")

    elif choice == "0":
        print("Bye RGANG!")
        break
    else:
        print("Invalid choice!")

    input("\nPress Enter to continue...")
