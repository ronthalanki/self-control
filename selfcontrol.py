#!/usr/bin/env python3

import datetime
import subprocess
import os


def main():
    if open("/Users/sthalanki/dev/self_control/env.txt", "r").read() == "1":
        date = (datetime.datetime.utcnow() + datetime.timedelta(seconds=(60 - 1))
                ).strftime("%Y-%m-%dT%H:%M:%S") + "+0000"
        path = "/Users/sthalanki/dev/self_control"
        config = open(path + "/config.txt","r").read().strip()
        config_path = f"{path}/{config}.selfcontrol"
        cmd = f'sudo /Users/sthalanki/Applications/SelfControl.app/Contents/MacOS/org.eyebeam.SelfControl $(id -u $(whoami)) --install {config_path} {date}'
        subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    main()

