from fastapi import APIRouter

from backend.services.pipeline_service import refresh_catalog

from backend.services.catalog_service import (
    get_all_databases,
    get_tables,
    get_columns
)

router = APIRouter()


@router.get("/")
def databases():
    return get_all_databases()


@router.get("/{database_name}")
def tables(database_name: str):
    return get_tables(database_name)


@router.get("/columns/{table_name}")
def get_table_columns(table_name: str):
    """
    Return metadata for all columns in a table.
    """
    return get_columns(table_name)

