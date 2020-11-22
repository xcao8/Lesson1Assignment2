import subprocess
from invoke import task

SRC_DIR = "src"
TEST_DIR = "src"

@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
    subprocess.call(cmd,shell=True)

@task
def lint(_):
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd,shell=True)

@task
def unit_test(_):
    cmd = f"pytest {TEST_DIR} --cov {SRC_DIR} --verbose"
    subprocess.call(cmd,shell=True)
