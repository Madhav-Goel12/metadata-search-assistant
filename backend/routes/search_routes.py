from fastapi import APIRouter

from backend.services.search_service import search_metadata

router = APIRouter()


@router.get("/")
def search(keyword: str):
    """
    Search metadata.
    """

    return search_metadata(keyword)