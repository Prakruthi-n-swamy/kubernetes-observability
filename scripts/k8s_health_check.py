import subprocess

pods = subprocess.check_output(
    ["kubectl", "get", "pods"]
)

print(
    pods.decode("utf-8")
)
