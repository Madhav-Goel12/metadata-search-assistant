from backend.services.dataset_scanner import scan_datasets
from backend.services.metadata_extractor import extract_metadata

files = scan_datasets()

# Test only the first dataset
metadata = extract_metadata(files[0])

print("=" * 80)
print(f"Columns Found : {len(metadata)}")
print("=" * 80)

for column in metadata:

    print(column)