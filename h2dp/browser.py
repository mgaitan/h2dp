#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import cookielib
import logging

# Browser
class Browser(mechanize.Browser):

    def __init__(self, *args, **kwargs):
        mechanize.Browser.__init__(self, *args, **kwargs)   #old style class
        cj = cookielib.LWPCookieJar()
        self.set_cookiejar(cj)

        # Browser options
        self.set_handle_equiv(True)
        self.set_handle_redirect(True)
        self.set_handle_referer(True)
        self.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        self.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #self.set_debug_http(True)
        #self.set_debug_redirects(True)
        #self.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        ua = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0'
        self.addheaders = [('User-agent', ua)]



class DotProjectBot(object):

    class LoginFailed(ValueError): pass
    class InvalidTask(ValueError): pass
    class LogFail(ValueError): pass


    def __init__(self, base_url):
        self.br = Browser()
        self.base_url = base_url
        if not self.base_url.endswith('/'):
            self.base_url += '/'
        

    def login(self, username, password):
        self.br.open(self.base_url)
        self.br.select_form(name="loginform")
        self.br['username'] = username
        self.br['password'] = password
        response = self.br.submit()

        if 'Login Failed' in response.read():
            raise DotProjectBot.LoginFailed('username and/or password are incorrect')
        else:
            logging.info("logged in")

    def log_task(self, dp_task_id, date, hours, description):
        url = self.base_url + 'index.php?m=tasks&a=view&task_id=%d&tab=1' % int(dp_task_id)
        response = self.br.open(url)
        if '<td class="error">Task ID is invalid' in response.read():
            raise DotProjectBot.InvalidTask("The task %d doesn't exists in" \
                    "dP or you don't have the permission to see it" % dp_task_id)

        self.br.select_form('editFrm')
        self.br.form.set_all_readonly(False)
        self.br['task_log_date'] = date.strftime('%Y%m%d')
        self.br['task_log_hours'] = str(hours)
        self.br['task_log_description'] = description
        response = self.br.submit()

        if not '<td class="message">Task Log inserted</td>' in response.read():
            raise DotProjectBot.LogFail('Something seems to be wrong. Please check %s' % url)
        else:
            msg = u"«%s (%s hs)» was logged succesfully" % (description, str(hours))
            logging.info(msg)
        

        


