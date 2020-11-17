import argparse
import get_interpretation

parser = argparse.ArgumentParser()
parser.add_argument("--signal", help="value of ID for key 'signal' in JSON payload",type=str)
args = parser.parse_args()

def main():
    print(get_interpretation.get_interpretation(args.signal))



if __name__=="__main__" :
    main()