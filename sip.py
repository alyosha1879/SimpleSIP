import testData

def getSIPMessage(msg): 
    return msg.split('\r\n\r\n')[0]

class SIP:

    def __init__(self, msg):

        startLine, headerFields = self.parseMsg(msg)

        self.SIPVersion = None

        self.method = None
        self.requestURI = None

        self.statusCode = None
        self.reasonPhrase = None

        self.parseStartLine(startLine)
        self.parseHeaderFields(headerFields)

    def parseMsg(self, msg):

        # 1st Line is Start-Line.
        # Remaing Lines are SIP-HeaderFiedls.

        startLine = msg.split('\r\n')[0]
        headerFields = msg.split('\r\n')[1:]

        return [startLine, headerFields]

    def parseStartLine(self, string):

        # Request-Line  =  Method SP Request-URI SP SIP-Version CRLF
        # Status-Line  =  SIP-Version SP Status-Code SP Reason-Phrase CRLF

        if string.split(" ")[2] == "SIP/2.0":
           self.method, self.requestURI, self.SIPVersion = string.split(" ")
        else:
           self.SIPVersion, self.statusCode, self.reasonPhrase = string.split(" ")
             
    def parseHeaderFields(self, msg):
        
        #print msg
        pass

""" debug code. """

#print testData.SOCKET_BUFFER
SIPMsg = getSIPMessage(testData.SOCKET_BUFFER)
testClass = SIP(SIPMsg)
print testClass.method
print testClass.requestURI
print testClass.SIPVersion

"""
        self.Via = self.getVia()
        self.MAX-Forward = self.getMax-Forwad(self.headerFields)
        self.Record-Route = ""
        self.From = ""
        self.Contact = ""
        self.To = ""
        self.Call-ID = ""
        self.Cseq = ""
        self.Contact = ""
        self.Expires = ""
        self.Content-Length = ""
        self.Content-Type = ""
        self.Content-Disposition = ""


    def getStartLine(msg):
        # Start-Line is Request-Line or Response-Line.
        return msg.split('\r\n')[0]


    def getHeaderFieldDict(msg):
        
        return msg.split('\r\n')[1:]


    def getFrom(msg):

# First, let's divide SIP from SDP.
def getSIPMessage(strData):

    return strData.split('\r\n\r\n')[0]


def getSDPMessage(strData):

    return strData.split('\r\n\r\n')[1]

# HeaderLied-format is "Name: Values1;Value2;Value3..."
def getHeaderFieldDict(SIPMessage):
    
    # 1st Line is Request, NOT SIPHeader.
    HeaderFieldsList = SIPMessage.split('\r\n')[1:]

    HeaderFieldDict = {}

    for line in HeaderFieldsList:
        name = line.split(':')[0]
        values = line.split(':')[1:]
        HeaderFieldDict[name] = values

    return HeaderFieldDict

def getSIPRequestLine(SIPMessage):

    return SIPMessage.split('\r\n')[0]

def getVIALine(HeaderFieldList):

    return 

def getSIPRequest(RequestLine):

    return RequestLine.split(' ')[0]

"""
