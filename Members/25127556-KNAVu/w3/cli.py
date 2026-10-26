import argparse
from datetime import date
from pathlib import Path
import sys

def main() -> None:
    parser = argparse.ArgumentParser(description="Study planner CLI tool")
    parser.add_argument("csv_file", type=str, help="Path to tasks CSV file")
    parser.add_argument("--hours", type=float, required=True, help="Available study hours")
    parser.add_argument("--today", type=str, default=date.today().isoformat(), help="Date override YYYY-MM-DD")
    args = parser.parse_args()
    csv_path = Path(args.csv_file)
    if not csv_path.is_file():
        print(f"Error: File '{args.csv_file}' not found.", file=sys.stderr)
        sys.exit(1)
    try:
        _ = date.fromisoformat(args.today)
    except ValueError:
        print("Error: Invalid date format for --today. Use YYYY-MM-DD.", file=sys.stderr)
        sys.exit(1)
    print(f"Tonight ({args.hours:.1f} h):")

if __name__ == "__main__":
    main()
