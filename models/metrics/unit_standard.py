from sqlmodel import SQLModel, Field

class UnitStandard(SQLModel, table=True):
    __tablename__ = "unit_standard"
    id: int = Field(default=None, primary_key=True, index=True)
    standard_id: int = Field(foreign_key="standard.id")
    unit_id: int = Field(foreign_key="unit.id")
