# =========================================================
# Verifier — run_to_verify.py
# =========================================================
# Run this file to check your answers:
#   python run_to_verify.py
# If you haven't edited glocal_practice.py yet, this will tell you.
# =========================================================

from glocal_practice import *
import math

EXPECTED = {
    "extract_page_numbers": (123, 456),
    "replace_whitespace": "GLOCAL_foundation_of_Canada",
    "glocal_to_list": ['g','l','o','c','a','l'],
    "extract_age": 25,
    "replace_commas": "Toronto; Ontario; Canada",
    "capitalize_words": "Python Programming",
    "reverse_string": "LACOLG",
    "extract_digits": "123",
    "convert_and_add": 50,
    "join_list": "apple,banana,cherry",
    "split_hyphen": ["data", "analysis", "with", "python"],
    "count_names": 3,
    "percent_pages_done": 26.97,
    "canada_age": 158,
    "trim_spaces": "extra spaces",
    "extract_domain": "glocalfoundation.ca",
    "uppercase_letters": ['P','Y','T','H','O','N'],
    "average_list": 30,
    "sum_numbers": "5",
    "extract_date_parts": (2025, 11, 7),
    "uppercase_world": "Hello WORLD",
    "count_s": 4,
    "convert_strings_to_ints": [1,2,3,4],
}

TASKS = [
    ("extract_page_numbers", extract_page_numbers),
    ("replace_whitespace", replace_whitespace),
    ("glocal_to_list", glocal_to_list),
    ("extract_age", extract_age),
    ("replace_commas", replace_commas),
    ("capitalize_words", capitalize_words),
    ("reverse_string", reverse_string),
    ("extract_digits", extract_digits),
    ("convert_and_add", convert_and_add),
    ("join_list", join_list),
    ("split_hyphen", split_hyphen),
    ("count_names", count_names),
    ("percent_pages_done", percent_pages_done),
    ("canada_age", canada_age),
    ("trim_spaces", trim_spaces),
    ("extract_domain", extract_domain),
    ("uppercase_letters", uppercase_letters),
    ("average_list", average_list),
    ("sum_numbers", sum_numbers),
    ("extract_date_parts", extract_date_parts),
    ("uppercase_world", uppercase_world),
    ("count_s", count_s),
    ("convert_strings_to_ints", convert_strings_to_ints),
]

def almost_equal(a, b, tol=1e-9):
    """Helper for comparing floats like percent_pages_done."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) <= tol or round(a, 2) == round(b, 2)
    return a == b

def run_checks():
    results = []
    all_none = True

    for name, fn in TASKS:
        try:
            got = fn()
        except Exception as e:
            results.append((name, "ERROR", f"raised {type(e).__name__}: {e}"))
            all_none = False
            continue

        expected = EXPECTED[name]

        if got is not None:
            all_none = False

        ok = almost_equal(got, expected)
        if ok:
            results.append((name, "PASS", got))
        else:
            results.append((name, "FAIL", f"got {got!r} expected {expected!r}"))

    if all_none:
        print("\nYou haven’t started in glocal_practice.py (everything returned None).")
        print("Edit glocal_practice.py where it says # TODO, save, then run this file again.\n")
        return

    passes = sum(1 for r in results if r[1] == "PASS")
    fails = sum(1 for r in results if r[1] == "FAIL")
    errors = sum(1 for r in results if r[1] == "ERROR")

    for name, status, info in results:
        if status == "PASS":
            print(f"[PASS] {name}")
        elif status == "FAIL":
            print(f"[FAIL] {name} — {info}")
        else:
            print(f"[ERROR] {name} — {info}")

    total = len(results)
    print("\nSummary:")
    print(f"  Passed: {passes}/{total}")
    print(f"  Failed: {fails}")
    print(f"  Errors: {errors}")

    if passes == total:
        print("\nALL COMPLETE — GREEN LIGHT! Great work.")
    else:
        print("\nNot done yet - check your TODOs in glocal_practice.py and re-run.")
        print("\nNeed a hint? Run hints.py to solve math for hints on each question.\n")

if __name__ == "__main__":
    run_checks()
