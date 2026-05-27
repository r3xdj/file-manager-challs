FROM python:3.11-slim

RUN useradd -ms /bin/bash ctf

WORKDIR /home/ctf/file_manager_3

COPY main.py flag.txt Dockerfile ./ 

RUN chown -R ctf:ctf /home/ctf/file_manager_3 \
    && chmod 755 /home/ctf/file_manager_3 \
    && chown root:root flag.txt \
    && chmod 444 flag.txt \
    && chown root:root main.py \
    && chmod 544 main.py

USER root

CMD ["python3", "-u", "main.py"]