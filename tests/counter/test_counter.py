from src.counter import count_ocurrences


def test_counter():
    response = count_ocurrences("src/jobs.csv", "National")
    assert response == 2140
    response = count_ocurrences("src/jobs.csv", "SomeWord")
    assert response == 0
