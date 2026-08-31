"""Check a student's `basic-operations.py` against the expected output.

Usage: python answer-key.py [path-to-script]

Prints PASS or FAIL for each of the 10 problems. It deliberately does not
show the expected values -- work out a failing problem yourself.
"""

import subprocess
import sys
from pathlib import Path

EXPECTED = [
    "40",
    "45.0",
    "750",
    "Python version 3",
    "Boxes: 5, Leftover: 2",
    "125",
    "12:F to s",
    "18",
    "Total: $102.00",
    "PY-9595703",
]


def run_student_script(script_path):
    """Return the student script's non-empty output lines, stripped."""
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def report(output_lines):
    """Print PASS/FAIL per problem and return the number passed."""
    passed = 0
    for number, expected in enumerate(EXPECTED, start=1):
        actual = output_lines[number - 1] if number <= len(output_lines) else None
        if actual == expected:
            passed += 1
            print(f"Problem {number:2d}: PASS")
        else:
            print(f"Problem {number:2d}: FAIL")
    return passed


def main():
    script_path = Path(sys.argv[1] if len(sys.argv) > 1 else "basic-operations.py")

    if not script_path.exists():
        sys.exit(f"Could not find {script_path}. Run this from the same directory as your script.")

    try:
        output_lines = run_student_script(script_path)
    except subprocess.TimeoutExpired:
        sys.exit(f"{script_path} did not finish running. Check for an infinite loop.")

    passed = report(output_lines)
    print(f"\nScore: {passed}/{len(EXPECTED)}")


if __name__ == "__main__":
    main()
