#!/usr/bin/env python3
import json
import sys
import os
from pprint import pprint

directory = os.fsencode("../intents-complex/2 - resolvedParameterPrompts/")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".json"):
        tfFile = filename.replace(".json", "_rep.json")

        bs = "/"
        bseq = ("en_response", tfFile)
        bpath = bs.join(bseq)
        print(bpath)

        cs = "/"
        cseq = ("cn_response", tfFile)
        cpath = cs.join(cseq)
        print(cpath)

        if(os.path.isfile(bpath) and os.path.isfile(cpath)):
            os.rename(bpath, "en_com_response/"+tfFile)
            os.rename(cpath, "cn_com_response/"+tfFile)

        print("==================")
    else:
        print("END")

