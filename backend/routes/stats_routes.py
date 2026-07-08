from fastapi import APIRouter
from backend.services.catalog_service import get_statistics

router = APIRouter()


@router.get("/")
def statistics():
    return get_statistics()