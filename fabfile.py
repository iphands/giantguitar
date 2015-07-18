from fabric.api import run, env
from fabric.contrib.project import rsync_project

env.hosts = ["pifi.lan"]
env.user = "root"

def deploy():
    rsync_project(remote_dir="/root/giantguitar", local_dir="./", exclude=(".git*", "*.pyc", "*~"))

def stop():
    run("supervisorctl stop giantguitar")

def restart():
    run("supervisorctl restart giantguitar")
