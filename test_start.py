import start
import pytest

@pytest.mark.parametrize("number, output", [(5, "buzz"),(3, "fizz"), (15, "fizzbuzz")])
def test_fizzbuzzer(number, output):
    assert start.fizz_buzzer(number) == output
