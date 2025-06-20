import pydirectinput
import keyboard
from time import sleep

def start():
    while True:
        if(keyboard.is_pressed('del')):
            print("중지")
            break
        # 1번째 사이클
        print("Right 1번째 사이클 시작")
        pydirectinput.press('right')
        pydirectinput.press('right')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        pydirectinput.press('right')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        # 2번째 사이클
        if(keyboard.is_pressed('del')):
            print("중지")
            break
        print("Right 2번째 사이클 시작")
        pydirectinput.press('right')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        pydirectinput.press('right')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        if(keyboard.is_pressed('del')):
            print("중지")
            break
        print("Right 3번째 사이클 시작")
        pydirectinput.press('right')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        if(keyboard.is_pressed('del')):
            print("중지")
            break
        print("Left 1번째 사이클 시작")
        pydirectinput.press('left')
        pydirectinput.press('left')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        pydirectinput.press('left')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)

        if(keyboard.is_pressed('del')):
            print("중지")
            break
        print("Left 2번째 사이클 시작")
        pydirectinput.press('left')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        pydirectinput.press('left')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        if(keyboard.is_pressed('del')):
            print("중지")
            break
        print("Left 3번째 사이클 시작")
        pydirectinput.press('left')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('alt')
        sleep(0.1)
        pydirectinput.press('shift')
        sleep(0.1)
        if(keyboard.is_pressed('del')):
            print("중지")
            break
while True:
    if(keyboard.is_pressed('ins')):
        start()