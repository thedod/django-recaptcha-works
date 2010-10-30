# -*- coding: utf-8 -*-
#
#  This file is part of django-recaptcha-works.
#
#  django-recaptcha-works provides a Django form field that integrates the
#  reCaptcha service.
#
#  Based on the code snippet #1644 as published on:
#    - http://djangosnippets.org/snippets/1644/
#
#  Copyright (c) 2009-2010 Chris Beaven (SmileyChris), http://smileychris.com/
#  Copyright (c) 2010 George Notaras <gnot@g-loaded.eu>, http://www.g-loaded.eu/
#
#  Development Web Site:
#    - http://www.codetrax.org/projects/django-recaptcha-works
#
#  Public Source Code Repository:
#    - https://source.codetrax.org/hgroot/django-recaptcha-works
#
#  Licensed under the BSD License.
#
#  Redistribution and use in source and binary forms, with or without modification,
#  are permitted provided that the following conditions are met:
#
#      1. Redistributions of source code must retain the above copyright notice, 
#         this list of conditions and the following disclaimer.
#      
#      2. Redistributions in binary form must reproduce the above copyright 
#         notice, this list of conditions and the following disclaimer in the
#         documentation and/or other materials provided with the distribution.
#
#      3. Neither the name of Django nor the names of its contributors may be used
#         to endorse or promote products derived from this software without
#         specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#  ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

VERSION = (0, 2, 3, 'final', 0)

def get_version():
    version = '%d.%d.%d' % (VERSION[0], VERSION[1], VERSION[2])
    return version


long_description = """
*django-recaptcha-works* provides a Django form field that integrates the
reCaptcha service. It is released under the terms of the BSD License.

The app is based on the code `snippet 1644 <http://djangosnippets.org/snippets/1644/>`_
as published by *Chris Beaven* (aka SmileyChris).

The original code has been further modified by *George Notaras* in order to
implement the following:

- transform the snippet to a Django application release
- add SSL support for both the captcha presentation and the communication with the reCaptcha servers 
- migration to the Google-hosted reCaptcha API
- extension of the available application settings
- addition of a decorator that adds the remote IP to the submitted form

More information about the installation, configuration and usage of this app
can be found in the **README** file inside the distribution package or in the
project's `wiki <http://www.codetrax.org/projects/django-recaptcha-works/wiki>`_.

Spotted a bug or have a feature request? Feel free to file a report at the
project's `issue tracker <http://www.codetrax.org/projects/django-recaptcha-works/issues>`_.

"""
