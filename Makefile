# Deployment and server setup

version=master
stage=staging
configure:
	@ansible-playbook devops/site.yml -i devops/inventory/$(stage) --limit=all

deploy:
	@ansible-playbook devops/deploy.yml -i devops/inventory/$(stage) -e 'APP_VERSION=$(version)' --limit=all


# for dev debugging.
run2:
	@sudo killall -9 supervisord | echo
	@sudo killall -9 gunicorn | echo
	@python manage.py validate --settings=config.settings.development &
	@python manage.py collectstatic --noinput --settings=config.settings.development &
	@python manage.py syncdb --noinput --settings=config.settings.development &
	@python manage.py migrate --settings=config.settings.development &
	@authbind --deep python manage.py runserver 0.0.0.0:3000 --settings=config.settings.development

cel:
	@sudo killall -9 celery | echo
	@export DJANGO_SETTINGS_MODULE="config.settings.development" && \
	celery worker -A some_app --loglevel=DEBUG --beat --autoreload --concurrency=2 #--events 


superuser:
	@python manage.py createsuperuser --settings=config.settings.development

shell:
	@python manage.py shell_plus --settings=config.settings.development

ssh:
	ssh -o ServerAliveInterval=20 user@something

mk:
	@python manage.py makemigrations some_app --settings=config.settings.development

flush:
	@python manage.py flush --no-initial-data --settings=config.settings.development

reload:
	@ansible-playbook devops/deploy.yml -i devops/inventory/development --limit=all
