include .env
export

run:
	poetry run python main.py

jupyter:
	jupyter-lab

autogenstudio:
	@poetry run autogenstudio ui --port 8081
