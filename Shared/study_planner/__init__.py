"""Study planner package exports and compatibility layer."""

import sys

# Ensure 'shared' points to 'Shared' for cross-platform imports
if "shared" not in sys.modules:
    try:
        import Shared

        sys.modules["shared"] = Shared
    except ImportError:
        pass

from Shared.contract import Block, Task
from Shared.study_planner.allocate import allocate
from Shared.study_planner.parse import parse_csv
from Shared.study_planner.prioritise import prioritise
from Shared.study_planner.render import render

__all__ = [
    "Block",
    "Task",
    "allocate",
    "parse_csv",
    "prioritise",
    "render",
]
