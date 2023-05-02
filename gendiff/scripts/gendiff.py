import argparse


def main():
    diff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    diff.add_argument('first_file', type=str, help='first configuration file')
    diff.add_argument('second_file', type=str, help='second configuration file')
    diff.add_argument('-f', '--format',
                      help='set format of output (default: stylish)')
    args = diff.parse_args()
    return args


if __name__ == '__main__':
    print(main())