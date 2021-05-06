import project_file as pf
import pytest

def test_deposit(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'no')

    with open('data.csv') as f:
        b = pf.Bank(f)
        c = pf.Customer(112233445566, b)
        
        assert c.deposit(0) == 1000.00
        assert c.deposit(50) == 1050.00
        assert c.deposit(50.50) == 1050.50
        assert c.deposit(1000) == 2000.00
        assert c.deposit(899.51) == 1899.51
        assert c.deposit(899.50) == 1899.50
