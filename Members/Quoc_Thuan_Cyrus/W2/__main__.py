import sys

from .io_utils import load_tasks


def main():
    # Define the path to your sample CSV file
    # (Adjust this path if your CSV is named differently or located elsewhere)
    csv_path = "sample.csv" 
    
    # Alternatively, allow passing the file path as a command-line argument:
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]

    try:
        # Load the sample CSV and print the tasks
        tasks = load_tasks(csv_path)
        print(f"Successfully loaded {len(tasks)} tasks:")
        for task in tasks:
            print(task)
    except FileNotFoundError:
        print(f"Error: Could not find the file '{csv_path}'")
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()