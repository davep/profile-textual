run          := pipenv run
python       := $(run) python
pyinstrument := $(run) pyinstrument
py           := $(pyinstrument)

.PHONY: repl
repl:
	$(run) python

%::
	$(py) -o $@.html $@.py
	open $@.html

### Makefile ends here
