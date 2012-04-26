
import os.path

DB_PATH = os.path.expanduser('~/.local/share/hamster-applet/hamster.db')
if not os.path.exists(DB_PATH):
    raise ValueError("Hamster's DB couldn't be found. Are you sure that Hamster is installed ?")


try:
    execfile(os.path.expanduser('~/.h2dp/local_settings.py'))
except IOError:
    template_path = os.path.join(os.path.dirname(__file__), 'local_settings.py.template')
    print " ~/.h2dp/local_settings.py not found. You can use %s as a template" % template_path
    import sys
    sys.exit()

MARK_TAG  = '_logged_in_dp_'      #change this could cause unsync problems. Take care.
