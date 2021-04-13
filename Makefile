#!/usr/bin/make

check: 
	pycodestyle openflow examples
	pylint -s n openflow examples
	git diff --check --cached
	pytest test
	make -C examples/configure

clean:
	py3clean .
	rm -fr .pytest_cache
