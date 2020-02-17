Docker build for ReadTheDocs
==================================

This repository provides Dockerfile for [Read The Docs][0]

### Status
Built images are uploaded to [index.docker.io][1]

### Tags

There are currently tags available depending of the way to distribute content:

 -  `latest`: Which rely on the [`django-manage runserver` command][6], this **should not be used for production**

### Quickstart:

### Enterprise Docker configuration

These images will expose the **port** `8000` for the web application as well as the `/www` **volume** which contains all the django project.

We have two things to do for enterprise docker configuration:
 - Set the data fold `/www/user_builds` as Volume Mapping to host machine.
 - Set domain `RTD_PRODUCTION_DOMAIN` for the producntion environment. For HAND dockerfile edition we only support MySQL now.
 - Set the metadata database configration.

You can also use the following `environment variables` while building Docker image :

 -  `RTD_PRODUCTION_DOMAIN`: Stands for `PRODUCTION_DOMAIN`in readthedocs settings (can be formed like "{host}:{port}"). e.g.: `docs.saas.hand-china.com`.
 -  `DJANGO_DB_ENGINE`,e.g.: `django.db.backends.mysql`
 -  `DJANGO_DB_NAME`,e.g.: `readthedocs`
 -  `DJANGO_DB_USER`,e.g.: `readthedocs`
 -  `DJANGO_DB_PASSWORD`,e.g.: `readthedocs`
 -  `DJANGO_DB_HOST`,e.g.: `XXX.XXX.XXX.XXX`
 -  `DJANGO_DB_PORT`,e.g.: `3306`

  [0]: http://readthedocs.org
  [1]: https://index.docker.io/u/shaker/
  [2]: http://docs.docker.io/en/latest/ "docs.docker.io"
  [3]: http://127.0.0.1:8000/
  [4]: https://docs.readthedocs.org/en/latest/settings.html
  [5]: http://gunicorn.org/
  [6]: https://docs.djangoproject.com/en/1.9/ref/django-admin/#runserver-port-or-address-port
  [7]: http://docs.gunicorn.org/en/latest/deploy.html
