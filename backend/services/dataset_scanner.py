from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATASET_DIR = BASE_DIR / "datasets"


def scan_datasets():
    """
    Scan the datasets directory and return all CSV files.

    Returns:
        list[dict]
    """

    csv_files = []

    # Iterate through dataset folders
    for dataset_folder in DATASET_DIR.iterdir():

        if not dataset_folder.is_dir():
            continue

        # Iterate through CSV files
        for csv_file in dataset_folder.glob("*.csv"):

            csv_files.append({

                "database_name": dataset_folder.name,

                "table_name": csv_file.stem,

                "file_path": csv_file

            })

    return csv_files