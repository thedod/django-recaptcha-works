# -*- coding: utf-8 -*-
#
#  This file is part of django-recaptcha-works.
#
#  django-recaptcha-works is an easy-to-use Django forms integration of the
#  reCaptcha service.
#
#  Based on the code snippet #1644 as published on:
#    - http://djangosnippets.org/snippets/1644/
#
#  Copyright (c) 2009-2010 Chris Beaven (SmileyChris), http://smileychris.com/
#  Copyright (c) 2010 George Notaras <gnot@g-loaded.eu>, http://www.g-loaded.eu/
#
#  django-recaptcha-works is based on the code snippet #1644 as published on:
#    - http://djangosnippets.org/snippets/1644/
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

from django import forms
from django.utils.safestring import mark_safe

from recaptchaworks import settings


class RecaptchaWidget(forms.Widget):
    def __init__(self, theme=None, tabindex=None, public_key=None):
        '''
        From http://recaptcha.net/apidocs/captcha/client.html#look-n-feel:

            theme:      'red' | 'white' | 'blackglass' | 'clean'
    
                Defines which theme to use for reCAPTCHA.
    
            tabindex:   any integer
    
                Sets a tabindex for the reCAPTCHA text box. If other elements
                in the form use a tabindex, this should be set so that
                navigation is easier for the user.
            
        The optional ``public_key`` argument can be used to override the
        default use of the project-wide ``RECAPTCHA_PUBLIC_KEY`` setting.
        '''
        options = {}
        if theme:
            options['theme'] = theme
        if tabindex:
            options['tabindex'] = tabindex
        self.options = options
        self.public_key = public_key or settings.RECAPTCHA_PUBLIC_KEY
        super(RecaptchaWidget, self).__init__()

    def render(self, name, value, attrs=None):
        args = dict(public_key=self.public_key, options='')
        if self.options:
            args['options'] = settings.RECAPTCHA_OPTIONS_SCRIPT_HTML % self.options
        return mark_safe(settings.RECAPTCHA_HTML % args)

    def value_from_datadict(self, data, files, name):
        challenge = data.get('recaptcha_challenge_field')
        response = data.get('recaptcha_response_field')
        return (challenge, response)

    def id_for_label(self, id_):
        return None

