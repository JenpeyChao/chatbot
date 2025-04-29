set -o errexit
pip in stall -r requirements.txt
python manage.py collectstatic --no-input
pyhton manage.py migrate