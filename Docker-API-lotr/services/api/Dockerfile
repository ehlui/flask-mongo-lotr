FROM python:3.8

LABEL MAINTAINER="ehlui"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD requirements.txt /var/www

RUN pip install -r requirements.txt
# If we dont bind the host it will use the local one (only available in the container)
# ie it will only be used inside the cointainer
CMD ["flask", "run", "--host", "0.0.0.0"]
