from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class AddressQuery(Base):
    __tablename__ = "address_queries"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    bandwidth = Column(Integer, nullable=True)
    energy = Column(Integer, nullable=True)
    trx_balance = Column(Integer, nullable=True)