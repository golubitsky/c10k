FROM python:3

WORKDIR /usr/src/app
ENV PYTHONPATH /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "ipython" ]