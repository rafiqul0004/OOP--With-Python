import pyautogui
from time import sleep
n=int(input())
sleep(5)
for i in range(n):
    for j in range(i+1):
        pyautogui.write("* ")
    pyautogui.write("\n")

