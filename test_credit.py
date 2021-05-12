import project_file as pd
import pytest

def test_credit(account):
    s = pd.Bank(account)

    assert s.credit(True) >= "500"

