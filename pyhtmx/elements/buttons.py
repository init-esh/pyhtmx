
from pyhtmx.base import BaseHtmx

class Button(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])
        
        
