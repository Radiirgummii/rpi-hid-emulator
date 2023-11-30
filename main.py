def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def hid_encoder(key, modifier=[]):
    keys ={"a":4}
    for num,key in enumerate("    abcdefghijklmnnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        keys[key] = num
    
    mod = 0
    if "shift" in modifier:
        mod + 1
    if "ctrl" in modifier:
        mod + 2
    if "alt" in modifier:
        mod + 4
    if "gui" in mod:
        mod + 8
    write_report(encode(chr(mod) + chr(0) + chr(keys[key] + chr(0) * 5)))

for i in range("    abcdefghijklmnnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    hid_encoder(i)
