import urllib.request as requests, subprocess, sys, os
from threading import Thread as td

successCount = 0
failCount = 0
total = 0

def openURL():
    global successCount, failCount, total
    while True:
        try:
            requests.urlopen("http://localhost").read()
            successCount = successCount + 1
            total = total + 1
            sys.stdout.write(u"\x1b[1A" + u"\x1b[2K" + "\rTotal: %s | Successful: %s | Failed: %s\nThese values are approximations!" % (total, successCount, failCount))
        except Exception as err:
            failCount = failCount + 1
            total = total + 1
            sys.stdout.write(u"\x1b[1A" + u"\x1b[2K" + "\rTotal: %s | Successful: %s | Failed: %s\nThese values are approximations!" % (total, successCount, failCount))


os.system("cls")
while True:
    td(target=openURL).start()