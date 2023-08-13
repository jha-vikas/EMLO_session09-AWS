import unittest
import json

from gradio_client import Client


class TestGPTGradio(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("deployment.json") as f:
            cls.base_url = json.load(f)["base_url"]

        print(f"using base_url={cls.base_url}\n\n")

    def test_predict(self):
        client = Client(self.base_url)
        result = client.predict(
            """THE RIDDLE HOUSE 

The villagers of Little Hangleton still called it “the 
Riddle House,” even though it""",
            512,
            api_name="/predict"
        )
        print(f"got result = {result}")


if __name__ == '__main__':
    unittest.main()
