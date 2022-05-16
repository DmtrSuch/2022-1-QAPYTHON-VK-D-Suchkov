from models.models import RequestsCount, RequestsCountByType, Top10MostFrequentLocations, Top5LocationsBySize, \
    Top5MostFrequentIps
from tests.base_mysql import MySQLBase


class TestRequestsCount(MySQLBase):

    def prepare(self):
        entry = self.mysql_builder.create_requests_count(self.parsed_log['Requests Count'])
        self.mysql.session.add(entry)

    def test_requests_count(self):
        row = self.mysql.session.query(RequestsCount).first()
        assert row.count == self.parsed_log['Requests Count']['count']


class TestRequestsCountByType(MySQLBase):

    def prepare(self):
        for entry in self.parsed_log['Requests Count By Type']:
            entry = self.mysql_builder.create_requests_count_by_type(entry)
            self.mysql.session.add(entry)

    def test_requests_count_by_type(self):
        rows = self.mysql.session.query(RequestsCountByType).all()
        assert len(rows) == len(self.parsed_log['Requests Count By Type'])


class TestTop10MostFrequentLocations(MySQLBase):

    def prepare(self):
        for entry in self.parsed_log['Top 10 Most Frequent Locations']:
            entry = self.mysql_builder.create_top_10_most_frequent_locations(entry)
            self.mysql.session.add(entry)

    def test_top_10_most_frequent_locations(self):
        rows = self.mysql.session.query(Top10MostFrequentLocations).all()
        assert len(rows) == len(self.parsed_log['Top 10 Most Frequent Locations'])


class TestTop5LocationsBySize(MySQLBase):

    def prepare(self):
        for entry in self.parsed_log['Top 5 Location By Size']:
            entry = self.mysql_builder.create_top_5_locations_by_size(entry)
            self.mysql.session.add(entry)

    def test_top_5_locations_by_size(self):
        rows = self.mysql.session.query(Top5LocationsBySize).all()
        assert len(rows) == len(self.parsed_log['Top 5 Location By Size'])


class TestTop5MostFrequentIps(MySQLBase):

    def prepare(self):
        for entry in self.parsed_log['Top 5 Most Frequent Ips']:
            entry = self.mysql_builder.create_top_5_most_frequent_ips(entry)
            self.mysql.session.add(entry)

    def test_top_5_most_frequent_ips(self):
        rows = self.mysql.session.query(Top5MostFrequentIps).all()
        assert len(rows) == len(self.parsed_log['Top 5 Most Frequent Ips'])