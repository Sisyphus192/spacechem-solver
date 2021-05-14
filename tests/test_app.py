from .context import spacechem_solver
import pytest


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    spacechem_solver.SpacechemSolver.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out

def test_app(copy_to_clipboard):
    # pylint: disable=W0612,W0613
    solution = spacechem_solver.SpacechemSolver.get_solution_from_clipboard()
    assert solution == pytest.test_solution.split('\r\s')