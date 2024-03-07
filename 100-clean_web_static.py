#!/usr/bin/python3
"""deletes out-of-date archives, using the function do_clean"""
from glob import glob
from fabric.api import *
from os import path
import re

env.user = 'ubuntu'
env.hosts = ['34.204.81.235', '18.234.107.45']
env.key_filename = "~/.ssh/id_rsa_alx"


def do_clean(number=0):
    """Deletes out of date archives minus
    n number to keep"""
    dir = "versions/"
    # get the list of files locally and sort
    files = list(filter(path.isfile, glob(dir + "*")))
    files.sort()
    # create new list containing only files to be kept
    num = int(number)
    if num <= 1:
        k_files = files[-1:]
    else:
        num_to_keep = -1 * num
        k_files = files[num_to_keep:]
    for f in files:
        if f not in k_files:
            local("rm -f {}".format(f))
    pattern = r'\/([^\/.]+)\.'
    files_online = [re.search(pattern, f).group(1) for f in files]
    k_files_online = [re.search(pattern, f).group(1) for f in k_files]
    for f in files_online:
        if f not in k_files_online:
            run("rm -rf /data/web_static/releases/{}".format(f))
