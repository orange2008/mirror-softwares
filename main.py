#!/usr/bin/env python3
import requests
import json
import os
import time

# Start timer
t = time.time()

# Global functions
def download(url):
    os.system('wget "' + url + '"')
    return True


# Constants
# Parent directories
parent_directory = "./target"
# First layer directories
layer1 = [
    "./target/clash",
    "./target/element",
    "./target/telegram"
]
# Second layer directories
layer2 = [
    "./target/clash/Clash-for-Windows",
    "./target/clash/Clash-for-Android",
    "./target/element/Element-for-Android",
    "./target/element/Element-for-Desktop"
]
# Others
clash_for_windows_releases = "https://api.github.com/repos/Fndroid/clash_for_windows_pkg/releases"
clash_for_windows_dir = "./target/clash/Clash-for-Windows"
clash_for_windows_back = "../../../"
clash_for_android_releases = "https://api.github.com/repos/Kr328/ClashForAndroid/releases"
clash_for_android_dir = "./target/clash/Clash-for-Android"
clash_for_android_back = "../../../"
element_for_android_releases = "https://api.github.com/repos/vector-im/element-android/releases"
element_for_android_dir = "./target/element/Element-for-Android"
element_for_android_back = "../../../"
element_for_desktop_releases_dir = "./target/element/Element-for-Desktop"
element_for_desktop_releases_back = "../../../"
element_for_desktop_releases = [
    "https://packages.riot.im/desktop/install/win32/x64/Element%20Setup.exe",
    "https://packages.riot.im/desktop/install/win32/ia32/Element%20Setup.exe",
    "https://packages.riot.im/desktop/install/macos/Element.dmg"
]
telegram_releases_dir = "./target/telegram"
telegram_releases_back = "../../"
telegram_releases = [
    "https://telegram.org/dl/android/apk",
    "https://telegram.org/dl/macos",
    "https://telegram.org/dl/desktop/mac",
    "https://telegram.org/dl/desktop/win64",
    "https://telegram.org/dl/desktop/win64_portable",
    "https://telegram.org/dl/desktop/win",
    "https://telegram.org/dl/desktop/win_portable",
    "https://telegram.org/dl/desktop/linux"
]

# Purging all old directories
os.system("rm -rf " + parent_directory)

# Create all new directories
os.mkdir(parent_directory)
for directories in layer1:
    os.mkdir(directories)
for directories in layer2:
    os.mkdir(directories)

# Clash for Windows
req = requests.get(clash_for_windows_releases).json()
body = req[0]
assets = body['assets']
os.chdir(clash_for_windows_dir)
for child in assets:
    download(child['browser_download_url'])
os.chdir(clash_for_windows_back)

# Clash for Android
req = requests.get(clash_for_android_releases).json()
body = req[0]
assets = body['assets']
os.chdir(clash_for_android_dir)
for child in assets:
    download(child['browser_download_url'])
os.chdir(clash_for_android_back)

# Element for Android
req = requests.get(element_for_android_releases).json()
body = req[0]
assets = body['assets']
os.chdir(element_for_android_dir)
for child in assets:
    download(child['browser_download_url'])
os.chdir(element_for_android_back)

# Element for Desktop
os.chdir(element_for_desktop_releases_dir)
os.system("wget -O ElementSetup_win64.exe " + element_for_desktop_releases[0])
os.system("wget -O ElementSetup_ia32.exe " + element_for_desktop_releases[1])
os.system("wget -O Element.dmg " + element_for_desktop_releases[2])
os.chdir(element_for_desktop_releases_back)

# Telegram
os.chdir(telegram_releases_dir)
os.system("wget -O Telegram.apk " + telegram_releases[0])
os.system("wget -O Telegram.dmg " + telegram_releases[1])
os.system("wget -O Telegram-for-Desktop.dmg " + telegram_releases[2])
os.system("wget -O Telegram_win64.exe " + telegram_releases[3])
os.system("wget -O Telegram_win64_portable.zip " + telegram_releases[4])
os.system("wget -O Telegram_ia32.exe " + telegram_releases[5])
os.system("wget -O Telegram_ia32_portable.zip " + telegram_releases[6])
os.system("wget -O Telegram.tar.xz " + telegram_releases[7])
os.chdir(telegram_releases_back)

# End
t_e = time.time()
t_elapsed = t_e - t
print("\nCompleted. Elapsed Time: " + str(t_elapsed) + "s")