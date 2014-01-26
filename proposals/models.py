from django.db import models
import datetime


class Proposal(models.Model):
    bg_name = models.CharField('BG name (required)',max_length=200) # intended to mimic name on trac: e.g. '13bg_NSF'
    trac_dir = models.URLField('Repo URL',blank=True) # link to directory on trac where proposal is edited

    proposal_title = models.CharField('Title',max_length=200,blank=True) # full name of proposal

    source_url = models.URLField('URL',max_length=200,blank=True) # intended to point to call for proposals
    source_file = models.FileField('file',upload_to='calls_for_proposals',null=True,blank=True)

    due_date = models.DateTimeField('deadline for submission',null=True,blank=True)
    submission_date = models.DateTimeField('date submitted',null=True,blank=True)

    proposal_file = models.FileField(upload_to='proposals',blank=True) # local copy of proposal

    funds_requested = models.IntegerField('Requested',null=True,blank=True)
    funds_awarded = models.IntegerField('Awarded',null=True,blank=True)

    notes = models.TextField(blank=True) # A place to put notes if needed

    def __unicode__(self):
        return self.bg_name


# STATUS STUFF
class Status(models.Model):
    proposal = models.ForeignKey(Proposal)
    # Application Status
    IN_PREPARATION = 'InPrep'
    SUBMITTED = 'Submtd'
    APPROVED = 'Apprvd'
    REJECTED = 'Rejctd'
    APPLICATION_STATUS_CHOICES = (
        (IN_PREPARATION, 'In-preparation'),
        (SUBMITTED, 'Submitted'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
        )
    application_status = models.CharField(max_length=6,verbose_name='Application Status',
                                       choices=APPLICATION_STATUS_CHOICES,
                                       default=IN_PREPARATION)
    # Historical Status
    CURRENT = 'Crnt'
    PAST = 'Past'
    HISTORICAL_STATUS_CHOICES = (
        (CURRENT, 'Current'),
        (PAST, 'Past'),
        )
    historical_status = models.CharField(max_length=4,verbose_name='Past or Current?',
                                     choices=HISTORICAL_STATUS_CHOICES,
                                     default=CURRENT)
    def __unicode__(self):
        return u'%s %s' % (self.application_status, self.historical_status)

# PI AND CO-PI STUFF
class PI(models.Model):
    proposal = models.ForeignKey(Proposal)
    PI_first_name = models.CharField('First Name',max_length=30)
    PI_last_name = models.CharField('Last Name',max_length=40)
    PI_email = models.EmailField('email',blank=True)
    def __unicode__(self):
        return u'%s %s' % (self.PI_first_name, self.PI_last_name)

class CoPI(models.Model):
    proposal = models.ForeignKey(Proposal)
    CoPI_first_name = models.CharField('First Name',max_length=30)
    CoPI_last_name = models.CharField('Last Name',max_length=40)
    CoPI_email = models.EmailField('email',blank=True)
    def __unicode__(self):
        return u'%s %s' % (self.CoPI_first_name, self.CoPI_last_name)

class Reference(models.Model):
    proposal = models.ForeignKey(Proposal)
    Reference_first_name = models.CharField('First Name',max_length=30)
    Reference_last_name = models.CharField('Last Name',max_length=40)
    Reference_email = models.EmailField('email',blank=True)
    Reference_letter = models.FileField('letter',upload_to='reference_letters',blank=True) # local copy of reference letter
    def __unicode__(self):
        return u'%s %s' % (self.Reference_first_name, self.Reference_last_name)
