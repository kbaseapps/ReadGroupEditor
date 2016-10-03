FROM kbase/kbase:sdkbase.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

# RUN apt-get update

RUN mkdir -p /kb/module/work && mkdir -p /kb/module/lib
RUN chmod 777 /kb/module
WORKDIR /kb/module

# Genbank uploader uses the data_api, so install that to our lib directory
RUN git clone https://github.com/kbaseapps/SetAPI && \
    cd SetAPI && \
    git checkout ed7c907 && \
    cd /kb/module && \
    cp -vr SetAPI/lib/SetAPI lib/
# -----------------------------------------

COPY ./ /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
