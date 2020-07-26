#!/usr/bin/env python3

import datetime
import subprocess
import os


def main(config_path: str, duration: int):
    if open("/Users/sthalanki/dev/self_control/env.txt", "r").read() == "1":
        date = (datetime.datetime.utcnow() + datetime.timedelta(seconds=(duration * 60 - 1))
                ).strftime("%Y-%m-%dT%H:%M:%S") + "+0000"
        cmd = f'sudo /Users/sthalanki/Applications/SelfControl.app/Contents/MacOS/org.eyebeam.SelfControl $(id -u $(whoami)) --install {config_path} {date}'
        subprocess.call(cmd, shell=True)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Start SelfControlApp')
    parser.add_argument('--config', type=str, help='path to the config file')
    parser.add_argument('--duration', type=int, default=1, help='length of self control block in minutes')
    args = parser.parse_args()

    main(args.config, args.duration)

