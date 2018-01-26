import webbrowser
import time
from pymouse import PyMouse
from pykeyboard import PyKeyboard

def open():
    webbrowser.open("https://www.baidu.com/")


var = 3
while var > 0:
    open()

    time.sleep(3)
    m = PyMouse()
    k = PyKeyboard()

    k.type_string('Hello, World!')
    time.sleep(2)
    m.click(1579, 108, 1)
    time.sleep(2)
    m.click(1149, 231, 1)
    time.sleep(5)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(1)
    m.click(1909, 480, 1)
    time.sleep(5)
    m.click(1899, 23, 1)
    var = var - 1
    time.sleep(3)

print("Good bye!")