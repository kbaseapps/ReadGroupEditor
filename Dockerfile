FROM kbase/kbase:sdkbase.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

RUN mkdir -p /kb/module/work && mkdir -p /kb/module/lib
RUN chmod 777 /kb/module
WORKDIR /kb/module

COPY ./ /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
