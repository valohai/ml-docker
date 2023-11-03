FROM sofiiavalohai/valohai-llms:v1.5

# Update the package list and install necessary dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3.9 python3.9-dev python3.9-distutils python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Create a symbolic link for python3.9 to python3


# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip
# Install required libraries
RUN pip install valohai-utils peft accelerate bitsandbytes torch>=1.10 transformers -U bitsandbytes -q trl xformers wandb datasets einops gradio sentencepiece -q -U datasets scipy ipywidgets

# Set the working directory
WORKDIR /app

# Copy your application files to the container (if needed)
# COPY . /app

# Specify the default command to be executed when the container starts
# CMD [ "python", "your_script.py" ]
