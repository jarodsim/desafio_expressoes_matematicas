import pytest
from index import validate_math_expression


def test_validate_math_expression():
    test_cases = [
        ("((2 + 3) * [4 - 1]) / {5 * (6 - 2)}", True),
        ("[(2 + 3) * {4 - 1}] / 5 * (6 - 2)", True),
        ("((2 + 3) * [4 - 1] / {5 * (6 - 2)}", False),
        ("(2 + 3) * [4 - 1]) / {5 * (6 - 2)}", False),
        ("12346789", True),
        ("", True),
        (" ", True),
        ("[", False),
        ("[[]", False),
        ("[[]]", True),
        ("[]]", False),
        ("]]", False),
        ("(x + y @ z", False),
        (None, False),
        (123, False),
    ]

    for expression, expected in test_cases:
        assert validate_math_expression(expression) == expected
