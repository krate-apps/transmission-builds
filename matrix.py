#!/usr/bin/env python3
import yaml

TRANSMISSION_VERSIONS = [
    "4.0.6",
    "4.1.0",
    "4.1.1",
    "4.1.3",
]

matrix = [{"version": version, "os": "debian-13", "codename": "trixie"} for version in TRANSMISSION_VERSIONS]
print(yaml.safe_dump({"include": matrix}, sort_keys=False))
