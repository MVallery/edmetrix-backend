
from sqlmodel import SQLModel, Field
# One that all concepts can have would be to put a "careless mistake" or "silly mistake" meaning it didn't show any lack of understanding the concept. 
# Some may be more generic like:  "misunderstanding word problem meaning" or "misunderstanding the question" or "misunderstanding the concept" etc.
# Other mistakes would be more specific to the concept such as "forgot the 0 on the 2nd row in multiplication" "Added instead of Multiply for area" or "didn't know the formula" etc.
class Mistake(SQLModel, table=True):
    __tablename__ = "mistake"
    id: int = Field(default=None, primary_key=True, index=True)
    mistake: str = Field(max_length=255)
