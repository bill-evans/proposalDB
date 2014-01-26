from django.contrib import admin
from proposals.models import Proposal, Status, PI, CoPI, Reference
# Register your models here.


class PIInline(admin.TabularInline):
    model = PI
    max_num = 1
    verbose_name_plural = ('Principle Investigator')
    can_delete = False

class CoPIInline(admin.TabularInline):
    model = CoPI
    extra = 1
    verbose_name = ('Co-Principle Investigator')
    verbose_name_plural = ('Co-Principle Investigators')

class ReferenceInline(admin.TabularInline):
    model = Reference
    extra = 1

class StatusInline(admin.TabularInline):
    model = Status
    extra = 1
    max_num = 1
    verbose_name_plural = ('Status')
    can_delete = False

class ProposalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['bg_name','proposal_title','trac_dir']}),
        ('Call for Proposal', {'fields': ['source_url', 'source_file']}),
        ('Date information', {'fields': [('due_date', 'submission_date')]}),
        ('Funding (in thousands of dollars)', {'fields': [('funds_requested', 'funds_awarded')]}),
        (None, {'fields': ['proposal_file','notes']}),
    ]
    inlines = [PIInline,CoPIInline,ReferenceInline,StatusInline]
    list_display = ('bg_name','proposal_title','funds_awarded', 'funds_requested')
    search_fields = ['proposal_title']
    date_hierarchy = 'due_date'


admin.site.register(Proposal,ProposalAdmin)
