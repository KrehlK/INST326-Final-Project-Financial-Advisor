# Michael's Customer withdraw() method test

import project_file as pf
import pytest

def test_withdraw(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'no')

    with open('data.csv') as f:
        b = pf.Bank(f)
        c = pf.Customer(112233445566, b)
        
        assert c.withdraw(0) == 1000.00
        assert c.withdraw(50) == 950.00
        assert c.withdraw(50.50) == 899.50
        assert c.withdraw(1000) == 899.50
        assert c.withdraw(899.51) == 899.50
        assert c.withdraw(899.50) == 0F