from fastapi import APIRouter, HTTPException
from backend.services.pipeline_service import refresh_catalog

router = APIRouter()


@router.post("/")
def refresh():
    """
    Rebuild the metadata catalog by rescanning all datasets.
    """
    try:

        stats = refresh_catalog()

        return {
            "status": "success",
            "message": "Metadata catalog refreshed successfully.",
            "statistics": stats
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Catalog refresh failed: {str(e)}"
        )