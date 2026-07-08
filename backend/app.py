from fastapi import FastAPI

from backend.routes.health_routes import router as health_router
from backend.routes.stats_routes import router as stats_router
from backend.routes.search_routes import router as search_router
from backend.routes.catalog_routes import router as catalog_router
from backend.routes.pipeline_routes import router as pipeline_router


app = FastAPI(
    title="Metadata Search Assistant",
    description="Search metadata extracted from Kaggle datasets.",
    version="1.0.0"
)

# -------------------------------------------------------
# Health Routes
# -------------------------------------------------------

app.include_router(
    health_router,
    tags=["Health"]
)

# -------------------------------------------------------
# Statistics Routes
# -------------------------------------------------------

app.include_router(
    stats_router,
    prefix="/stats",
    tags=["Statistics"]
)

# -------------------------------------------------------
# Search Routes
# -------------------------------------------------------

app.include_router(
    search_router,
    prefix="/search",
    tags=["Search"]
)

# -------------------------------------------------------
# Catalog Routes
# -------------------------------------------------------

app.include_router(
    catalog_router,
    prefix="/databases",
    tags=["Catalog"]
)

# -------------------------------------------------------
# Pipeline Routes
# -------------------------------------------------------

app.include_router(
    pipeline_router,
    prefix="/refresh",
    tags=["Pipeline"]
)