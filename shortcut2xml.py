# -*- coding: utf-8 -*-
r"""shortcut2xml.py converts a .shortcut file ()== INFILEPATH) to xml Producing ORIGFILENAME.xml
Usage:   shortcut2xml.py INFILEPATH 
Example: shortcut2xml.py myInFileName.shortcut    PRODUCES  myInFileName.xml
Ex2:     python fun1\shortcut2xml.py fun1\shortcuts\SendHowdyTextToSelf.shortcut
"""
# --------------------------------------------------------------------------
# Copyright (c) 2019 Joe Dorocak  (joeCodeswell at gmail dot com)
# Distributed under the MIT/X11 software license, see the accompanying
# file license.txt or http://www.opensource.org/licenses/mit-license.php.
# --------------------------------------------------------------------------

import sys, os
import plistlib

def shortcut2xml(INFILEPATH):

    with open(INFILEPATH, 'rb') as fp:
        pl = plistlib.load(fp)  # fmt=None  => autodetect
    plBytesObj = plistlib.dumps(pl,  fmt=plistlib.FMT_XML, sort_keys=True, skipkeys=False)

    head, tail = os.path.split(INFILEPATH)
    OUTFILEPATH = os.path.join(head, os.path.splitext(tail)[0]+'.xml')
    f = open(OUTFILEPATH, 'w'); f.write(plBytesObj.decode("utf-8")); f.close()

 
NUM_ARGS = 1
def main():
    args = sys.argv[1:]
    if len(args) != NUM_ARGS or "-h" in args or "--help" in args:
        print (__doc__)
        sys.exit(2)
    shortcut2xml(args[0])
 
if __name__ == '__main__':
    main()
