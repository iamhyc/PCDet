#!/usr/bin/env python3
import argparse
import subprocess as sp
import socketio
from enum import Enum

class State(Enum):
    INIT        = 0x01
    WAIT        = 0x02
    ERROR       = 0x0F
    pass

class Action(Enum):
    EVAL        = 0x10
    ERROR       = 0xF0
    pass

class FedClient(object):
    #args.exec: python -m torch.distributed.launch --nproc_per_node=${NGPUS} train.py --launcher pytorch --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE}
    pass

def main(args):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--addr', type=str, default='127.0.0.1:11112',
                        help='federated server address')
    parser.add_argument('--exec', type=str, required=True,
                        help='the script or command to call up traning process.')
    args = parser.parse_args()

    main(args)