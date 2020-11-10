import argparse
import server_communication_handler as client

parser = argparse.ArgumentParser()
parser.add_argument("--signal", help="value for key 'signal' in JSON payload",type=str)
args = parser.parse_args()

def main():
    client.post_message(url, payload)

if __name__=="__main__" :
    url = "http://127.0.0.1:5000/"
    payload={"signal": args.signal}
    main()