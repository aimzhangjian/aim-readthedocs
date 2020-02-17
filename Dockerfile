FROM aim/readthedocs-basic

COPY ./ /www/

WORKDIR /www

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./local_settings.py ./readthedocs/settings/
COPY ./rtfd-start.sh ./

RUN chmod +x rtfd-start.sh
RUN chmod +x manage.py
RUN chmod +x setup.py
RUN chmod +x local_settings.py
RUN chmod +x fabfile.py
RUN pip install --upgrade pip

EXPOSE 8000
ENTRYPOINT ["./rtfd-start.sh"]

CMD ["/www/manage.py", "runserver", "0.0.0.0:8000"]