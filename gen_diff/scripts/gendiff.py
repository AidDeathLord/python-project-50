#!/usr/bin/env python3
import json
import argparse


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file', type=str, help='first configuration file')
    diff.add_argument('second_file', type=str, help='second configuration file')
    diff.add_argument('-f', '--format', help='set format of output')
    args = diff.parse_args()
    return generate_diff(args.first_file, args.second_file)


def generate_diff(first_path, second_path):
    first_file = json.load(open(first_path))
    second_file = json.load(open(second_path))

    result = []
    for key in list(first_file.keys()):
        if key in second_file:
            if first_file[key] == second_file[key]:
                result.append([' ', key, first_file.get(key)])
            else:
                result.append(['-', key, first_file.get(key)])
                result.append(['+', key, second_file.get(key)])
        else:
            result.append(['-', key, first_file.get(key)])

    for key in list(second_file.keys()):
        if key not in first_file:
            result.append(['+', key, second_file.get(key)])
    return correcting_output(result)


def correcting_output(diff_list):
    result = '{\n'
    for value in diff_list:
        result = result + f'  {value[0]} {value[1]}: {value[2]}\n'
    return result + '}'


if __name__ == '__main__':
    print(main())
