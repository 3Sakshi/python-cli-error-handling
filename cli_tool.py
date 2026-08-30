import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="A CLI tool that safely divides an integer by a divisor.",
        epilog="Example: python cli_tool.py 10 --divide-by 2"
    )

    parser.add_argument(
        "number",
        type=int,
        help="The integer to divide"
    )

    parser.add_argument(
        "--divide-by",
        type=int,
        default=2,
        help="The divisor (default: 2)"
    )

    try:
        args = parser.parse_args()

        if args.divide_by == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        result = args.number / args.divide_by
        print(f"Result: {result}")

    except ZeroDivisionError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except KeyboardInterrupt:
        print("\nError: Program interrupted by user.", file=sys.stderr)
        sys.exit(130)

    except Exception as error:
        print(f"Unexpected error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()