#!/usr/bin/env bash
#WARNING: please refer to this README before using: https://github.com/pytorch/pytorch/blob/master/torch/distributed/launch.py

set -x
NGPUS=$1
PY_ARGS=${@:2}

python -m torch.distributed.launch --nproc_per_node=${NGPUS} train.py --launcher pytorch ${PY_ARGS}

