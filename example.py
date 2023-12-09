from main import text_encode, hid_encoder
from time import sleep

def main():
    hid_encoder("r", ["gui"])# open windows run dialog
    sleep(.5)# wait .5 seconds
    text_encode("microsoft-edge")
    hid_encoder(".", ["shift"])# :
    text_encode("https")
    hid_encoder(".", ["shift"])# :
    hid_encoder("7", ["shift"])# /
    hid_encoder("7", ["shift"])# /
    text_encode("www.youtube.com")# /
    text_encode("watch")
    hid_encoder("ẞ",["shift"]) # ?
    hid_encoder("v")
    hid_encoder("0",["shift"]) # =
    text_encode("dQw4w9WgXcQ!") # ! = [Enter]

if __name__ == "__main__":
    main()