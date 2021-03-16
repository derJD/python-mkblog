PODMAN := podman run -it --rm -v ./:/builds/${PWD##*/} -w /builds/${PWD##*/} gitlab.der-jd.de:5050/containers/python-build:latest

.PHONY: all help

all: help

package:
	${PODMAN} pylint pyproject-build --sdist --wheel
install:
	pip install .
list:
	pip show ${PWD##*/}
lint:
	${PODMAN} bash -c 'pip install .; pylint --exit-zero -f parseable src/'
container:
	@echo "#########################################################"
	@echo "# pip install .                                         #"
	@echo "# mkdocs -v serve -f example/mkdocs.yml -a 0.0.0.0:8000 #"
	@echo "#########################################################"

	podman run -it --rm \
		--pull always \
		-p 8000:8000 \
		-v ./:/builds/$${PWD##*/} \
		-w /builds/$${PWD##*/} \
		gitlab.der-jd.de:5050/containers/mkdocs:latest bash

help:
	@echo -e "Available targets:\n"
	@awk -F ':' '$$0~/^\S+:$$/ || $$2 ~ /glr-check/ {print $$1}' Makefile
