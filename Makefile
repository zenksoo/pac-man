RM = rm -rf

PY_CACHE=$$(find . -type d -name __pycache__)
MYPY_CACHE=$$(find . -type d -name ".mypy_cache")

install:
	@uv sync

run:
	@uv run pac-man.py config.json

debuge:
	@uv run -m pdb pac-man.py config.json

clean:
	@rm -rf $(PY_CACHE) $(MYPY_CACHE)

lint:
	@uv tool run flake8 . --exclude=.venv/

	@uv tool run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
