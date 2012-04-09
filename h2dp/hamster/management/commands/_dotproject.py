#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from _browser import Browser

class LoginFailed(ValueError): pass
class InvalidTask(ValueError): pass
class LogFail(ValueError): pass

class DotProjectBot(object):

    def __init__(self, base_url):
        self.br = Browser()
        self.base_url = base_url
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        logging.basicConfig(level=logging.INFO)

    def login(self, username, password):
        self.br.open(self.base_url)
        self.br.select_form(name="loginform")
        self.br['username'] = username
        self.br['password'] = password
        response = self.br.submit()

        if 'Login Failed' in response.read():
            raise LoginFailed('username and/or password are incorrect')
        else:
            logging.info("logged in")

    def log_task(self, dp_task_id, date, hours, description):
        url = self.base_url + 'index.php?m=tasks&a=view&task_id=%d&tab=1' % int(dp_task_id)
        response = self.br.open(url)
        if '<td class="error">Task ID is invalid' in response.read():
            raise InvalidTask("The task doesn't exists in dP or you don't have the permission to see it")

        self.br.select_form('editFrm')
        self.br.form.set_all_readonly(False)
        self.br['task_log_date'] = date.strftime('%Y%m%d')
        self.br['task_log_hours'] = str(hours)
        self.br['task_log_description'] = description
        response = self.br.submit()

        if not '<td class="message">Task Log inserted</td>' in response.read():
            raise LogFail('Something seems to be wrong. Please check %s' % url)
        else:
            msg = u"«%s (%s hs)» was logged succesfully" % (description, str(hours))
            logging.info(msg)
        

        

