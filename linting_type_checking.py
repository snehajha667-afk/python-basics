"""
Linting and Type Checking Example

Run:
python linting_type_checking.py

Lint:
python -m flake8 linting_type_checking.py

Type Check:
python -m mypy linting_type_checking.py
"""

from typing import List


def calculate_average(marks: List[int]) -> float:
    """Calculate the average marks."""
    return sum(marks) / len(marks)


def find_highest(marks: List[int]) -> int:
    """Return the highest mark."""
    return max(marks)


student_marks = [85, 90, 78, 92, 88]

average = calculate_average(student_marks)
highest = find_highest(student_marks)

print(f"Marks   : {student_marks}")
print(f"Average : {average:.2f}")
print(f"Highest : {highest}")
