# class_id = Column(Integer, ForeignKey('class.id'))
# student_id = Column(Integer, ForeignKey('student.id'))
# amount -1/1
# type = Column(Text(255)) # type of behavior (e.g. off-task, on-task, etc.)
# # store these for future use to be able to track behavior based on seating chart
# seating_chart_id = Column(Integer, ForeignKey('seating_chart.id'))
# student_desk_id = Column(Integer, ForeignKey('student_desk.id'))
# date = Column(DateTime, default=func.now())
# notes = Column(Text(1000))