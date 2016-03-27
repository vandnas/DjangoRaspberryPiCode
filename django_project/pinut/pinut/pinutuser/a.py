cl_mac="c1:f5:c6:0c:b9:ef"

clmac_list=cl_mac.split(':')
print "clmac",clmac_list
CLIENT_MAC = ''.join([str(mac) for mac in clmac_list])
print "CLIENT_MAC",CLIENT_MAC ,type(CLIENT_MAC)

