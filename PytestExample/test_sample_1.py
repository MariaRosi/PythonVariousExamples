import pytest

def test_m1():
    assert True

def test_m2():
    assert False

def test_m3():
    assert 100 == 100

@pytest.mark.login
def test_login():
    assert 100 == 100