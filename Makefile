# containers/python-build is located on a private registry
#  which is known to podman via ~/.config/containers/registries.conf
# containers/python-build is a container with
#   build, setuptools_scm, pylint, twine installed via pip3
#
CBIN := podman
CFLAGS := run -it --rm \
			--pull always \
			-v ./:/builds/${PWD##*/} \
			-w /builds/${PWD##*/} \
			containers/python-build:latest

.PHONY: all help

all: help

package:
	${CBIN} ${CFLAGS} pyproject-build --sdist --wheel

install:
	pip install .

list:
	pip show ${PWD##*/}

lint:
	${CBIN} ${CFLAGS} bash -c 'pip install .; pylint --exit-zero -f parseable src/'

serve:
	${CBIN} ${CFLAGS} bash -c 'pip install .; mkdocs -v serve -f example/mkdocs.yml -a 0.0.0.0:8000'

help:
	@echo -e "Available targets:\n"
	@awk -F ':' '$$0~/^\S+:$$/ || $$2 ~ /glr-check/ {print $$1}' Makefile
