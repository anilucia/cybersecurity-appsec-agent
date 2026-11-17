import importlib.util
import pathlib
import unittest

BASE = pathlib.Path(__file__).resolve().parents[1] / "examples" / "sql-injection"


def load(filename, name):
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TestSqlInjectionScenario(unittest.TestCase):
    def test_vulnerable_case_demonstrates_bypass(self):
        app = load("app.py", "unsafe_app")
        con = app.create_database()
        try:
            self.assertTrue(app.authenticate(con, "aluno", "senha-ficticia"))
            self.assertTrue(app.authenticate(con, "' OR 1=1 -- ", "qualquer"))
        finally:
            con.close()

    def test_fixed_case_blocks_bypass(self):
        app = load("app_fixed.py", "safe_app")
        con = app.create_database()
        try:
            self.assertTrue(app.authenticate(con, "aluno", "senha-ficticia"))
            self.assertFalse(app.authenticate(con, "' OR 1=1 -- ", "qualquer"))
            self.assertFalse(app.authenticate(con, "aluno", "errada"))
        finally:
            con.close()


if __name__ == "__main__":
    unittest.main()
