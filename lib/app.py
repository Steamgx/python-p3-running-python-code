import os

print("Hello World! Pass this test, please.")

def test_app_py_exists():
    assert os.path.exists("lib/app.py")
