import argparse
import sys

import messages.findit_pb2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_file', help='Input filename')
    parser.add_argument('out_file', help='Output filename')

    args = parser.parse_args()

    with open(args.in_file, 'rb') as f:
        proto = messages.findit_pb2.RecognitionRequest()
        proto.payload  = f.read()

    with open(args.out_file, 'wb') as f:
        f.write(proto.SerializeToString())


