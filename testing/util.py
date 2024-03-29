# Copyright (c) 2014 pre-commit dev team: Anthony Sottile, Ken Struys
from __future__ import annotations

import os.path

TESTING_DIR = os.path.abspath(os.path.dirname(__file__))


def get_resource_path(path):
    return os.path.join(TESTING_DIR, 'resources', path)
