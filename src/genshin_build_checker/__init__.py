import os

from genshin_build_checker.data import load_builds, save_parquet


def main() -> None:
    builds = load_builds("data/builds.csv")
    print(f"Loaded {len(builds)} builds")

    good = [b.character for b in builds if b.good == 1]
    print("Good builds:", good)

    save_parquet("data/builds.csv", "data/builds.parquet")
    for f in ["data/builds.csv", "data/builds.parquet"]:
        print(f, os.path.getsize(f), "bytes")
