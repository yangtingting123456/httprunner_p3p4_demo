
from httprunner.api import HttpRunner
runner = HttpRunner(failfast=False)
runner.run('testcases\\20201204\\acg-login-interfaces.yml')