from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CountRequests(Base):
    __tablename__ = 'total_number_of_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    count = Column(Integer, nullable=False, primary_key=True)

    def __repr__(self):
        return f"<CountRequests(count='{self.count}')>"


class CountRequestsByType(Base):
    __tablename__ = 'total_number_of_requests_by_type'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req_type = Column(String(300), nullable=False, primary_key=True)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<CountRequestsByType(id='{self.id}', req_type='{self.req_type}', count='{self.count}')>"


class MostFrequentRequest(Base):
    __tablename__ = 'most_frequent_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    count = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<MostFrequentRequest(id='{self.id}', url='{self.url}', count='{self.count}')>"


class LargestRequestsWith4xx(Base):
    __tablename__ = 'largest_requests_with_4xx'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(300), nullable=False)
    size = Column(Integer, nullable=False)
    ip = Column(String(30), nullable=False)

    def __repr__(self):
        return f"<LargestRequestsWith4xx(id='{self.id}', url='{self.url}', size='{self.size}', IP='{self.ip}')>"


class UserWith5xxRequests(Base):
    __tablename__ = 'users_with_5xx_requests'
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30), nullable=False)
    requests_number = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<UserWith5xxRequests(id='{self.id}', IP='{self.ip}', requests_number='{self.requests_number}')>"
