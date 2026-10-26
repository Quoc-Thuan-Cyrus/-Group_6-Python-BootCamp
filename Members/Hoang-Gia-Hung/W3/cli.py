"""W3-3: Command-line interface for the study planner.

Usage:
    python -m Members.Hoang-Gia-Hung.W3.cli tasks.csv --hours 2 [--today 2026-10-26]
"""

import argparse
import importlib
import sys
from datetime import date
from pathlib import Path

# Ensure repository root is on sys.path for proper package discovery
_REPO_ROOT = Path(__file__).resolve().parents[3]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

# Guarantee case-insensitive availability of the shared package
try:
    import shared
except ModuleNotFoundError:
    import Shared as shared  # type: ignore

    sys.modules["shared"] = shared

from shared.contract import Block
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise

# Import W2 loading logic
try:
    from ..W2.io_utils import load_tasks
except (ImportError, ValueError):
    _w2_io = importlib.import_module("Members.Hoang-Gia-Hung.W2.io_utils")
    load_tasks = _w2_io.load_tasks


def render_plan(blocks: list[Block], hours: float) -> str:
    """Format scheduled blocks in the standardized dotted output format.

    Example output:
        Tonight (2.0 h):
          1. Assignment ...... 1.5 h
          2. DS exam ......... 0.5 h
    """
    lines = [f"Tonight ({hours:.1f} h):"]
    if not blocks:
        lines.append("  (no tasks scheduled)")
        return "\n".join(lines)

    target_col = 28
    for idx, block in enumerate(blocks, start=1):
        prefix = f"  {idx}. {block.task.title} "
        suffix = f" {block.hours:.1f} h"
        dots_count = max(3, target_col - len(prefix) - len(suffix))
        dots = "." * dots_count
        lines.append(f"{prefix}{dots}{suffix}")

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    """Construct and configure the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Study planner CLI: prioritise and allocate study hours for tasks."
    )
    parser.add_argument(
        "file",
        help="Path to the tasks CSV file.",
    )
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours tonight.",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=date.today().isoformat(),
        help="Reference date in YYYY-MM-DD format (default: today).",
    )
    return parser


def main() -> None:
    """Entry point for the study planner CLI."""
    parser = build_parser()
    args = parser.parse_args()

    # Validate task file existence
    csv_file = Path(args.file)
    if not csv_file.is_file():
        print(f"Error: The file '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    # Validate --today format
    try:
        today_date = date.fromisoformat(args.today)
    except ValueError:
        print("Error: --today must be in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)

    # Process tasks and generate schedule
    try:
        tasks = load_tasks(csv_file)
        prioritised_tasks = prioritise(tasks, today_date)
        blocks = allocate(prioritised_tasks, args.hours)
        output = render_plan(blocks, args.hours)
        print(output)
    except (ValueError, OSError, KeyError) as exc:
        print(f"Error processing tasks: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
