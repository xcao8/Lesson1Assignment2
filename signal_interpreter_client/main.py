import os
from argparse import ArgumentParser
import logging
import logging.config
import yaml

try:
    from get_interpretation import get_interpretation
except ImportError:
    from signal_interpreter_client.get_interpretation import get_interpretation

os.chdir(os.path.dirname(os.path.dirname
                         (os.path.realpath(__file__))))

with open(r'cfg\logger_configuration.yaml', "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = ArgumentParser(description="Interpret signal using server")
    parser.add_argument("-s", "--signal", required=True, help="signal (e.g. 11)")
    return parser.parse_args()


def main():
    args = parse_arguments()
    logger.info("Signal get from command line: %s", args.signal)
    interpretation = get_interpretation(args.signal)
    print(interpretation)


def init():
    if __name__ == "__main__":
        main()


init()
