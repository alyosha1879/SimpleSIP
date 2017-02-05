
SIP_RESPONSE_DICT = {

        # Informational
        100:'Trying',
        180:'Ringing',
        181:'Call Is Being Forwarded',
        182:'Queued',
        183:'Session Progress',

        # Success
        200:'OK',

        # Redirection
        301:'Moverd Permanentry',
        302:'Moved Temporary',
        305:'Use Proxy',
        380:'Alternative Service',

        # Client-Error
        400:'Bad Request',
        401:'Unauthorized',
        403:'Forbidden',
        404:'Not Found',
        486:'Busy Here',
        487:'Request Terminated',

        # Server-Error
        500:'Server Internal Error',
        501:'Not Implemented',
        503:'Service Unavalable',
        504:'Server Time-out',
        505:'SIP Version not supported',
        513:'Message Too Large',

        # Global-Failure
        600:'Busy Everywhre',
        603:'Decline',
        604:'Does not exist anywhere',
        606:'Not Acceptable'
}

