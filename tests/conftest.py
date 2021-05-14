import logging
import pyperclip
import pytest

LOGGER = logging.getLogger(__name__)


@pytest.fixture(scope='function')
def example_fixture():
    LOGGER.info("Setting Up Example Fixture...")
    yield
    LOGGER.info("Tearing Down Example Fixture...")

@pytest.fixture(scope='function')
def copy_to_clipboard():
    pytest.test_solution = "SOLUTION:Of Pancakes and Spaceships,Sisyphus192 #feelthebern,115-1-6,Min Symbols\r\nCOMPONENT:'empty-research-reactor',2,0,''\r\nMEMBER:'instr-start',0,0,128,0,1,0,0\r\nMEMBER:'instr-start',180,0,32,1,6,0,0\r\nMEMBER:'instr-output',-1,0,32,0,6,0,0\r\nMEMBER:'instr-arrow',180,0,64,7,1,0,0\r\nMEMBER:'instr-grab',-1,2,128,7,1,0,0\r\nMEMBER:'instr-input',-1,0,128,1,1,0,0\r\nMEMBER:'instr-grab',-1,1,128,2,1,0,0\r\nMEMBER:'instr-arrow',0,0,64,1,1,0,0\r\nPIPE:0,4,1\r\nPIPE:1,4,2"
    pyperclip.copy(pytest.test_solution)
