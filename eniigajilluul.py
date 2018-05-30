def shutdown(self):
    import subprocess
    subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
