from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ...database.database import Base

class Talk(Base):
    __tablename__ = "talks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    speaker_id = Column(Integer, ForeignKey("speakers.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)

    speaker = relationship("Speaker", back_populates="talks")