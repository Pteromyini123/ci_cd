import argparse, subprocess, sys, os, shutil


def run(cmd: list[str]) -> None:
    print(">", *cmd)
    subprocess.run(cmd, check=True)

def network_exists(name: str) -> bool:
    return shutil.which("docker") and subprocess.run(
        ["docker", "network", "inspect", name],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    ).returncode == 0


p = argparse.ArgumentParser(description="Deploy both micro-services locally")
p.add_argument("--version_service1", default="latest",
               help="Docker tag za service1 (default: latest)")
p.add_argument("--version_service2", default="latest",
               help="Docker tag za service2 (default: latest)")
p.add_argument("--port_s1", type=int, default=8080, help="Host-port za service1")
p.add_argument("--port_s2", type=int, default=5003, help="Host-port za service2")
p.add_argument("--network", default="hashnet", help="Docker network name")
args = p.parse_args()


if not shutil.which("docker"):
    sys.exit("Docker nije pronađen u PATH-u.")


if network_exists(args.network):
    print(f"> docker network inspect {args.network}   # već postoji")
else:
    run(["docker", "network", "create", args.network])


subprocess.run(["docker", "rm", "-f", "service1"],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(["docker", "rm", "-f", "service2"],
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

run([
    "docker", "run", "--rm", "-d",
    "--name", "service1",
    "--network", args.network,
    "-p", f"{args.port_s1}:8080",
    f"ghcr.io/pteromyini123/service1:{args.version_service1}"
])



run([
    "docker", "run", "--rm", "-d",
    "--name", "service2",
    "--network", args.network,
    "-p", f"{args.port_s2}:8080",
    "-e", "SERVICE1_URL=http://service1:8080/",
    f"ghcr.io/pteromyini123/service2:{args.version_service2}"
])

print("\n Services are running:")
print(f"   • service1 (hash)  → http://localhost:{args.port_s1}/")
print(f"   • service2 (fetch) → http://localhost:{args.port_s2}/")
print("Stop:  docker stop service2 service1 && "
      f"docker network rm {args.network}")
