import subprocess
import pexpect
import sys
from MongoDBConf import (
    USERNAME,
    PASSWORD,
    COMMIT_MESSAGE,
    EXPORT_DB_COLLECTION,
    IMPORT_DB_COLLECTION
)


def print_cmd(cmd, type="Send Command"):
    print("############################################")
    print(type)
    print(cmd)
    print("############################################")


def send_command(cmd):
    print_cmd(cmd)
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(stdout)


def git_login(handle, username, password):
    out = handle.expect(["Username .*:"])
    print_cmd(out, "Out Response")
    if out == 0:
        print_cmd(username)
        handle.sendline(username)
        res = handle.expect(["Password .*:"])
        print_cmd(res, "Out Response")
        if res == 0:
            print_cmd(password)
            handle.sendline(password)
    out = handle.read()
    print_cmd(out, "Out Response")


def git_command(cmd):
    print_cmd(cmd)
    child = pexpect.spawn(cmd)
    git_login(child, USERNAME, PASSWORD)


# print argument received
print_cmd(sys.argv, "Arguments Received")

# get action from argument
action = sys.argv[1]

# print the action
print_cmd(action, "Action Received")

if action == "export":
    # mongo export from DB
    for item in EXPORT_DB_COLLECTION:
        cmd = "mongoexport --db={} --collection={} --out=Dump/{}.json".format(item["db"], item["collection"], item["file_name"])
        send_command(cmd)

    # git status
    send_command("git status")

    # git add
    send_command("git add {}".format("Dump"))

    # git commit
    send_command("git commit -m {}".format(COMMIT_MESSAGE))

    # git push
    git_command("git push")

elif action == "import":
    # git pull
    git_command("git pull")

    # Mongo import from json file
    for item in IMPORT_DB_COLLECTION:
        cmd = "mongoimport --db={} --collection={} --file=Dump/{}.json".format(item["db"], item["collection"], item["file_name"])
        send_command(cmd)

else:
    pass
