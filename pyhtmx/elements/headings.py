from pyhtmx.base import BaseHtmx

class H1(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

      
class H2(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class H3(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class H4(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class H5(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])
 
class H6(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

