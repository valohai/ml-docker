.PHONY: tf18

tf18:
	docker build -t valohai/tf-imageops:tf18-gpu --build-arg=BASE_VERSION=1.8.0-devel-gpu-py3 .
	docker build -t valohai/tf-imageops:tf18-cpu --build-arg=BASE_VERSION=1.8.0-devel-py3 .

tf18-test-cpu:
	docker run -it -v ${CURDIR}:/app:ro valohai/tf-imageops:tf18-cpu python3 /app/test.py

tf18-test-gpu:
	nvidia-docker run -it -v ${CURDIR}:/app:ro valohai/tf-imageops:tf18-gpu python3 /app/test.py	

tf18-test: tf18-test-cpu tf18-test-gpu