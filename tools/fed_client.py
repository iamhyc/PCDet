#!/usr/bin/env python3
import argparse
import subprocess as sp
import socket
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
    # python -m torch.distributed.launch --nproc_per_node=${NGPUS} train.py --launcher pytorch --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE}
    pass

def main(args):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, required=True, help="which GPU to run")
    parser.add_argument("--config_file", type=str, required=True, help="task config file")
    parser.add_argument("--ignore_load", default=True, help="whether ignore load or not")
    parser.add_argument("--port", type=int, required=True, help="server port")
    args = parser.parse_args()

    main(args)