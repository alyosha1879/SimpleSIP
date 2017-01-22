class SIPURI():

    # SIP-URI = "sip:" [ userinfo ] hostport uri-parameters [ headers ]
    # userinfo = ( user / telephone-subscriber ) [ ":" password ] "@"
    # hostport = host [ ":" port ]
    # uri-parameters = *( ";" uri-parameter)
    # uri-parameter = transport-param / user-param / method-param/ ttl-param /    maddr-param / lr-param / other-param

    def __init__(sipURI):
        
        self.parser(sipURI)

        self.schema = None
        self.userinfo = None
        self.user = None
        self.telephone-subscriber = None
        self.password = None
        self.hostport = None
        self.host = None
        self.port = None
        self.uri-parameters = []

    def parser(self, sipURI):

    
