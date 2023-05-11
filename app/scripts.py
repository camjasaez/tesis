import subprocess


def run_dev():
    subprocess.run("docker-compose up -d && docker-compose logs -f", shell=True)


def run_server():
    subprocess.run("unicorn app.main:app --reload", shell=True)


def run_tests():
    subprocess.run("pytest", shell=True)


if __name__ == "__main__":
    run_dev()
