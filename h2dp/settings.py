# Django settings for h2dotp project.
import os.path
db_path = os.path.expanduser('~/.local/share/hamster-applet/hamster.db')
if not os.path.exists(db_path):
    raise ValueError("Hamster's DB couldn't be found. Are you sure that Hamster is installed ?")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': db_path,   # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'can_9pxy&k4r_9r3v^lmox&59!ly0j7e08o4$+rlfzypr#*e_8'

INSTALLED_APPS = (
    'h2dp.hamster'
)


# Import local_settings file


try:
    execfile(os.path.expanduser('~/.h2dp/local_settings.py'))
except IOError:
    template_path = os.path.join(os.path.dirname(__file__), 'local_settings.py.template')
    print " ~/.h2dp/local_settings.py not found. You can use %s as a template" % template_path
    import sys
    sys.exit()
