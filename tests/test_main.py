import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import main


def test_main_runs():
    assert main() is True
