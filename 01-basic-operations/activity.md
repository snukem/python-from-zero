# Activity: Basic Operations

Write all of your code in a single file named `basic-operations.py` in your working directory.

When run with `python basic-operations.py`, your script must print exactly **10 lines** — one answer per problem, in order. Print only the requested answer on each line: no problem numbers, labels, or extra text.

Use the given values in each problem exactly as written.

Check your work by running `python answer-key.py` from the same directory. It reports PASS or FAIL for each problem.

---

## Problem Set

**1. Variable assignment and addition**
Assign `15` to `x` and `25` to `y`, then print their sum.
*Output: a single integer.*

**2. Floats and combined arithmetic**
Assign `12.5` to `item_price`, `4` to `quantity`, and `5.0` to `discount`. Multiply the price by the quantity, subtract the discount, and print the result.
*Output: a single float.*

**3. Multiple assignment**
On a single line, assign `5`, `10`, and `15` to `a`, `b`, and `c`. Print their product.
*Output: a single integer.*

**4. F-string formatting**
Assign `"Python"` to `name` and `3` to `version`. Print a line reading `<name> version <version>`.
*Output: `<name> version <version>`.*

**5. Integer division and modulus**
Assign `27` to `total_items` and `5` to `items_per_box`. Use `//` to find the number of full boxes and `%` to find the leftover items.
*Output: `Boxes: <boxes>, Leftover: <leftover>`.*

**6. Type casting**
Given `str_num1 = "100"` and `str_num2 = "25.5"`, cast `str_num1` to an integer and `str_num2` to a float. Add them, cast the sum to an integer, and print it.
*Output: a single integer.*

**7. String length and indexing**
Assign `"Fundamentals"` to `text`. Print its length, the character at index `0`, and the character at index `-1`.
*Output: `<length>:<first_char> to <last_char>`.*

**8. Operator precedence**
Evaluate `2 ** 3 + 10 // 3 * 4 - 5 % 3` as written — no added parentheses — and print the result.
*Output: a single integer.*

**9. Casting, percentage math, and currency output**
Assign `base_price = "80"`, `tax_rate = "0.15"`, and `shipping = 10`. Convert `base_price` and `tax_rate` to floats, then compute `base_price * (1.0 + tax_rate) + shipping`, formatted to exactly two decimal places.
*Output: `Total: $<total_cost>`, with the cost shown to exactly two decimal places.*

**10. Unpacking, slicing, and exponentiation**
On a single line, assign `"PY2026"`, `"99"`, and `"3"` to `code1`, `code2`, and `code3`. Then:
  1. Slice the numeric portion out of `code1` (everything from index 2 onward) and cast it to an integer.
  2. Cast `code2` and `code3` to integers.
  3. Compute `key_val = ((code1_num + code2_num) ** code3_num) // 1000`.
  4. Slice the two-letter prefix from the front of `code1`.
*Output: `<prefix>-<key_val>`.*
