from sqlmodel import Field, SQLModel

class GroupMeetingConcept(SQLModel, table=True):
    __tablename__ = "group_meeting_concept"
    id: int = Field(default=None, primary_key=True, index=True)
    group_meeting_id: int = Field(foreign_key="group_meeting.id")
    concept_id: int = Field(foreign_key="concept.id")
