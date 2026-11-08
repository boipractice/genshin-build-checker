import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Build:
    character: str
    atk: float
    crit_rate: float
    crit_dmg: float
    good: int


def load_builds(path: str | Path) -> list[Build]:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
        return [
            Build(
                character=row["character"],
                atk=float(row["atk"]),
                crit_rate=float(row["crit_rate"]),
                crit_dmg=float(row["crit_dmg"]),
                good=int(row["good"]),
            )
            for row in rows
        ]


def save_parquet(csv_path: str, parquet_path: str) -> None:
    import pandas as pd

    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path)
