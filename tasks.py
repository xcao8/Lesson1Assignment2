import subprocess


SRC_DIR = "/"
TEST_DIR = "/"

@task
def style(_):
    cmd = f"pycodestyle{SRC_DIR}--ignore=E501"
    subprocess.call(cmd,shell=True)

@task
def lint(_):
    cmd = f"pylint {SRC_DIR}"
    subprocess.call(cmd,shell=True)

@task
def unit_test(_):
    cmd = f"pytest {TEST_DIR}--cov{SRC_DIR}--cov"
    subprocess.call(cmd,shell=True)
