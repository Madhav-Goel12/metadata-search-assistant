from backend.services.dataset_scanner import scan_datasets

files = scan_datasets()

print("\n" + "=" * 70)
print(f"Found {len(files)} CSV files")
print("=" * 70)

for i, file in enumerate(files, start=1):
    print(f"""
File {i}
--------------------------
Database : {file['database_name']}
Table    : {file['table_name']}
Path     : {file['file_path']}
""")