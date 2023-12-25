import argparse
from gendiff import generate_diff


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file', type=str, help='first configuration file')
    diff.add_argument('second_file', type=str, help='second configuration file')
    diff.add_argument('-f', '--format',
                      choices=['stylish', 'plain', 'json'],
                      help='set format of output (default: stylish)',
                      default='stylish')
    args = diff.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
