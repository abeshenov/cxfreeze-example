FROM python:3

WORKDIR /app

COPY requirements.txt app.py setup ./
RUN pip install --no-cache-dir --requirement requirements.txt
RUN cxfreeze app.py
RUN tar -zcvf app.tar.gz build/exe.linux-x86_64-*

CMD bash
