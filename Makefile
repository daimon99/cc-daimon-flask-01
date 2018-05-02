all: test

clean:
	rm -rf /tmp/yourapplication/

test: clean
	cookiecutter . --output-dir /tmp --no-input && \
	cd /tmp/yourapplication && \
	pip install -r requirements.txt && \
	fab dev
