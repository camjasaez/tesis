import subprocess


def run_app():
    subprocess.run("uvicorn main:app --reload", shell=True)


def install_dependencies():
    subprocess.run("pip install -r requirements.txt", shell=True)


def run_tests():
    subprocess.run("pytest", shell=True)


if __name__ == "__main__":
    run_app()
