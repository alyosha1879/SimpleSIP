from urlparse import urlparse

class SIPURI():

    # SIP-URI = "sip:" [ userinfo ] hostport uri-parameters [ headers ]
    # userinfo = ( user / telephone-subscriber ) [ ":" password ] "@"
    # hostport = host [ ":" port ]
    # uri-parameters = *( ";" uri-parameter)
    # uri-parameter = transport-param / user-param / method-param/ ttl-param /    maddr-param / lr-param / other-param

    def __init__(uri):
        
        self.scheme = None
        self.userinfo = None
        self.user = None
        self.telephone-subscriber = None
        self.password = None
        self.hostport = None
        self.host = None
        self.port = None
        self.uri-parameters = []

        self.parser(uri)

    def parser(self, uri):

        self.schema = uri.split(':')[0]
        

        o = urlparse(uri)

        print o.shceme
        print o.netloc


