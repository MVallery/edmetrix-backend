from sqlmodel import SQLModel, Field

class Standard(SQLModel, table=True):
    __tablename__ = "standard"
    id: int = Field(primary_key=True, index=True)
    key: str = Field(max_length=255)
    description: str
    type: str = Field(max_length=255)  # CC TEKS
    grade: str = Field(max_length=50)  # K, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    subject: str = Field(max_length=255)  # Math, Science, ELA, Social Studies
