run    := pipenv run
python := $(run) python
py     := $(run) pyinstrument

all: $(patsubst %.py,%.html,$(wildcard *.py))

%.html: %.py
	$(py) -o $@ $<
	open $@

.PHONY: repl
repl:
	$(run) python

clean:
	rm -f *.html

### Makefile ends here
