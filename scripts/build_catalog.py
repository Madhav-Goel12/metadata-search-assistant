from backend.services.dataset_scanner import scan_datasets
from backend.services.metadata_extractor import extract_metadata
from backend.services.catalog_service import insert_metadata

files = scan_datasets()

total_columns = 0

for file in files:

    print(f"Processing {file['table_name']}...")

    metadata = extract_metadata(file)

    insert_metadata(metadata)

    total_columns += len(metadata)

print("\n====================================")
print("Catalog Build Complete")
print(f"Files Processed : {len(files)}")
print(f"Columns Indexed : {total_columns}")
print("====================================")