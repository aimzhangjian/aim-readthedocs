#!/bin/bash -x

cd /www

# python manage.py syncdb --noinput
# python manage.py migrate
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@localhost', 'admin')" | ./manage.py shell
# python manage.py makemessages --all
# python manage.py compilemessages
# python manage.py celeryd -l INFO &

./manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('aim', 'aim@localhost', '572136zhanghongs')" | ./manage.py shell
echo "yes" | ./manage.py collectstatic
./manage.py loaddata test_data &

exec "$@"
