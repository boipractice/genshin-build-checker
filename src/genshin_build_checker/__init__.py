from genshin_build_checker.api import fetch_character
from genshin_build_checker.data import load_builds


def main() -> None:
    import io
    import sys

    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
    builds = load_builds("data/builds.csv")
    print(f"Loaded {len(builds)} builds\n")

    for b in builds:
        try:
            info = fetch_character(b.character)
        except RuntimeError as err:
            print(f"Stopped: {err}")
            return
        if info is None:
            print(f"{b.character:12} NOT FOUND IN THE API")
        else:
            print(
                f"{b.character:12} {info['element']:8} {info['weapon']:9} {info['rarity']}★  {info['region']}"
            )
