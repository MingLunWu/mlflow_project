FROM tensorflow/tensorflow

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install -r requirements.txt \
&& rm requirements.txt

EXPOSE 8888

CMD ["bash"]