from django.db import models 
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

STAGE0 = '0'
STAGE1 = '1'
STAGE2 = '2'
STAGE3 = '3'
STAGE3a = '3a'
STAGE3b = '3b'
STAGE3c = '3c'
STAGE4 = '4'
STAGES = (
    (STAGE1, 'I'),
    (STAGE2, 'II'),
    (STAGE3, 'III'),
    (STAGE3, 'III A'),
    (STAGE3, 'III B'),
    (STAGE3, 'III C'),
    (STAGE4, 'IV'),
    )
MSISTATUS = (
    ("MSS", 'MSS'),
    ("MSIH", 'MSI-H'),
    )
NED = (
    ("YES", 'Yep'),
    ("NO", 'Nope'),
    )

class BiomarkersLookUp(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)  

class Treatment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    description = models.TextField(max_length=255)
    trial_id = models.CharField(max_length=100)
    dose_schedule = models.TextField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    last_treatment_date = models.DateField(blank=True, null=True)
    response = models.TextField(max_length=255)
    treatment_notes = models.TextField(max_length=255)
    side_effect = models.TextField(max_length=255)

    def __str__(self):
        return self.desciption

    class Meta:
        ordering = ('start_date',) 

class Patient(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    dx_date = models.DateField(blank=True, null=True)
    last_treatment_date = models.DateField(blank=True, null=True)
    ned = models.CharField(
        max_length=20,
        choices=NED,
        default="YES",
    )
    stage_now = models.CharField(
        max_length=20,
        choices=STAGES,
        default=STAGE1,
    )
    stage_at_dx = models.CharField(
        max_length=20,
        choices=STAGES,
        default=STAGE1,
    )
    msi_status = models.CharField(
        max_length=20,
        choices=MSISTATUS,
        default="MSS",
    )

    biomarkers = models.ManyToManyField(BiomarkersLookUp)
   
    class Meta:
        managed = True
        db_table = 'patient'

@receiver(post_save, sender=User)
def create_or_update_user_patient(sender, instance, created, **kwargs):
    if created:
        Patient.objects.create(user=instance)
    instance.patient.save()

@receiver(post_save, sender=User)
def save_user_patient(sender, instance, **kwargs):
    instance.patient.save()

class Hospital(models.Model):
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='Zip', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=20, blank=True, null=True)  # Field name made lowercase.
    field_colontown_patients = models.CharField(db_column='# ColonTown Patients', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    guestimated_of_hai_implants_per_year = models.CharField(db_column='Guestimated # of HAI Implants per year', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ct_contacts = models.CharField(db_column='CT Contacts', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    longitude = models.CharField(db_column='Longitude', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    latitude = models.CharField(db_column='Latitude', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
   
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        db_table = 'hospital'
