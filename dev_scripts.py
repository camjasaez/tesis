import argparse
import subprocess


def run_dev():
    docker_build()
    docker_run()


def docker_run():
    command = (
        'docker run -p 8000:8000 -v "$(pwd)/app:/app" --name detector-api detector-api'
    )
    subprocess.run(command, shell=True)


def docker_build():
    subprocess.run("docker build -t detector-api .", shell=True, check=True)


def docker_down():
    subprocess.run("docker rm -f detector-api", shell=True)
    subprocess.run("docker rmi detector-api", shell=True)


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
