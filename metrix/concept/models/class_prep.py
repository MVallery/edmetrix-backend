from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from _models.base import Base

class ClassPrep(Base):
    __tablename__ = "class_prep"
    id = Column(Integer, primary_key=True, index=True)
    prep_id = Column(Integer, ForeignKey('prep.id'))
    class_id = Column(Integer, ForeignKey('class.id'))

    prep = relationship("Prep") 


    # class_ = relationship("ClassModel", backref="subjects") 



