class SIPServer():
    pass

class LocationServer(SIPServer):

 # A location service is used by a SIP redirect or
 # proxy server to obtain information about a callee's possible
 # location(s).  It contains a list of bindings of address-of-
 # record keys to zero or more contact addresses.  The bindings
 # can be created and removed in many ways; this specification
 # defines a REGISTER method that updates the bindings
    
    pass

class RegistrarServer(SIPServer):

 # A registrar is a server that accepts REGISTER requests 
 # and places the information it receives in those requests 
 # into the location service for the domain it handles.(rfc3261)
    
    pass

class RedirectServer(SIPServer):

 # A redirect server is a user agent server that
 # generates 3xx responses to requests it receives, directing the
 # client to contact an alternate set of URIs.
       
    pass

class ProxyServer(SIPServer):
    pass

class StatefulProxyServer(ProxyServer):
    pass

class StatelessProxyServer(ProxyServer):
    pass

class UAServer(SIPServer):
    pass


