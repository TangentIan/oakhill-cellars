up:
	@docker-compose up

upd:
	@docker-compose up -d

build:
	@docker-compose build --build-arg BUILD=DEV

stop:
	@docker-compose stop

down:
	@docker-compose down

restart:
	@docker-compose restart

restartc:
	@docker-compose restart celery

restartw:
	@docker-compose restart web

test:
	@docker-compose run --rm web coverage run --source='.' manage.py test $(app) --parallel

coveragereport:
	@docker-compose run --rm web coverage report

coveragexml:
	@docker-compose run --rm web coverage xml

coveragehtml:
	@docker-compose run --rm web coverage html

makemigrations:
	@docker-compose run --rm web python manage.py makemigrations

migrate:
	@docker-compose run --rm web python manage.py migrate

shell:
	@docker-compose run --rm web python manage.py shell

collectstatic:
	@docker-compose run --rm web python manage.py collectstatic

logs:
	@docker-compose logs -tf

logsw:
	@docker-compose logs -tf web

logsc:
	@docker-compose logs -tf celery

lint:
	@echo -e 'Applying Flake8 linting';
	@docker-compose run --rm web flake8 \
		--max-line-length=88 \
		--exclude='**migrations/,**tests/,.git,**/__pycache__,**/node_modules' \
		--exit-zero
	@echo -e 'All done';

import:
	@docker-compose run --rm web python manage.py import

importleave:
	@docker-compose run --rm web python manage.py import_leave

mystify:
	@docker-compose run --rm web python manage.py mystify

delete:
	@docker-compose run --rm web python manage.py delete

build-docs:
	cd docs && vuepress build
run-docs:
	cd docs && vuepress dev

crud:
	ansible-playbook automation/create_crud.yml -i automation/inventory

docgen:
	@docker-compose run --rm web python manage.py docgen
