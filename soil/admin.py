# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# username : admin
# password : meclabs123


admin.site.register(User)
admin.site.register(LandProfile)
