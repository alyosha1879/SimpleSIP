""" 
SIP test Message 

INVITE sip:francisco@bestel.com:55060 SIP/2.0
Via: SIP/2.0/UDP 200.57.7.195;branch=z9hG4bKff9b46fb055c0521cc24024da96cd290
Via: SIP/2.0/UDP 200.57.7.195:55061;branch=z9hG4bK291d90e31a47b225bd0ddff4353e9cc0
From: <sip:200.57.7.195:55061;user=phone>;tag=GR52RWG346-34
To: "francisco@bestel.com" <sip:francisco@bestel.com:55060>
Call-ID: 12013223@200.57.7.195
CSeq: 1 INVITE
Contact: <sip:200.57.7.195:5060>
Content-Type: application/sdp
Content-Length:   229

v=0
o=Clarent 120386 120387 IN IP4 200.57.7.196
s=Clarent C5CM
c=IN IP4 200.57.7.196
t=0 0
m=audio 40376 RTP/AVP 8 18 4 0
a=rtpmap:8 PCMA/8000
a=rtpmap:18 G729/8000
a=rtpmap:4 G723/8000
a=rtpmap:0 PCMU/8000
a=SendRecv
"""

import binascii

INVITE_BIN="494e56495445207369703a6672616e636973636f4062657374656c2e636f6d3a3535303630205349502f322e300d0a5669613a205349502f322e302f554450203230302e35372e372e3139353b6272616e63683d7a39684734624b66663962343666623035356330353231636332343032346461393663643239300d0a5669613a205349502f322e302f554450203230302e35372e372e3139353a35353036313b6272616e63683d7a39684734624b32393164393065333161343762323235626430646466663433353365396363300d0a46726f6d3a203c7369703a3230302e35372e372e3139353a35353036313b757365723d70686f6e653e3b7461673d475235325257473334362d33340d0a546f3a20226672616e636973636f4062657374656c2e636f6d22203c7369703a6672616e636973636f4062657374656c2e636f6d3a35353036303e0d0a43616c6c2d49443a203132303133323233403230302e35372e372e3139350d0a435365713a203120494e564954450d0a436f6e746163743a203c7369703a3230302e35372e372e3139353a353036303e0d0a436f6e74656e742d547970653a206170706c69636174696f6e2f7364700d0a436f6e74656e742d4c656e6774683a2020203232390d0a0d0a763d300d0a6f3d436c6172656e74203132303338362031323033383720494e20495034203230302e35372e372e3139360d0a733d436c6172656e74204335434d0d0a633d494e20495034203230302e35372e372e3139360d0a743d3020300d0a6d3d617564696f203430333736205254502f4156502038203138203420300d0a613d7274706d61703a382050434d412f383030300d0a613d7274706d61703a313820473732392f383030300d0a613d7274706d61703a3420473732332f383030300d0a613d7274706d61703a302050434d552f383030300d0a613d53656e64526563760d0a"
INVITE_STR = binascii.a2b_hex(INVITE_BIN)

REGISTER_BIN="5245474953544552207369703a3132372e302e302e31205349502f322e300d0a5669613a205349502f322e302f554450203132372e302e302e313a35373538363b72706f72743b6272616e63683d7a39684734624b506a7539717072794b796f643236667a722e363357316b7649575069786267766b570d0a4d61782d466f7277617264733a2037300d0a46726f6d3a2022746573742d666f722d6175746822203c7369703a7465737432403132372e302e302e313e3b7461673d365559576c2e742d48635a32613136595246516d4c62304956586a554161714e0d0a546f3a2022746573742d666f722d6175746822203c7369703a7465737432403132372e302e302e313e0d0a43616c6c2d49443a2061392e52536e352e6b4f433871494970796c6d645a354d69454b5a69643752740d0a435365713a20323631302052454749535445520d0a557365722d4167656e743a2054656c6570686f6e6520312e322e360d0a436f6e746163743a2022746573742d666f722d6175746822203c7369703a7465737432403132372e302e302e313a35373538363b6f623e0d0a457870697265733a203330300d0a416c6c6f773a20505241434b2c20494e564954452c2041434b2c204259452c2043414e43454c2c205550444154452c20494e464f2c205355425343524942452c204e4f544946592c2052454645522c204d4553534147452c204f5054494f4e530d0a436f6e74656e742d4c656e6774683a2020300d0a0d0a"

REGISTER_STR = binascii.a2b_hex(REGISTER_BIN)