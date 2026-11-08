import json
import os
import urllib.error
import urllib.parse
import urllib.request

API_URL = os.getenv(
    "GENSHIN_API_URL", "https://genshin-db-api.vercel.app/api/v5/characters"
)


def fetch_character(name: str) -> dict | None:
    url = f"{API_URL}?query={urllib.parse.quote(name)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        raise RuntimeError(f"API answered with error {err.code} for {name!r}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(f"Can't reach the API: {err.reason}") from err
    if not body:
        return None
    data = json.loads(body)
    return {
        "element": data["elementText"],
        "weapon": data["weaponText"],
        "rarity": data["rarity"],
        "region": data["region"],
    }
