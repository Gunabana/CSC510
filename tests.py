from hw1 import execute
import pytest

def test_execute_validInput(capsys):
    execute("N")
    actual = capsys.readouterr().out.strip()
    expected = "Okay, that is smart. Shutting down."
    assert actual == expected
    # assert execute('N') == "Okay, that is smart. Shutting down."

def test_execute_invaldInput(): # crashes program
    assert execute('l') ==  "This Should Fail"




