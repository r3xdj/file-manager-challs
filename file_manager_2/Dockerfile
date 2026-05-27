FROM python:3.11-slim

RUN useradd -ms /bin/bash ctf

WORKDIR /home/ctf/file_manager_2

COPY main.py flag.txt ./ 

RUN chown -R ctf:ctf /home/ctf/file_manager_2 \
    && chmod 755 /home/ctf/file_manager_2 \
    && chown root:root flag.txt \
    && chmod 400 flag.txt \
    && chown root:root main.py \
    && chmod 500 main.py

USER root

CMD ["python3", "-u", "main.py"]