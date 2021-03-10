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
	${PODMAN} pylint --exit-zero -f parseable src/

help:
	@echo -e "Available targets:\n"
	@awk -F ':' '$$0~/^\S+:$$/ || $$2 ~ /glr-check/ {print $$1}' Makefile
