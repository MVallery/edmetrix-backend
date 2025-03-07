from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils.types.encrypted.encrypted_type import StringEncryptedType

Base = declarative_base()

class DreamSign(Base):
    __tablename__ = "dream_signs"
    id = Column(Integer, primary_key=True, index=True)
    # name = Column(StringEncryptedType(Text, length=255), index=True)
    # name = Column(Text(255), index=True)

    color = Column(Text)