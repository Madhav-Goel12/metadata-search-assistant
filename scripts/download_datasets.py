import kaggle
from pathlib import Path

from config import DATASET_DIR
from datasets import DATASETS


def download_dataset(name, slug):

    destination = DATASET_DIR / name

    destination.mkdir(exist_ok=True)

    print(f"Downloading {name}...")

    kaggle.api.dataset_download_files(
        slug,
        path=destination,
        unzip=True
    )

    print(f"Finished {name}")


def main():

    for name, slug in DATASETS.items():

        try:
            download_dataset(name, slug)

        except Exception as e:

            print(f"Failed {name}")

            print(e)


if __name__ == "__main__":
    main()