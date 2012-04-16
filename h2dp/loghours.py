import logging

from peewee import Q

import settings
from models import Fact, Tag, FactTag
from browser import DotProjectBot



def log_hours():
    logging.basicConfig(level=logging.INFO)
    
    categories = settings.HAMSTER_TO_DP.keys()
    tag_logged = Tag.get_or_create(name = '_logged_in_dp_')
    assert tag_logged.id == 7

    already_tagged = [ft.fact.id for ft in FactTag.filter(tag=tag_logged).distinct()]
    

    #get all facts that belong to exportable categories, finished, and
    # not previously posted
    facts = Fact.filter(
                Q(activity__category__name__in=categories) & 
                ~Q(end_time__is=None) &
              # ~Q(fact_tags_set__tag=tag_logged)     # * see note
                ~Q(id__in=already_tagged)
            )

    # NOTE
    # I want to exclude Facts tagged with ``tag_logged``, . but that ~Q() condition
    # only exclude the facts that are ONLY tagged with ``tag_logged``.
    
    # the last Q is a workaround but imply a nested select.
    # How I should write this query?

    if not facts.exists():
        logging.info("You're up to date! There is no unsynced tasks")
        return
        

    br = DotProjectBot(settings.DP_BASE_URL)
    br.login(settings.DP_USERNAME, settings.DP_PASSWORD)


    for f in facts:
        #process data
        tags = ', '.join([ft.tag.name for ft in f.fact_tags_set])

        if tags and f.description:
            description = '%s %s: %s' % (f.activity.name, tags, f.description)
        elif tags:
            description = '%s %s' % (f.activity.name, tags)
        elif f.description:
            description = '%s %s' % (f.activity.name, f.description)
        else:
            description = f.activity.name

        dp_task_id = settings.HAMSTER_TO_DP[f.category.name]

        #and post the fact into dotproject!
        br.log_task(dp_task_id, f.start_time, f.duration, description)

        #then mark the fact as logged.
        ft = FactTag(fact=f, tag=tag_logged)
        ft.save()


if __name__ == '__main__':
	log_hours()
