import psutil
import socket
import csv
import collections

from operator import itemgetter
from itertools import groupby

printfmt = "%-6s %-30s %-30s %-13s"
print(printfmt % ("PID", "Local address", "Remote address", "Status"))
AD = "-"
inlist = []

for c in psutil.net_connections(kind='inet'):
    laddr = "%s@%s" % (c.laddr)
    raddr = "" 
    if c.raddr:
        raddr = "%s@%s" % (c.raddr)   
    if c.pid and c.raddr:       
       inlist.append(tuple((c.pid,laddr,raddr,c.status)))


countspid = collections.Counter( x[0] for x in inlist)

inlist.sort(key = lambda x : countspid[x[0]],reverse = True)

for elt, items in groupby(inlist, itemgetter(0)):
        for c in items:
            print(printfmt % (c[0],c[1],c[2],c[3]))





