#!/usr/bin/env python3

import time


def _edit_file(x):
    file = open("env.txt","w")
    file.write(x)
    file.close()


def main(duration: int):
    _edit_file("0")
    time.sleep(duration * 60)
    _edit_file("1")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Start SelfControlApp')
    parser.add_argument('--duration', type=int, default=5, help='length of disabling self control block in minutes')
    args = parser.parse_args()

    main(args.duration)
