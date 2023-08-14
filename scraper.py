#!/usr/bin/env python3
import re
import argparse
import requests
from bs4 import BeautifulSoup


parser = argparse.ArgumentParser()
parser.add_argument("srcfile", metavar="srcfile", type=str, help="Source file containing proxies")
parser.add_argument("-o", "--outfile", metavar="outfile", type=str, required=False, default="proxies.txt", help="Destination file, where your proxies will be saved")
parser.add_argument("-p", "--port", metavar="port", type=int, required=False, help="Port to filter by. This is an int like 8080")
args = parser.parse_args()



def page_Data(url):
    page = requests.get(url)

    try:
        soup = BeautifulSoup(page.content, 'html.parser')
        data = soup.get_text()
        data = data.split('\n', -1)
    except:
        pass
        
    return str(data)


def rem_Duplicates(x):
  return list(dict.fromkeys(x))



with open(args.srcfile, 'r') as f:
    lines = f.readlines()
    proxies = []
    for line in lines:
            data = page_Data(str.strip(line))
            pattern = re.findall(r'[0-9]+(?:\.[0-9]+){3}:[0-9]+', data)
            proxies.append(pattern)
        
with open(args.outfile, 'w') as pl:
    pattern = rem_Duplicates(pattern)
    if args.port is None:
        for each in pattern:
            pl.write(each + '\n')
    else:
        for each in pattern:
            port = each.split(":", 1)[1]
            if int(port) == args.port:
                pl.write(each + '\n')
 
