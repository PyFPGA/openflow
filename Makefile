#!/usr/bin/make

check: 
	pycodestyle openflow
	pylint -s n openflow
	git diff --check --cached
	pytest test

clean:
	py3clean .
	rm -fr .pytest_cache
