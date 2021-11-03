from lxml import etree, html

class BaseHtmx():
    def __init__(self,*args,**kwargs):
        self._id=''
        self._class=''
        self._style=''
        self._name=''
        self._method=''
        self._url=''
        self._target=''
        self._swap=''
        self._trigger=''
        
        
        for k,v in kwargs.items():
            setattr(self,k,v)

    def get(self,url):
        self._url=url
        self._method='GET'
        return self

    def post(self,url):
        self._url=url
        self._method='POST'
        return self

    def put(self,url):
        self._url=url
        self._method='PUT'
        return self
    
    def target(self,target):
        self._target=target
        return self

    def __repr__(self):
        op={k:v for k, v in self.__dict__.items() if v}

        inner_elem=op.pop('inner') if 'inner' in op else ""
        tagstart=f"<{self.__class__.__name__.lower()}"
        for k,v in op.items():
            if k!='_url' and k!='_method' and k!='_target' and k!='_swap' and k!='_trigger': 
                tagstart+=f' {str(k).replace("_","")}="{v}"'
            elif k=='_method' and v=='GET':
                tagstart+=f' hx-get="{self._url}"'
            elif k=='_method' and v=='POST':
                tagstart+=f' hx-post="{self._url}"'
            elif k=='_method' and v=='PUT':
                tagstart+=f' hx-put="{self._url}"'
        tagstart+='>'
        tagend=f"</{self.__class__.__name__.lower()}>"
        return f"{tagstart}{inner_elem}{tagend}"
    
    def __str__(self):
        return self.__repr__()

    def render(self):
        document_root = html.fromstring(self.__repr__())
        print(etree.tostring(document_root, encoding='unicode', pretty_print=True))

