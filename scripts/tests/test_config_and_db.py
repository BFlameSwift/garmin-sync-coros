import os
import tempfile
import unittest
from unittest import mock


class ConfigTests(unittest.TestCase):
    def test_load_sync_config_requires_both_accounts(self):
        from scripts.config import ConfigError, load_sync_config

        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ConfigError):
                load_sync_config()

    def test_load_sync_config_parses_newest_num_and_direction(self):
        from scripts.config import load_sync_config

        values = {
            "GARMIN_AUTH_DOMAIN": "cn",
            "GARMIN_EMAIL": "g@example.com",
            "GARMIN_PASSWORD": "secret",
            "GARMIN_NEWEST_NUM": "25",
            "COROS_EMAIL": "c@example.com",
            "COROS_PASSWORD": "secret2",
            "RUN_TYPE": "garmin_to_coros",
        }
        with mock.patch.dict(os.environ, values, clear=True):
            config = load_sync_config()
        self.assertEqual(config.garmin_newest_num, 25)
        self.assertEqual(config.run_type, "garmin_to_coros")


class DatabaseTests(unittest.TestCase):
    def test_activity_insertion_is_idempotent_and_database_is_created(self):
        from scripts.garmin.garmin_db import GarminDB
        from scripts.sqlite_db import DB_DIR

        with tempfile.TemporaryDirectory() as directory:
            with mock.patch("scripts.sqlite_db.DB_DIR", directory), mock.patch(
                "scripts.garmin.garmin_db.DB_DIR", directory
            ):
                db = GarminDB("state.db")
                db.initDB()
                db.saveActivity(123)
                db.saveActivity(123)
                self.assertEqual(db.getUnSyncActivity(), [123])


if __name__ == "__main__":
    unittest.main()
