from hw_average import compute_hw_average
from pytest import approx


def test_no_submissions_is_zero_average():
    assert compute_hw_average([]) == approx(0)


def test_one_submission_average():
    assert compute_hw_average([5]) == approx(5)


def test_all_same_scores_is_average():
    assert compute_hw_average([5, 5, 5]) == approx(5)


def test_lowest_grade_dropped():
    assert compute_hw_average([0, 5, 7]) == approx(6)


def test_average_is_float():
    assert compute_hw_average([0, 1, 2, 3, 4]) == approx(10/4)
