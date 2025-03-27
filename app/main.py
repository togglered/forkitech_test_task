from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, services, models
from .database import get_db, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/address-info/", response_model=schemas.AddressInfoResponse)
def get_address_info(request: schemas.AddressInfoRequest, db: Session = Depends(get_db)):
    try:
        info = services.TronService.get_address_info(request.address)
        query = services.TronService.log_query(db, request.address, info)
        
        return {
            "address": request.address,
            "bandwidth": info["bandwidth"],
            "energy": info["energy"],
            "trx_balance": info["trx_balance"],
            "timestamp": query.timestamp
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/query-history/", response_model=schemas.QueryHistoryResponse)
def get_query_history(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    try:
        history = services.TronService.get_query_history(db, page, page_size)
        return {
            "queries": history["queries"],
            "total": history["total"],
            "page": history["page"],
            "page_size": history["page_size"]
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))