from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset folder
DATASET_DIR = BASE_DIR / "datasets"

# Metadata folder
METADATA_DIR = BASE_DIR / "metadata"

# Create folders if they don't exist
DATASET_DIR.mkdir(exist_ok=True)
METADATA_DIR.mkdir(exist_ok=True)