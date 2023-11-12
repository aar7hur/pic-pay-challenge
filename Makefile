clean:
	find . -name "*.pyc" -exec rm -f {} \;

format:
	black picpaychallenge && isort picpaychallenge
