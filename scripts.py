import argparse
import subprocess
import os


def run_dev():
    print("=> Running docker-compose up")
    subprocess.run(
        "docker-compose up -d && docker-compose logs -f detector-api", shell=True
    )


def docker_down():
    print("=> Running docker-compose down")
    project_folder = os.path.basename(os.getcwd())
    subprocess.run(
        f"docker-compose down && docker rmi {project_folder}-detector-api", shell=True
    )


# def docker_build():
#     """En casode no tener docker-compose, ejecutar en orden estos comandos con el Dockerfile en la carpeta app"""
#     "docker build -t detector-api ."
#     'docker run -p 8000:8000 -v "$(pwd)/app:/app" --name detector-api detector-api'


def run_tests():
    subprocess.run("pytest", shell=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Docker script")
    parser.add_argument(
        "action", choices=["run_dev", "docker_down"], help="Action to perform"
    )
    args = parser.parse_args()

    if args.action == "run_dev":
        run_dev()
    elif args.action == "docker_down":
        docker_down()
