#!/usr/bin/env python3
import argparse
from gendiff.diff_generator import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        dest='format',
                        default='stylish',
                        choices=['plain', 'stylish', 'json'],
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
