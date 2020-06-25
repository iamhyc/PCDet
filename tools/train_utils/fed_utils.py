import pickle, codecs
import socket
import torch

def objdump_pickle(obj, file_path=''):
    if file_path:
        with open(file_path, 'wb') as fd:
            pickle.dump(x, fd)
        return True
    else:
        obj_str = pickle.dumps(obj)
        obj_str = codecs.encode(obj_str, 'base64').decode()
        # obj_str = msgpack.packb(obj_str, default=msgpack_numpy.encode) #TODO: compare msgpack vs json serialization performance
        return obj_str
    pass

def objload_pickle(obj_str, isFile=False):
    if isFile:
        file_path = obj_str
        with open(file_path) as fd:
            return pickle.load(fd)
    else:
        _decode_str = codecs.decode(obj_str.encode(), 'base64')
        return pickle.loads(_decode_str)
    pass

class FedTrainingUtility(object):
    def __init__(self, method):
        self.method = 'sync' if method=='sync' else 'async'
        pass

    def report_and_fetch(self, model_state):
        if self.method=='sync':
            pass
        elif self.method=='async': #TODO: todo
            return None
        else:
            return None
        pass

    pass