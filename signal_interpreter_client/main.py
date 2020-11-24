from argparse import ArgumentParser
from signal_interpreter_client.get_interpretation import get_interpretation


def parse_arguments():
    parser = ArgumentParser(description="Interpret signal using server")
    parser.add_argument("-s", "--signal", required=True, help="signal (e.g. 11)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    interpretation = get_interpretation(args.signal)
    print(interpretation)


def init():
    if __name__ == "__main__":
        main()


init()
