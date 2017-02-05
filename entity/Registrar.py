class Registtar(SIPEntity):

    def __init__():

        super(Registrar, self).__init__()

    def handle_request(msg):

        self.msg = msg

        # only handle_register_request
        if not msg.request == "Register":
            return

        # RFC3261 "10.3 Processing REGISTER Requests"

        # Step1
        if not self.canBindRequestURI(msg.requestURI):
            # Domain not allowed.
            return

        # Step2
        self.processRequireHF(msg.requireHF)

        # Step3
        self.authUAC()

        # Step4
        self.

        # Step5
        self.extractAOR(msg.toHF)

        # Step6
        self.checkContactHF(msg.contactHF)

        # Step7
        self.processContactHF(msg.contactHF)

        # Step8
        self.send_response(200)


    def handle_response():
        # only handle_register_response:

        assert(self.isMsgRequest("REGISTER"))

    def send_response(code):






    def canBindRequestURI(self, requestURI):
        # The registrar inspects the Request-URI to determine whether it has 
        # access to bindings for the domain identified in the Request-URI.

        if CHECK_DOMAIN == False:
            # Allow all domains.
            return

        else:
            allowdDomainList = readDomainList()
            
            if uriDomain in allowedDomainList:
                return True
            else:
                return False

