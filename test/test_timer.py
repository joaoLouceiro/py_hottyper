import pytest
from tkinter import Tk
from hottyper.main import Timer

@pytest.fixture(scope="module")
def tk_root():
    root = Tk()
    yield root
    root.destroy()

