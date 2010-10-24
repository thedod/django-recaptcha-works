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

from recaptchaworks.fields import RecaptchaField


class BaseRecaptchaForm(forms.BaseForm):
    def __init__(self, remote_ip, *args, **kwargs):
        super(BaseRecaptchaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field, RecaptchaField):
                field.remote_ip = remote_ip


class RecaptchaForm(BaseRecaptchaForm, forms.Form):
    pass

