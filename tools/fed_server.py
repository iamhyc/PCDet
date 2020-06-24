#!/usr/bin/env python3
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
    pass

def main():
    pass

if __name__ == "__main__":
    main()