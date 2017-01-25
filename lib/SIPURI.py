import sys
sys.path.append('/root/git-test/SimpleSIP/testdir')

import testData


class SIPURI():

    # SIP-URI = "sip:" [ userinfo ] hostport uri-parameters [ headers ]
    # userinfo = ( user / telephone-subscriber ) [ ":" password ] "@"
    # hostport = host [ ":" port ]
    # uri-parameters = *( ";" uri-parameter)
    # uri-parameter = transport-param / user-param / method-param/ ttl-param /    maddr-param / lr-param / other-param

    def __init__(self, uri):
        
        self.scheme = None
        self.userinfo = None
        self.user = None
        self.telephone_subscriber = None
        self.password = None
        self.hostport = None
        self.host = None
        self.port = None
        self.uri_parameters = []

        self.parserURI(uri)

    def parserURI(self, uri):

        self.schema = uri.split(':')[0]
        restURI = uri.split(':')[1]

        if "@" in uri:
            userinfo = restURI.split('@')[0]
            self.userinfo = userinfo
            self.parseUserinfo(userinfo)

    def parseUserinfo(self, userinfo):

        if ":" in userinfo:
            self.user = userinfo.split(':')[0]
            self.password = userinfo.split(':')[1]
        else:
            self.user = userinfo

testURI = testData.SIPURI3
print testURI
test = SIPURI(testURI)

print test.schema
print test.userinfo
print test.user
print test.password
