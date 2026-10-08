from pathlib import Path
import zipfile
import requests

DATASETS = {
    "pizza_steak_sushi": (
        "https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip"
    ),
    "pizza_steak_sushi_20_percent": (
        "https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi_20_percent.zip"
    ),
}

DATA_DIR = Path("data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def download_file(url: str, destination: Path) -> None:
    if destination.exists():
        print(f"[skip] {destination} already exists")
        return

    print(f"[download] {destination.name}")
    with requests.get(url, stream=True, timeout=60) as response:
        response.raise_for_status()
        with open(destination, "wb") as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)


def extract_zip(zip_path: Path, destination: Path) -> None:
    train_dir = destination / "train"
    test_dir = destination / "test"

    if train_dir.is_dir() and test_dir.is_dir():
        print(f"[skip] {destination} already extracted")
        return

    destination.mkdir(parents=True, exist_ok=True)
    print(f"[extract] {zip_path.name} -> {destination}")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(destination)


def main() -> None:
    for folder_name, url in DATASETS.items():
        zip_path = DATA_DIR / f"{folder_name}.zip"
        extract_path = DATA_DIR / folder_name

        download_file(url, zip_path)
        extract_zip(zip_path, extract_path)

    print("\nDone. Both datasets are ready in the data/ directory.")


if __name__ == "__main__":
    main()
