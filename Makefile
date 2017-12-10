test:
	cd src/tests; \
	python3 utilities_test.py; \
	python3 fetchdata_test.py

clean:
	find . -name "*.pyc" -type f -delete

mrproper:
	find . -name "__pycache__" -type d -delete
