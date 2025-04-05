from sqlalchemy import Column, Boolean, Integer, Text, ForeignKey
from _models.base import Base

class Standard(Base):
    __tablename__ = "standard"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(Text(255))
    type = Column(Text(255)) # CC TEKS, School, 
    grade = Column(Text(50)) # K, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    subject = Column(Text(255)) # Math, Science, ELA, Social Studies
    domain = Column(Text(255)) # Number and Operations, Algebra, Geometry, Measurement, Data Analysis and Probability
    subDomain = Column(Text(255)) # Number and Operations in Base Ten, Number and Operations in Fractions, Algebraic Thinking, Measurement and Data, Geometry
    description = Column(Text(255))
