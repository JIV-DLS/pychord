FROM python:3.6

WORKDIR /app

COPY tests_find_successors_in_N_nodes.py main.py

RUN pip3 install numpy
RUN pip3 install tqdm

COPY . .

CMD [ "python3", "main.py"]