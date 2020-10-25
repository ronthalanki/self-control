#!/usr/bin/env python3

import time


def _edit_file(x):
    file = open("config.txt","w")
    file.write(x)
    file.close()


def main(config):
    _edit_file(config)
    time.sleep(10 * 60) # 10 minutes
    _edit_file("max")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Start SelfControlApp')
    parser.add_argument('--config', type=str, default="work", help='config file to use with self control')
    args = parser.parse_args()

    main(args.config)
