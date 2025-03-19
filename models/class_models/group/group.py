from sqlmodel import Field, SQLModel

class Group(SQLModel, table=True):
    __tablename__ = "group"
    id: int = Field(default=None, primary_key=True, index=True)
    status: str = Field(max_length=255)  # active / inactive
    name: str = Field(max_length=255)
    description: str = Field(max_length=255)
    class_id: int = Field(foreign_key="class.id")
