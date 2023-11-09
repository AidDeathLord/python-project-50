import argparse
from gendiff import generate_diff
from gendiff.formats.stylish import stylish


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file', type=str, help='first configuration file')
    diff.add_argument('second_file', type=str, help='second configuration file')
    diff.add_argument('-f', '--format',
                      help='set format of output (default: stylish)')
    args = diff.parse_args()
    return generate_diff(args.first_file, args.second_file, stylish)


if __name__ == '__main__':
    main()
