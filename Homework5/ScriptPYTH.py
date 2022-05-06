#!/usr/bin/python3
import os
import sys
from collections import Counter
from sys import argv
import argparse
import re
import json

def Parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename',default='access.log')
    parser.add_argument('--json',action='store_true' ,default=False)
    return parser



if __name__ == '__main__':
    parser = Parser()
    namespace = parser.parse_args(sys.argv[1:])
    file_path = os.path.abspath(os.path.join(__file__, os.pardir))+"/"+namespace.filename
    with open(file_path) as log:
        lines = [line.split(' ') for line in log]
    result = {}

    # 1
    result['Task 1.Count of all string'] = {'count': sum(1 for _ in lines)}

    # 2
    default_types = ('GET', 'POST', 'PUT', 'HEAD')
    types_counted = Counter([line[5].strip('"') for line in lines])
    result['Task 2.Count Request:'] = [
        {'type': r_type if r_type in default_types else 'Unknown', 'count': value}
        for r_type, value in sorted(types_counted.items(), key=lambda item: item[1], reverse=True)
    ]

    # 3
    locations_counted = Counter([line[6].split('?')[0] for line in lines])
    result['Task 3.Top 10 Request url:'] = [
        {'location': url, 'count': value}
        for url, value in sorted(locations_counted.items(), key=lambda item: item[1], reverse=True)[:10]
    ]

    # 4
    client_error_requests = [
        {'ip': line[0], 'location': line[6].split('?')[0], 'status': line[8], 'size': int(line[9])}
        for line in lines if re.match('4[0-9]{2}$', line[8])
    ]
    result['Task 4.Top 5 Request bytes'] = [
        request for request in sorted(client_error_requests, key=lambda item: item['size'], reverse=True)[:5]
    ]

    # 5
    server_error_clients_counted = Counter([line[0] for line in lines if re.match('5[0-9]{2}$', line[8])])
    result['Task 5.Top 5 IP'] = [
        {'ip': ip, 'count': value}
        for ip, value in sorted(server_error_clients_counted.items(), key=lambda item: item[1], reverse=True)[:5]
    ]
    if namespace.json:
        with open('solveJSON','w',encoding="utf-8") as out:
            json.dump(result,out)
        out.close()
    else:
        with open('solvePY.txt', 'w') as out:
            for key, val in result.items():
                out.write('{}:\n{}\n\n'.format(key, val))
        out.close()