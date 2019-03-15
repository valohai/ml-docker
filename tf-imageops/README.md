tf-imageops
===========

GPU-enabled Tensorflow images with preinstalled libraries:

* matplotlib 3
* OpenCV-Python 4
* Pillow 5
* scikit-image 0.14
* scikit-learn 0.20

Building
--------

* Run `make tf18` to make the GPU and CPU variants of the Tensorflow 1.8 image.
  * Run `make tf18-test-cpu` to test the CPU variant.
  * If you have `nvidia-docker` set up, run `make tf18-test-gpu` to also test the GPU variant.