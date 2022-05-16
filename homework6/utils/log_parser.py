from collections import Counter
import re


def parse_log(file_path):

    with open(file_path) as log:
        lines = [line.split(' ') for line in log]
    result = {}

    # 1
    result['Requests Count'] = {'count': sum(1 for _ in lines)}

    # 2
    default_types = ('GET', 'POST', 'PUT', 'HEAD')
    types_counted = Counter([line[5].strip('"') for line in lines])
    result['Requests Count By Type'] = [
        {'type': r_type if r_type in default_types else 'Unknown', 'count': value}
        for r_type, value in sorted(types_counted.items(), key=lambda item: item[1], reverse=True)
    ]

    # 3
    locations_counted = Counter([line[6].split('?')[0] for line in lines])
    result['Top 10 Most Frequent Locations'] = [
        {'location': url, 'count': value}
        for url, value in sorted(locations_counted.items(), key=lambda item: item[1], reverse=True)[:10]
    ]

    # 4
    client_error_requests = [
        {'ip': line[0], 'location': line[6].split('?')[0], 'status': line[8], 'size': int(line[9])}
        for line in lines if re.match('4[0-9]{2}$', line[8])
    ]
    result['Top 5 Location By Size'] = [
        request for request in sorted(client_error_requests, key=lambda item: item['size'], reverse=True)[:5]
    ]

    # 5
    server_error_clients_counted = Counter([line[0] for line in lines if re.match('5[0-9]{2}$', line[8])])
    result['Top 5 Most Frequent Ips'] = [
        {'ip': ip, 'count': value}
        for ip, value in sorted(server_error_clients_counted.items(), key=lambda item: item[1], reverse=True)[:5]
    ]

    return result