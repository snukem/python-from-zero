"""Check a student's `hot-days.py` against the expected output.

Usage: python answer-key.py [path-to-script]

Prints PASS or FAIL. It deliberately does not show the expected value --
work the answer out yourself.
"""

import subprocess
import sys
from pathlib import Path

EXPECTED = [
    "Hot readings: 9",
]


def run_student_script(script_path):
    """Return the student script's non-empty output lines, stripped."""
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        timeout=10,
    )
    if result.returncode != 0:
        sys.exit(f"{script_path} crashed before it finished:\n\n{result.stderr}")
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def report(output_lines):
    """Print PASS/FAIL per expected line and return the number passed."""
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
    script_path = Path(sys.argv[1] if len(sys.argv) > 1 else "hot-days.py")

    if not script_path.exists():
        sys.exit(f"Could not find {script_path}. Run this from the same directory as your script.")

    try:
        output_lines = run_student_script(script_path)
    except subprocess.TimeoutExpired:
        sys.exit(f"{script_path} did not finish running. Check for an infinite loop.")

    passed = report(output_lines)

    if len(output_lines) > len(EXPECTED):
        print(f"\nNote: your script printed {len(output_lines)} lines; only {len(EXPECTED)} was expected.")

    print(f"\nScore: {passed}/{len(EXPECTED)}")


if __name__ == "__main__":
    main()
