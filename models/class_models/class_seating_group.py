from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base
# This would be a way to do it by row / group by going to try to do it by snap grid layout instead first.
class Class_Seating(Base):
    __tablename__ = "class_seating"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255)) # group 1 / row 1 / pair 1 The Owls
    order = Column(Integer)
    note = Column(Text(255))
    color = Column(Text(10))


from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Seating_Group_Student(Base):
    __tablename__ = "class_seating_group_student"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(ForeignKey('student.id'))
    class_seating_group_id = Column(ForeignKey('class_seating_group.id'))
    order = Column(Integer)

    from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, JSON
from ..base import Base

class Class_Seating(Base):
    __tablename__ = "class_seating"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text(255))
    order = Column(Integer)
    status = Column(Text(255)) # active / inactive
    active_starting = Column(Text(255)) # date
    active_ending = Column(Text(255)) # date
    type = Column(Text(255)) # rows, groups, pairs
    