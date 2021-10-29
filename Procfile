release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input
web: gunicorn myproject.wsgi --log-file -
sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0