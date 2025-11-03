from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ...database.database import Base

class Speaker(Base):
    __tablename__ = "speakers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    bio = Column(String)
    company = Column(String)

    talks = relationship("Talk", back_populates="speaker")