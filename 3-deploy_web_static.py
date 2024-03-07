#!/usr/bin/python3
"""A fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from datetime import datetime
from fabric.api import *
from os import path
import re

env.user = 'ubuntu'
env.hosts = ['34.204.81.235', '18.234.107.45']
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

def deploy():
    """Deploys an archive to web servers"""
    # if archive_path is None:
    #     return False
    archive_path = do_pack()
    if not path.exists(archive_path):
        return False
    
    put(archive_path, "/tmp/")
    # get the archive filename without extension
    pattern = r'\/([^\/.]+)\.'
    match = re.search(pattern, archive_path)
    pathname = match.group(1)
    # create destination folder for unzipping
    destination_path = "/data/web_static/releases/{}".format(pathname)
    run("mkdir -p {}".format(destination_path))
    # unzip files to destination folder
    run("tar -xvzf /tmp/{} -C /data/web_static/releases/{}".format(
        archive_path.split('/')[1], pathname))
    # delete archive
    sudo("rm -rf /tmp/{}".format(archive_path.split('/')[1]))
    # delete old symbolic link
    run("rm -rf /data/web_static/current")
    # move all contents of decompressed web_static to
    # destination folder, then delete it
    run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}".format(pathname, pathname))
    run("rm -rf /data/web_static/releases/{}/web_static".format(pathname))
    # add new symbolic link
    run("ln -sf {} /data/web_static/current".format(destination_path))

    return True
