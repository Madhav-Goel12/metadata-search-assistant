from pathlib import Path

DATASET_DIR = Path("../datasets")

for dataset in DATASET_DIR.iterdir():

    print(dataset.name)

    for file in dataset.glob("*"):

        print("   ", file.name)