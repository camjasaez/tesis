import subprocess


def run_dev():
    subprocess.run(
        "docker-compose up -d && docker-compose logs -f detector-api", shell=True
    )


def docker_down():
    subprocess.run("docker-compose down", shell=True)


def docker_build():
    "docker build -t detector-api ."
    "docker run -p 8000:8000 --name detector-api detector-api"


def run_server():
    # docker exec -it detector-api bash
    subprocess.run("uvicorn main:app --reload", shell=True)


def run_tests():
    subprocess.run("pytest", shell=True)


if __name__ == "__main__":
    run_dev()
