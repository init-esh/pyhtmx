from pyhtmx.base import BaseHtmx

class Html(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class Body(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class Span(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

   
class P(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])


class Div(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

class Title(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

class Head(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

class Ul(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])

class Li(BaseHtmx):
    def __init__(self, *inner, **kwargs):
        super().__init__(**kwargs)
        if type(inner[0])==list:
            self.inner = ''.join([str(child) for child in inner[0]])
        else:
            self.inner = ''.join([str(child) for child in inner])
