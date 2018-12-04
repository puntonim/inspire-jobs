from django.contrib import admin

from .models import inspirehep


admin.site.register(inspirehep.LegacyRecordsMirror)
