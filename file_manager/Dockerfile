FROM python:3.11-slim

RUN useradd -ms /bin/bash ctf

WORKDIR /home/ctf/file_manager

COPY main.py flag.txt ./ 

RUN chown -R ctf:ctf /home/ctf/file_manager \
    && chmod 755 /home/ctf/file_manager \
    && chmod 755 main.py

USER ctf

CMD ["python3", "-u", "main.py"]