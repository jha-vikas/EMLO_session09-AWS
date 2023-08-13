FROM python:3.10-slim-buster

WORKDIR /workspace

COPY requirements.txt .


RUN pip3 install -r requirements.txt && rm -rf /root/.cache/pip

COPY demo_gpt_jit.py .

EXPOSE 80

CMD [ "python3", "demo_gpt_jit.py"]
