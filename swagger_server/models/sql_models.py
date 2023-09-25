from sqlalchemy import Column, UUID, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class SARegion(Base):
    __tablename__ = 'regions'
    id = Column(UUID, primary_key=True)
    name = Column(Text, unique=True)
    endpoint = Column(Text, unique=True)


class SAZone(Base):
    __tablename__ = 'zones'
    id = Column(UUID, primary_key=True)
    name = Column(Text, unique=True)
    region_id = Column(UUID, ForeignKey('regions.id'))
    region = relationship('SARegion')


class SARecord(Base):
    __tablename__ = 'records'
    id = Column(UUID, primary_key=True)
    name = Column(Text, unique=True)
    type = Column(Text, unique=True)
    value = Column(Text, unique=True)
    zone_id = Column(UUID, ForeignKey('zones.id'))
    zone = relationship('SAZone')
