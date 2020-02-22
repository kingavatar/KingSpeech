import subprocess
def commands(command):
    if  "lock" in command.lower() and "unlock" not in command.lower():
        subprocess.call(["loginctl","lock-session"])
    if "unlock" in command.lower():
        subprocess.call([ "loginctl","unlock-session" ])
    if "reboot" in command.lower():
        subprocess.call("reboot")
    if "poweroff" in command.lower() or  "shutdown" in command.lower() or "shut up" in command.lower():
        subprocess.call("poweroff")
