from locust import user,task,between
class MyTest(user.HttpUser):
    wait_time = between(1,1)

    @task
    def login_test(self):
        url = 'commerceapi/member/login'
        params = {}
        self.client.post(url=url,data=params,timeout=10)