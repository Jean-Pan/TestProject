from pysnmp.entity.rfc3413.oneliner import cmdgen

ip = '10.167.76.5'
community = 'public'
oid = '1.3.6.1.2.1.17.4.3.1.1'


def info(ip, community, oid):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.nextCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((ip, 161)),
        oid
    )

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
            errorStatus.prettyPrint(),
            errorIndex and varBinds[-1][int(errorIndex) - 1][0] or '?'
        )
              )
    else:
        for varBind in varBinds:
            # print(varBind)
            for name, val in varBind:
                print(name.prettyPrint(), val.prettyPrint())
        #         print(name.prettyPrint(),val)
        #         print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))


info(ip, community, oid)
