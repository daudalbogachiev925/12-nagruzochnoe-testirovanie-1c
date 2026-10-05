from locust import HttpUser, task, between

class OneCUser(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def open_document(self):
        self.client.get("/hs/test/document?id=123")

    @task(2)
    def post_document(self):
        self.client.post("/hs/test/post", json={'ref': 'abc'})

    @task(1)
    def run_report(self):
        self.client.post("/hs/test/report", json={'kind': 'sales'})
