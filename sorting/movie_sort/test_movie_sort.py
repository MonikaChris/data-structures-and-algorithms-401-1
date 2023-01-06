import pytest
from movie_sort import year_sort, movies


def test_year_sort():
    actual = year_sort(movies)
    # Expected test output of test #1
    expected1 = ["The Intouchables", "Valkyrie", "Ratatouille", "Stardust", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

    assert actual == expected1

# Expected test output of test #2
# expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento",
#              "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"]

