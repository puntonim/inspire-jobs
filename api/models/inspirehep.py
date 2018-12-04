from django.db import models


class LegacyRecordsMirror(models.Model):
    recid = models.IntegerField(primary_key=True)
    last_updated = models.DateTimeField()
    marcxml = models.BinaryField()
    valid = models.BooleanField(blank=True, null=True)
    errors = models.TextField(blank=True, null=True)
    collection = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legacy_records_mirror'
