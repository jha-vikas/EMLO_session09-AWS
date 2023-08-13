# EMLOv3 | Assignment 09

[![pytorch](https://img.shields.io/badge/PyTorch_2.0+-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/get-started/locally/)
[![black](https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray)](https://black.readthedocs.io/en/stable/)


## GPT on Harry Potter text deployed on AWS
- The trained model checkpoint is stored in S3, to be accessed using 'aws_access_key_id' & 'aws_secret_access_key'.
- The gpt_jit model is deployed as Fargate spot container deployment on AWS ECS.
- The deployment url is updated on 'deployment.json'.
- Demo Web UI (Gradio) must run on port 80 and should be publicly accessible.


## To run demo

- Access the url in deployment.json

![aws_deployment](screenshots/aws_deployment.jpg)

## Author

- Vikas Jha