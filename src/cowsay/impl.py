from ascii_announcers import announcers, hello
import textwrap
import os
import math
from colored import Style, fore

def framed(announcer, text, width=30):
    coll = textwrap.wrap(text, width=width) if text else []
    if len(coll) == 0:
        coll = [hello.get(announcer,"...")]
    frame_width = max(len(s) for s in coll)
    frame_height = len(coll)
    header = " " + "_" * (frame_width + 2) + " "
    footer = " " + "-" * (frame_width + 2) + " "
    ret = [header]
    for idx, x in enumerate(coll):
        indent = frame_width - len(x)
        indent_l = math.floor(indent / 2)
        indent_r = indent - indent_l
        def linef(prefix, suffix):
            ret.append(prefix + (" " * indent_l) + x + (" " * indent_r) + suffix)
        if frame_height == 1:
            linef("< "," >")
        elif idx == 0:
            linef("/ "," \\")
        elif idx == frame_height - 1:
            linef("\\ ", " /")
        else:
            linef("| ", " |")
    ret.append(footer)
    return os.linesep.join(ret)

def speaking(text, c="\\"):
    coll = text.splitlines()
    if len(coll) < 2:
        coll = [""] * (2 - len(coll)) + coll
    ret = []
    for idx, x in enumerate(coll):
        if idx == 0:
            ret.append("   " + c + "  " + x)
        elif idx == 1:
            ret.append("    " + c + " " + x)
        else:
            ret.append("      " + x)
    return os.linesep.join(ret)

def announce(text, color, think, announcer):
    announcer = announcer or "cow"
    color = color or "green"
    c = "o" if think else "\\"
    print(fore(color) + framed(announcer, text) + Style.reset)
    print(speaking(announcers.get(announcer,"?"), c))
