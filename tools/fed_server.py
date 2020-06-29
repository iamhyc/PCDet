#!/usr/bin/env python3
import argparse
import socketio
from enum import Enum
from train_utils.fed_utils import *

class State(Enum):
    INIT        = 0x01
    WAIT        = 0x02
    ERROR       = 0x0F
    pass

class Action(Enum):
    EVAL        = 0x10
    ERROR       = 0xF0
    pass

class FedServer(object):
    def __init__(self, args):
        self.server = socketio.Server()
        pass

    pass

def main(args):

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=11112,
                        help='server port')
    parset.add_argument('--init_model', type=str, default=None,
                        help='the initial model distributed to the clients')
    parser.add_argument('--num_client', type=int, required=True,
                        help='the number of clients in this experiment')
                        
    args = parser.parse_args()

    main(args)