#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import cookielib


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


