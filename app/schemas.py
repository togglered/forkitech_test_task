from pydantic import BaseModel
from datetime import datetime

class AddressInfoRequest(BaseModel):
    address: str

class AddressInfoResponse(BaseModel):
    address: str
    bandwidth: int
    energy: int
    trx_balance: int
    timestamp: datetime

class QueryHistoryItem(BaseModel):
    id: int
    address: str
    timestamp: datetime
    bandwidth: int
    energy: int
    trx_balance: int

class QueryHistoryResponse(BaseModel):
    queries: list[QueryHistoryItem]
    total: int
    page: int
    page_size: int