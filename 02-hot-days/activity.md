# Activity: Hot Days

Write all of your code in a single file named `hot-days.py` in your working directory.

The file `data/sensor_readings.txt` holds one temperature reading per line, in degrees.

When run with `python hot-days.py`, your script must read that file, count how many readings are **strictly greater than** `30.0`, and print exactly one line:

```
Hot readings: <count>
```

Print only that line — no problem numbers, labels, or extra text.

Check your work by running `python answer-key.py` from the same directory. It reports PASS or FAIL.

---

## Notes

- Read the file rather than counting by hand or pasting the numbers into your script. The point of this module is the reading and the loop.
- "Strictly greater than" means a reading of exactly `30.0` does **not** count.
- Each line comes out of the file as a string with a newline on the end. You will need to convert it to a number before you can compare it.
- Every line in this file is a clean number. Later modules will hand you messier data.
