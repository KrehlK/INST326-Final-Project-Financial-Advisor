#Abdul's pytest

import project_file as pf 
import pytest

def test_saving(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'no')

    with open('data.csv') as f:
        b = pf.Bank(f)
        c = pf.Customer(112233456789, b)
        
        c.saving(1000)
        assert c.get_bal() == 53519.00
        c.saving(400)
        assert c.get_bal() == 53919.00
         c.saving(100)
        assert c.get_bal() == 54019.00
         c.saving(50)
        assert c.get_bal() == 54069.00
           c.saving(300)
        assert c.get_bal() == 54369.00