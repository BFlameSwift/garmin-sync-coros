import os
from dataclasses import dataclass

# getting content root directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)


GARMIN_FIT_DIR = os.path.join(parent, "garmin-fit")
COROS_FIT_DIR = os.path.join(parent, "coros-fit")

DB_DIR =  os.path.join(parent, "db")


class ConfigError(ValueError):
    """Raised when the sync job is not configured with both accounts."""


@dataclass(frozen=True)
class SyncConfig:
    garmin_auth_domain: str
    garmin_email: str
    garmin_password: str
    garmin_newest_num: int
    coros_email: str
    coros_password: str
    sync_limit: int = 10000
    run_type: str = "garmin_to_coros"


def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise ConfigError(f"Missing required environment variable: {name}")
    return value


def load_sync_config() -> SyncConfig:
    domain = _required("GARMIN_AUTH_DOMAIN").upper()
    if domain not in {"CN", "COM"}:
        raise ConfigError("GARMIN_AUTH_DOMAIN must be CN or COM")
    try:
        newest = int(os.getenv("GARMIN_NEWEST_NUM", "10000"))
    except ValueError as exc:
        raise ConfigError("GARMIN_NEWEST_NUM must be an integer") from exc
    if newest < 0:
        raise ConfigError("GARMIN_NEWEST_NUM must be non-negative")
    run_type = os.getenv("RUN_TYPE", "garmin_to_coros").strip().lower()
    if run_type not in {"garmin_to_coros", "coros_to_garmin"}:
        raise ConfigError("RUN_TYPE must be garmin_to_coros or coros_to_garmin")
    try:
        sync_limit = int(os.getenv("SYNC_LIMIT", "10000"))
    except ValueError as exc:
        raise ConfigError("SYNC_LIMIT must be an integer") from exc
    if sync_limit < 1:
        raise ConfigError("SYNC_LIMIT must be at least 1")
    return SyncConfig(
        garmin_auth_domain=domain,
        garmin_email=_required("GARMIN_EMAIL"),
        garmin_password=_required("GARMIN_PASSWORD"),
        garmin_newest_num=newest,
        coros_email=_required("COROS_EMAIL"),
        coros_password=_required("COROS_PASSWORD"),
        sync_limit=sync_limit,
        run_type=run_type,
    )
