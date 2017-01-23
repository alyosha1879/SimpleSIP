class Registtar(SIPEntity):

    def __init__():

        super(Registrar, self).__init__()


    def handle_request(msg):

        self.msg = msg

        # only handle_register_request
        assert(self.isMsgRequest(msg, "REGISTER"))

    　　# RFC3261 "10.3 Processing REGISTER Requests"

        if self.fail_check_URI(msg):
            # Not forward SIP Msg.
            return

        self.handl_require_header
        self.auth_UAC

        self.send_response(200)

    def handle_response():

        # only handle_register_response:
        assert(self.isMsgRequest("REGISTER"))

    def fail_check_URI():
        
        host = msg.requestURI

        host == 
