from django.core.management.base import NoArgsCommand, CommandError
from django.db import settings 
from _dotproject import DotProjectBot
from hamster.models import Fact, Tag, FactTag
import logging


class Command(NoArgsCommand):
    help = "Syncs your hamster's logs into dotproject"

    def handle_noargs(self, **options):
        
        br = DotProjectBot(settings.DP_BASE_URL)
        br.login(settings.DP_USERNAME, settings.DP_PASSWORD)
        
        categories = settings.HAMSTER_TO_DP.keys()
        tag_logged, _ = Tag.objects.get_or_create(name = '_logged_in_dp_')
        facts = Fact.objects \
                    .exclude(tags=tag_logged) \
                    .exclude(end_time=None) \
                    .filter(activity__category__name__in=categories)
                    
        for f in facts:
            #process data
            tags = ', '.join([t.name for t in f.tags.exclude(id=tag_logged.id)])
            if tags:
                description = '%s %s: %s' % (f.activity.name, tags, f.description)
            else:
                description = '%s %s' % (f.activity.name, f.description)
            
            dp_task_id = settings.HAMSTER_TO_DP[f.category.name]

            #and post the fact into dotproject!
            br.log_task(dp_task_id, f.start_time, f.duration, description)
        
            #then mark the fact as logged. 
            FactTag.objects.create(fact=f, tag=tag_logged)
