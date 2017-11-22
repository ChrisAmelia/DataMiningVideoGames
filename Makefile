test:
	cd src/tests; \
	python3 *.py

clean:
	find . -name "*.pyc" -type f -delete

mrproper:
	find . -name "__pycache__" -type d -delete
