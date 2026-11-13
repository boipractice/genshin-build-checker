from genshin_build_checker.api import fetch_character
from genshin_build_checker.data import load_builds
import logging
import time


# send warnings to logger.log and the screen. with the time and level on each line
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logger.log"),
        logging.StreamHandler(),
    ],
)
# logger use to write warnings
log = logging.getLogger(__name__)


def main() -> None:  # prints out the character information
    import io
    import sys

    # reads every build from the csv
    start = time.perf_counter()
    builds = load_builds("data/builds.csv")
    load_seconds = time.perf_counter() - start


    # prints in utf-8 so the star works in pipes
    if isinstance(sys.stdout, io.TextIOWrapper):
        sys.stdout.reconfigure(encoding="utf-8")
        

    # keeps only the builds with acceptable stats; warn about the rest
    valid_builds = []
    for b in builds:
        if b.atk <= 0:
            log.warning(f"{b.character} attack {b.atk} must be above 0")
        elif b.crit_rate > 1:
            log.warning(f"{b.character} crit rate {b.crit_rate} must be 1 or less")
        else:
            valid_builds.append(b)

    print(f"Loaded {len(builds)} builds, {len(valid_builds)} valid\n")

    start = time.perf_counter()

    # look up each valid build in the api and print the information
    for b in valid_builds:
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
    api_seconds = start = time.perf_counter() - start
    print(f"\nLoading the CSV book took {load_seconds:.2f}s, API lookups took {api_seconds:2f}s")
