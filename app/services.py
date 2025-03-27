import requests
from sqlalchemy.orm import Session
from .models import AddressQuery
from .config import settings

class TronService:
    @staticmethod
    def get_address_info(address: str):
        """Fetch address info from Tron network"""
        url = f"{settings.tron_network_url}{address}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json().get("data", [{}])[0]
        
        return {
            "bandwidth": data.get("bandwidth", 0),
            "energy": data.get("energy", 0),
            "trx_balance": data.get("balance", 0)
        }

    @staticmethod
    def log_query(db: Session, address: str, info: dict):
        """Log query to database"""
        db_query = AddressQuery(
            address=address,
            bandwidth=info.get("bandwidth"),
            energy=info.get("energy"),
            trx_balance=info.get("trx_balance")
        )
        db.add(db_query)
        db.commit()
        db.refresh(db_query)
        return db_query

    @staticmethod
    def get_query_history(db: Session, page: int = 1, page_size: int = 10):
        """Get paginated query history"""
        offset = (page - 1) * page_size
        queries = db.query(AddressQuery).order_by(AddressQuery.timestamp.desc()).offset(offset).limit(page_size).all()
        total = db.query(AddressQuery).count()
        return {
            "queries": queries,
            "total": total,
            "page": page,
            "page_size": page_size
        }