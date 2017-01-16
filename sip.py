import utils

def getSIPMessage(msg): 
    return msg.split('\r\n\r\n')[0]

class SIP:

    def __init__(self, msg):

        self.msg = msg

        # SIP-Message-Format
	# 
	# Start-Line: Request-Line or Status-Line.
	# HeaderFields: Name: Values1;Value2;Value3...
	# SDP:

        # Start-Line = Request-Line or Status-Line.
        self.startLine = None
        self.SIPVersion = None

        # If startLine is a Request-Line.
        self.method = None
        self.requestURI = None

        # If startLine is a Status-Line.
        self.statusCode = None
        self.reasonPhrase = None

        # HeaderFields.
        self.headerFields = None
        self.headerDict = {}

        self.Request_URI = None
        self.To = None
        self.From = None
        self.Call_ID = None
        self.CSeq = None
        self.Contact = None

        self.parseMsg()
        self.parseStartLine()
        self.parseHeaderFields()

    def parseMsg(self):

        # 1st Line is Start-Line.
        # Remaing Lines are SIP-HeaderFiedls.

        self.startLine = self.msg.split('\r\n')[0]
        self.headerFields = self.msg.split('\r\n')[1:]


    def parseStartLine(self):

        # Start-Line = Request-Line or Status-Line.
        # Request-Line  =  Method SP Request-URI SP SIP-Version CRLF
        # Status-Line  =  SIP-Version SP Status-Code SP Reason-Phrase CRLF

        if self.startLine.split(" ")[2] == "SIP/2.0":
           self.method, self.requestURI, self.SIPVersion = self.startLine.split(" ")
        else:
           self.SIPVersion, self.statusCode, self.reasonPhrase = self.startLine.split(" ")
             
    def parseHeaderFields(self):

        # HeaderLied-format is "Name: Values1;Value2;Value3..."
        for line in self.headerFields:
            index = line.find(':')
            name = line[:index]
            values = line[index+1:][1:] #[:1] is to remove WS.
 
            # Number of Via-header may be more than one.
            if name == 'Via':
                if not self.headerDict.get(name):
                    self.headerDict[name] = values
                else:
                    self.headerDict[name] += ","
                    self.headerDict[name] += values
            else:
		self.headerDict[name] = values

        #print headerDict.keys()
	#print headerDict.values()

        self.setRequest_URI()
        self.setTo()
        self.setFrom()
        self.setCall_ID()
        self.setCseq()
        self.setContact()

    def setRequest_URI(self):

        return

    def setTo(self):

        self.To = self.headerDict['To']
        

    def setFrom(self):

        self.From = self.headerDict['From']
        print self.From

    def setCall_ID(self):

        self.Call_ID = self.headerDict['Call-ID']

    def setCseq(self):

        self.CSeq = self.headerDict['CSeq']

    def setContact(self):

        self.Contact = self.headerDict['Contact']
         
""" debug code. """

#print testData.SOCKET_BUFFER
SIPMsg = getSIPMessage(utils.SOCKET_BUFFER)
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
