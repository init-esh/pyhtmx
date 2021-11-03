
from pyhtmx.base import BaseHtmx

class Input(BaseHtmx):
    def __init__(self, _type, **kwargs):
        super().__init__(**kwargs)
        self._type = _type
        
    def __repr__(self):
        return f'<{self.__class__.__name__.lower()} type="{self._type}"/>'
        

    def __str__(self):
        return f'<{self.__class__.__name__.lower()} type="{self._type}"/>'