import json
from pathlib import Path
import requests
from .credentials import creds

# Reuse the loaded credentials and keep a requests session
session = requests.Session()


def _update_env(env_path: str, updates: dict) -> None:
    """Update or append key/value pairs in the given .env file."""
    env_file = Path(env_path)
    lines = env_file.read_text().splitlines() if env_file.exists() else []

    new_lines = []
    seen = set()
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            new_lines.append(line)
            continue

        key, _, _ = line.partition("=")
        key = key.strip()
        if key in updates:
            new_lines.append(f"{key}={updates[key]}")
            seen.add(key)
        else:
            new_lines.append(line)

    for key, value in updates.items():
        if key not in seen and not any(l.startswith(f"{key}=") for l in new_lines):
            new_lines.append(f"{key}={value}")

    trailing = "\n" if new_lines else ""
    env_file.write_text("\n".join(new_lines) + trailing)


class GetServices:
    def __init__(self):
        self.tenant = creds.tenant
        self.base_url = creds.base_url
        self.tenant = creds.tenant

    def CallServices(self):
        endpoint = self.base_url + self.tenant
        print("------------------------")
        print(endpoint)
        print("------------------------")
        response = session.get(endpoint)
        data = response.json()

        tenant_id, services = next(iter(data.items()))
        wanted_keys = ("3DCOMPASS", "3DPASSPORT", "3DSPACE")
        filtered = {tenant_id: {k: services[k]["url"] for k in wanted_keys if k in services}}
        print(json.dumps(filtered, indent=2, ensure_ascii=False))
        return filtered

    def SaveCoreUrlsToEnv(self, data: dict | None = None, env_path: str = ".env"):
        """Save Compass/Passport/Space URLs to the provided .env file."""
        if data is None:
            data = self.CallServices()
        tenant_id, services = next(iter(data.items()))
        env_updates = {
            "3DCompassURL": services.get("3DCOMPASS", ""),
            "3DPassportURL": services.get("3DPASSPORT", ""),
            "3DSpaceURL": services.get("3DSPACE", ""),
        }
        _update_env(env_path, env_updates)
        print("-----------------------------")
        print("Env Updated Successfully")
