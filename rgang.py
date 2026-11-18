import os, time

print("="*40)
print("  R G A N G   T O O L S  v1.0")
print("  by Courage15")
print("="*40)
print("")
print("[1] Check IP")
print("[2] System Info")
print("[3] Exit")
print("")

choice = input("Choose > ")

if choice == "1":
    os.system("curl -s ifconfig.me; echo")
elif choice == "2":
    os.system("uname -a")
else:
    print("Bye RGANG!")
