import start
import pytest

@pytest.mark.parametrize("number, output", [(1, 1), (5, "buzz"),(3, "fizz"), (15, "fizzbuzz")])
def test_fizzbuzzer(number, output):
    assert start.fizz_buzzer(number) == output


@pytest.mark.parametrize("number, output", [
    (3, [1, 2, "fizz"]),
    (15, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]),
    (5, [1, 2, "fizz", 4, "buzz"]),
    (-5, ["zubb", -4, "zzif", -2, -1])
]
                         )
def test_fizzbuzz(number, output):
    assert start.fizzbuzz(number) == output
