"""Study Planner CLI entrypoint (Team T-W3).

Pipeline: parse_csv -> prioritise -> allocate -> render
Usage:
    python -m Shared.study_planner samples/tasks.csv --hours 2
    python -m shared.study_planner samples/tasks.csv --hours 2
"""

import argparse
import sys
from datetime import date, datetime
from pathlib import Path

# Ensure 'shared' points to 'Shared' so relative/absolute imports succeed on all systems
if "shared" not in sys.modules:
    try:
        import Shared

        sys.modules["shared"] = Shared
    except ImportError:
        pass

from Shared.study_planner.allocate import allocate
from Shared.study_planner.parse import parse_csv
from Shared.study_planner.prioritise import prioritise
from Shared.study_planner.render import render

# Import InfeasiblePlan exception from available W2 modules or define fallback
try:
    from Members.Quoc_Thuan_Cyrus.W2.errors import InfeasiblePlan
except ImportError:
    try:
        from Members.Hoang_Gia_Hung.W2.errors import InfeasiblePlan  # type: ignore
    except ImportError:

        class InfeasiblePlan(Exception):
            def __init__(self, needed_h: float, available_h: float):
                super().__init__()
                self.needed_h = needed_h
                self.available_h = available_h

            def __str__(self) -> str:
                return (
                    f"Need {self.needed_h:.1f} hours, "
                    f"but only {self.available_h:.1f} hours available."
                )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Study Planner CLI — automatically plan study schedule from CSV tasks."
    )
    parser.add_argument("file", help="Path to the tasks CSV file")
    parser.add_argument(
        "--hours",
        type=float,
        required=True,
        help="Available study hours",
    )
    parser.add_argument(
        "--today",
        type=str,
        default=date.today().isoformat(),
        help="Optional current date override (YYYY-MM-DD)",
    )

    args = parser.parse_args()

    # 1. Validate file existence
    csv_path = Path(args.file)
    if not csv_path.is_file():
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    # 2. Parse today's date
    try:
        today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
    except ValueError:
        print("Error: --today must be in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)

    # 3. Pipeline execution: parse_csv -> prioritise -> allocate -> render
    try:
        # Step 1: parse_csv
        tasks = parse_csv(csv_path)
        if not tasks:
            print("Error: The task file is empty.", file=sys.stderr)
            sys.exit(1)

        # Check feasible: available hours must be positive
        total_needed = sum(t.effort_h for t in tasks)
        if args.hours <= 0:
            raise InfeasiblePlan(total_needed, args.hours)

        # Step 2: prioritise
        prioritised_tasks = prioritise(tasks, today_date)

        # Step 3: allocate
        blocks = allocate(prioritised_tasks, args.hours)

        # Step 4: render
        output = render(blocks)

        print(f"Tonight ({args.hours:.1f} h):")
        print(output)

    except InfeasiblePlan as e:
        print(f"InfeasiblePlan: {e}", file=sys.stderr)
        sys.exit(1)
    except (ValueError, KeyError, OSError) as e:
        print(f"Error processing tasks: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
