import logging
from time import sleep
logging.basicConfig(level=logging.DEBUG)
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        logging.debug(f"writeing report: {repr(report)}")
        fd.write(report.encode())


def hid_encoder(key, modifier=[]):
    logging.debug(f"{key= } {modifier= }")
    keys ={"a":4}
    for num,key1 in enumerate("****abcdefghijklmnopqrstuvwxyz1234567890!*'> ß´ü+##öä^,.-ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        keys[key1] = num

    mod = 0
    if "shift" in modifier:
        mod + 1
    if "ctrl" in modifier:
        mod + 2
    if "alt" in modifier:
        mod + 4
    if "gui" in modifier:
        mod + 8
    logging.debug(f"encoding key: {key} as {repr(keys[key])}")
    write_report(chr(mod) + chr(0) + chr(keys[key]) + chr(0) * 5)
    write_report(chr(0)*8)
    keys ={"a":4}

def text_encode(text):
    for i in text:
        if key == "/":
            mod = ["shift"]
            i = "7"
        if key == ":":
            mod = ["shift"]
            i = "."
        if key == "?":
            mod = ["shift"]
            i = "ß"
        if key == "=":
            mod = ["shift"]
            i = "0"
        hid_encoder(i, mod)


write_report(chr(8) + chr(0) + chr(21) + chr(0) * 5)
hid_encoder("r", ["gui"])
sleep(.5)
text_encode("microsoft-edge:https://www.youtube.com/watch?v=dQw4w9WgXcQ!")

'''
while True:
    for i in input():
        hid_encoder(i)
'''

