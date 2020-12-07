import os
import subprocess
from invoke import task

CURR_DIR = os.path.abspath(os.path.dirname(__file__))
SRC_DIR = os.path.join(CURR_DIR, "signal_interpreter_client")
TEST_DIR = os.path.join(CURR_DIR, "tests")
COV_FILE = os.path.join(CURR_DIR, "coveragerc")
INT_TEST_DIR = os.path.join(CURR_DIR, "tests/Integration")

@task
def style(_):
    cmd = f"pycodestyle {SRC_DIR} --ignore=E501"
    subprocess.call(cmd, shell=True)

@task
def lint(_):
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd, shell=True)

@task
def unit_test(_):
    cmd = f"pytest {TEST_DIR} --cov {SRC_DIR} --verbose --cov-config {COV_FILE}"
    subprocess.call(cmd, shell=True)

@task
def integration_test():
    cmd = f"pytest {INT_TEST_DIR}"
    subprocess.call(cmd,shell=True)
