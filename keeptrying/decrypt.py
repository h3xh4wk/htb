#!/usr/bin/env python

from arc4 import ARC4
import base64
import zipfile


def decode(msg):
    # base64 URL
    msg=msg.replace("_", "/").replace("-", "+")
    # neccessary padding before decoding
    msg += "=" * ((4 - len(msg) % 4 ) % 4)
    return base64.b64decode(msg)


def Main(qname):

    with open('secret.zip', 'wb') as f:
        f.write(ARC4(key_).decrypt(decode(qname)))

    with zipfile.ZipFile('secret.zip', 'r') as zipf:
        zipf.extractall(".")

if __name__=="__main__":

    key_='TryHarder'
    dns_request_txt=open('dns_request_TXT', 'r').read()
    domainName='totallylegit.com'
    qname=dns_request_txt.split(".", 1)[1].strip()
    qname=qname.replace(domainName,"").replace(".","")
    Main(qname)
    print(open('secret.txt', 'r').read())
