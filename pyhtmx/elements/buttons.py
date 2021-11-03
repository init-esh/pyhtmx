
from pyhtmx.base import BaseHtmx

class Button(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        self.inner = ''.join([str(child) for child in inner])
        
        
