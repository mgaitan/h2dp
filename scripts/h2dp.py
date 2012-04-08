#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.management import setup_environ, call_command
from h2dp import settings
setup_environ(settings) 

if __name__ == '__main__':
	call_command('loghours')

