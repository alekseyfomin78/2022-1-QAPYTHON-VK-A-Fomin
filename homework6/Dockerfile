FROM python:3.10

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && rm -rf /requirements.txt

CMD ["start_tests.sh"]