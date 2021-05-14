import pyperclip

class SpacechemSolver:

    @staticmethod
    def run():
        print("Hello World...")

    @staticmethod
    def get_solution_from_clipboard() -> list[str]:
        return pyperclip.paste().split('/r/s')