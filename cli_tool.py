import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="CLI tool with real error handling"
    )

    parser.add_argument("number", type=int, help="Enter an integer")
    parser.add_argument("--divide-by", type=int, default=2)

    args = parser.parse_args()

    try:
        if args.divide_by == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        result = args.number / args.divide_by
        print(f"Result: {result}")

    except ZeroDivisionError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()