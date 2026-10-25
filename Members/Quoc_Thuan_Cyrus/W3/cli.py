import argparse
import os
import sys
from datetime import date, datetime

# Adjust these imports based on your actual W2 module structure
from Members.Quoc_Thuan_Cyrus.W2.io_utils import load_tasks
from shared.study_planner.allocate import allocate
from shared.study_planner.prioritise import prioritise
from shared.study_planner.render import render


def main():
    parser = argparse.ArgumentParser(description="Study Planner CLI")
    parser.add_argument("file", help="Path to the tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available hours")
    parser.add_argument("--today", type=str, default=date.today().isoformat(), 
                        help="Optional current date (YYYY-MM-DD)")
    
    args = parser.parse_args()

    # Exit with code 1 if file is missing
    if not os.path.isfile(args.file):
        print(f"Error: The file '{args.file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    try:
        today_date = datetime.strptime(args.today, "%Y-%m-%d").date()
    except ValueError:
        print("Error: --today must be in YYYY-MM-DD format.", file=sys.stderr)
        sys.exit(1)

    # Reusing W2 Code
    try:
        tasks = load_tasks(args.file)
        prioritised_tasks = prioritise(tasks, today_date)
        blocks = allocate(prioritised_tasks, args.hours)
        output = render(blocks)
        print(f"Tonight ({args.hours:.1f} h):")
        print(output)
    except ValueError as e:
        print(f"Error processing tasks: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()