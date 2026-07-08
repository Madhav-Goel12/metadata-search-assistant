from backend.services.dataset_scanner import scan_datasets
from backend.services.metadata_extractor import extract_metadata
from backend.services.catalog_service import (
    insert_metadata,
    clear_catalog,
    get_statistics,
)


def build_catalog():
    """
    Scan datasets, extract metadata, and insert it into the catalog.
    """

    files = scan_datasets()

    all_metadata = []

    for file in files:
        print(f"Processing: {file['table_name']}")

        metadata = extract_metadata(file)

        all_metadata.extend(metadata)

    insert_metadata(all_metadata)

    print(f"\nSuccessfully indexed {len(all_metadata)} columns.")


def refresh_catalog():
    """
    Clear the existing catalog and rebuild it.
    """

    print("Refreshing catalog...\n")

    clear_catalog()

    build_catalog()

    stats = get_statistics()

    print("\n========== Catalog Statistics ==========")
    print(f"Databases : {stats['databases']}")
    print(f"Tables    : {stats['tables']}")
    print(f"Columns   : {stats['columns']}")
    print("========================================")

    return stats