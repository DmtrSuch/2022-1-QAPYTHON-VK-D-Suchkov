from models.models import RequestsCount, RequestsCountByType, Top10MostFrequentLocations, Top5LocationsBySize,\
    Top5MostFrequentIps


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_requests_count(self, values: dict):

        requests_count = RequestsCount(
            count=values['count']
        )
        self.client.session.add(requests_count)
        return requests_count

    def create_requests_count_by_type(self, values: dict):

        requests_count_by_type = RequestsCountByType(
            r_type=values['type'],
            count=values['count']
        )
        self.client.session.add(requests_count_by_type)
        return requests_count_by_type

    def create_top_10_most_frequent_locations(self, values: dict):

        top_10 = Top10MostFrequentLocations(
            location=values['location'],
            count=values['count']
        )
        self.client.session.add(top_10)
        return top_10

    def create_top_5_locations_by_size(self, values: dict):

        top_5_size = Top5LocationsBySize(
            ip=values['ip'],
            location=values['location'],
            status=values['status'],
            size=values['size']
        )
        self.client.session.add(top_5_size)
        return top_5_size

    def create_top_5_most_frequent_ips(self, values: dict):

        top_5_ip = Top5MostFrequentIps(
            ip=values['ip'],
            count=values['count']
        )
        self.client.session.add(top_5_ip)
        return top_5_ip