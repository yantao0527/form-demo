# setup local env

install-requirements:
	pip install -r deployment/requirements.txt

# local dev

dev:
	python backend/main.py

form-test:
	python backend/form_assistant_test.py
