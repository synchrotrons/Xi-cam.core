from xicam.plugins.DataHandlerPlugin import DataHandlerPlugin, start_doc
import numpy as np


class NPYPlugin(DataHandlerPlugin):
    name = 'NPYPlugin'

    DEFAULT_EXTENTIONS = ['.npy']

    def __call__(self, *args, **kwargs):
        return np.load(self.path)

    def __init__(self, path):
        super(NPYPlugin, self).__init__()
        self.path = path

    @classmethod
    def getStartDoc(cls, paths, start_uid):
        return start_doc(start_uid=start_uid, metadata={'paths': paths})
