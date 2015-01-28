#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright @ 2015
#
# Author: jaypei <jaypei97159@gmail.com>
#

import os
from serial import Serial
import cStringIO


SERIAL_DEV = "/dev/ttyACM0"
SERIAL_RATE = 9600
KEY_MAP = {
    "0xFF629D": "Up",
    "0xFFA857": "Down",
    "0xFF22DD": "Left",
    "0xFFC23D": "Right",
    "0xFF629D": "Up",
    "0xFFA25D": "Escape",
    "0xFF02FD": "space"
}
MOTD = ur"""
 _________________________
< 主人, 记得休息 10 分钟. >
 -------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""


def press_key(key):
    os.system("xdotool key %s" % key)
    print key


def process_command(cmd):
    print cmd
    global KEY_MAP
    cmd = cmd.strip()
    pkey = KEY_MAP.get(cmd, None)
    if pkey:
        press_key(pkey)


def show_motd():
    global MOTD
    print MOTD


def main():
    global SERIAL_DEV, SERIAL_RATE
    show_motd()
    # open serial
    s = Serial(SERIAL_DEV, SERIAL_RATE)
    buf = cStringIO.StringIO()
    while True:
        c = s.read()
        buf.write(c)
        if c == "\n":
            process_command(buf.getvalue())
            buf.reset()
            buf.truncate()


if __name__ == "__main__":
    main()
