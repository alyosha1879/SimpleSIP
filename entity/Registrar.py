class Registtar(SIPEntity):

    def __init__():

        super(Registrar, self).__init__()

    def handle_request(msg):

        self.msg = msg

        # only handle_register_request
        if msg.request != "Register":
            return

    　　# RFC3261 "10.3 Processing REGISTER Requests"

        # Step1
        if not self.canBindRequestURI(msg.requestURI):
            return

        # Step2
        self.processHField(msg.):

        self.handl_require_header
        self.auth_UAC

        self.send_response(200)

    def handle_response():

        # only handle_register_response:
        assert(self.isMsgRequest("REGISTER"))

    def canBindRequestURI(self, requestURI):

        localAddrList = getLocalAddrList()

        if requestURI in localAddrList:
            return True
        else:
            return False



    def fail_check_URI():
        
        host = msg.requestURI

        host == 
