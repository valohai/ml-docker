ARG BASE_VERSION
FROM tensorflow/tensorflow:${BASE_VERSION}
RUN apt-get update && apt-get install -y libsm6 libxrender1 libfontconfig1 libxext6 && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip3 install --no-cache -U pip wheel setuptools
RUN pip3 install --no-cache -U opencv-contrib-python~=4.0 pillow~=5.0 scikit-learn~=0.20 scikit-image~=0.14 matplotlib~=3.0