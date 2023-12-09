# importing libaries
import logging

# define log level
logging.basicConfig(level=logging.DEBUG)

def write_report(report):
    """writing a report to hid device"""
    with open('/dev/hidg0', 'rb+') as fd: # open hid device in secure way
        logging.debug(f"writeing report: {repr(report)}")# log writing the report
        fd.write(report.encode())# do the report


def hid_encoder(key, modifier=["shift"]):
    """encoding keys to hid codes"""
    logging.debug(f"{key= } {modifier= }")# log what is done

    # defining keys dictionary
    keys ={"a":4}
    for num,key1 in enumerate("abcdefghijklmnopqrstuvwxzy1234567890!*'> ß´ü+##öä^,.-", 4):
        keys[key1] = num# complete the dictionary
    
    mod = 0#define mod byte
    if "shift" in modifier:
        mod + 2# sets mod bit for shift to 1 if modifier shift is passed into parameterarray modifier
    if "ctrl" in modifier:
        mod + 1# sets mod bit for ctrl to 1 if modifier ctrl is passed into parameterarray modifier
    if "alt" in modifier:
        mod + 4# sets mod bit for alt to 1 if modifier alt is passed into parameterarray modifier
    if "gui" in modifier:
        mod + 8# sets mod bit for gui(windows) to 1 if modifier gui is passed into parameterarray modifier
    logging.debug(f"encoding key: {key} as {repr(keys[key])}")# log encoding
    write_report(chr(mod) + chr(0) + chr(keys[key]) + chr(0) * 5)# write hid report to set the keys
    write_report(chr(0)*8)# write hid report to release all keys

def text_encode(text):# define function text encode
    """encoding text to hid"""
    for i in text: # iterate over string
        hid_encoder(i) # encode every character




