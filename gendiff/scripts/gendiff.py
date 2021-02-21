import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate diff.')
    parser.add_argument('first_file')

    parser.add_argument('second_file')

    parser.add_argument(
        '-f',
        '--format',
    )

    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()