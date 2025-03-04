import json
from pathlib import Path
from typing import Any


def get_data(filename: str) -> list[dict[str, Any]]:
    path = Path() / filename
    with open(path, mode="r") as file:
        data = json.load(file)
        return data
