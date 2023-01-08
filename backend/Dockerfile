FROM python:3.9

ARG PROJECT_DIR

RUN mkdir -p ${PROJECT_DIR}

COPY main.py ${PROJECT_DIR}/main.py
COPY requirements.txt ${PROJECT_DIR}/requirements.txt
COPY finalized_model.sav ${PROJECT_DIR}/finalized_model.sav

RUN pip install --no-cache-dir --upgrade -r ${PROJECT_DIR}/requirements.txt

EXPOSE 16000/tcp

WORKDIR ${PROJECT_DIR}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "16000"]

