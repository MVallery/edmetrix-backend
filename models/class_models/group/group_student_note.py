from sqlmodel import Field, SQLModel

class GroupStudentNote(SQLModel, table=True):
    __tablename__ = "group_student_note"
    id: int = Field(default=None, primary_key=True, index=True)
    text: str = Field(max_length=255)
    order: int
    group_id: int = Field(foreign_key="group.id")
    created: str = Field(max_length=255)
    updated: str = Field(max_length=255)
    type: str = Field(max_length=255)  # academic / behavior / general
