#!/usr/bin/python3
"""A fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from datetime import datetime
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['34.204.81.235']
env.key_filename = "~/.ssh/id_rsa_alx"


def create_folder():
    """Creates a folder named versions"""
    local('mkdir -p versions')


def do_pack():
    """generates a .tgz archive from the
    contents of the web_static folder"""
    tp = datetime.now()
    filename = "web_static_{}{}{}{}{}{}.tgz".format(
        tp.year, tp.month, tp.day, tp.hour, tp.minute, tp.second)
    create_folder()
    res = local("tar -czf versions/{} ./web_static".format(filename),
                capture=True)
    if res.return_code != 0:
        return None
    return "versions/{}".format(filename)
