# Creates docker container
#       original source:
#           https://github.com/scitran-apps/fsl-bet/blob/master/Dockerfile
#       modified by amf Nov 2022 for captk-coregistration gear
#

#############################################
# Select the OS
FROM cbica/captk:2021.03.29
LABEL authors="CBICA_UPenn <software@cbica.upenn.edu>"

# # # install required Python packages
# # FROM python:3.9.7-slim-buster
# RUN sudo apt update
# RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# RUN apt-get install -y python3-pip
# # RUN pip install -r requirements.txt
# RUN set -ex \
#     && apt-get update && apt-get install -y ca-certificates build-essential git --no-install-recommends \
#     && git clone -b v1.26.1 https://github.com/numpy/numpy.git 

#############################################
# Setup default flywheel/v0 directory
ENV FLYWHEEL=/flywheel/v0
RUN mkdir -p ${FLYWHEEL}
WORKDIR ${FLYWHEEL}
COPY run ${FLYWHEEL}/run
COPY manifest.json ${FLYWHEEL}/manifest.json

#############################################
# Configure entrypoint
RUN chmod a+x /flywheel/v0/run
ENTRYPOINT ["/flywheel/v0/run"]
