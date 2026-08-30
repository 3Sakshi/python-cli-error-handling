# python-cli-error-handling
A simple command-line interface (CLI) tool built in Python that safely divides an integer by a divisor and provides clear error messages.

## Features
- Accepts an integer from the command line.
- Supports a custom divisor using `--divide-by`.
- Uses `2` as the default divisor.
- Handles division by zero with a clear error message.
- Provides helpful `--help` information.
- Uses appropriate exit codes for errors.

## Requirements
- Python 3.x

## Usage
Run the program with:

```bash
python cli_tool.py 10

Output:
Result: 5.0

### Custom divisor
python cli_tool.py 10 --divide-by 5

Output:
Result: 2.0

### Division by zero
python cli_tool.py 10 --divide-by 0

Output:
Error: Cannot divide by zero.

### Help
python cli_tool.py --help

## Error Handling
The program provides user-friendly error messages instead of exposing raw Python tracebacks for expected errors.

## Project Structure
python-cli-error-handling/
├── cli_tool.py
└── README.md

## Author
Sakshi Tayade