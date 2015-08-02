
import os


class CreateDirectory:
    def __init__(self, value):
        self.dir_name = value

    def __call__(self, obj):
        def wrap(*args, **kwargs):
        	if not os.path.exists(self.dir_name):
        		os.makedirs(self.dir_name)
        	obj(*args, **kwargs)
        return wrap    

__all__ =  ['CreateDirectory']