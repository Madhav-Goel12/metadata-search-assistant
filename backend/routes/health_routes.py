from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def health_check():
    """
    Health check endpoint.
    """
    return {
        "message": "Metadata Search Assistant API is running."
    }