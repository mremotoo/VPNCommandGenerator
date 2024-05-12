import pyperclip

iPSecIntName = ""
WANInterface = ""
remotePeer = ""
insdideInterface = ""
localaddr = ""
localaddrName = ""
remoteaddr = ""
remoteaddrName = ""
psksecret = ""
policyNumber = ""
staticRouteNumber = ""

interfaceCommands = [
#     # phase 1 interface ------------------

"config vpn ipsec phase1-interface" ,
f"  edit {iPSecIntName}",
f"      set interface {WANInterface}",
"       set ike-version 2",
"       set keylife 28800",
"       set peertype any",
"       set net-device disable",
"       set proposal aes256-sha512",
"       set dhgrp 21",
f"      set remote-gw {remotePeer}",
f"      set psksecret {psksecret}",
"   next",
"end",

#     # phase 2 interface ------------------
    
"config vpn ipsec phase2-interface",
f"  edit {iPSecIntName}",
f"      set phase1name {iPSecIntName}",
"       set proposal aes256-sha512",
"       set dhgrp 21",
"       set auto-negotiate enable",
"       set keylifeseconds 28800",
"   next",
"end",

    # address object ------------------

"config firewall address",
f"    edit {remoteaddrName}",
"        set allow-routing enable",
f"        set subnet {remoteaddr}",
"    next",
f"    edit {localaddrName}",
"        set allow-routing enable",
f"        set subnet {localaddr}",
"    next",
"end",

    # static route ------------------

"config router static",
f"    edit {staticRouteNumber}",
f"        set device {iPSecIntName}",
f"        set dstaddr {remoteaddrName}",
"    next",
"end",

    # firewall policy ------------------

"config firewall policy",
f"  edit {policyNumber}",
f"      set name {iPSecIntName + "_" + "Outgoing"}",
f"      set srcintf {insdideInterface}",
f"      set dstintf {iPSecIntName}",
"       set action accept",
f"      set srcaddr {localaddrName}",
f"      set dstaddr {remoteaddrName}",
    "next",
"end"
]

# print('\n'.join(interfaceCommands))
pyperclip.copy('\n'.join(interfaceCommands))