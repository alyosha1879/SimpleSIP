import testData.py

class SIP:

    def __init__(msg):

        Start-Line, HeaderFields = parseMsg(msg)

        self.SIP-Version = None

        self.Method = None
        self.Request-URI = None

        self.Status-Code = None
        self.Reason-Phrase = None

        self.parseFirst-Line(Start-Line)
        self.setHeaderFields(headerFields)

    def parseMsg(msg):

        # 1st Line is Start-Line.
        # Remaing Lines are SIP-HeaderFiedls.

        Start-Line = msg.split('\r\n')[0]
        HeaderFields = msg.split('\r\n')[1:]

       return Start-Line, HeaderFields

    def parseStartLine(string):

        return self._parseRequestLine(string)

        return self._parserStatusLine(string)
         
    def parseHeaderFields(msg):

        pass

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
