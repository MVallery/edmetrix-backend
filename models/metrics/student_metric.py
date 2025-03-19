from sqlmodel import SQLModel, Field

class StudentMetric(SQLModel, table=True):
    __tablename__ = "student_metric"
    id: int = Field(default=None, primary_key=True, index=True)
    student_id: int = Field(foreign_key="student.id")
    metric_id: int = Field(foreign_key="metric.id")
    mistake_id: int = Field(foreign_key="mistake.id")
