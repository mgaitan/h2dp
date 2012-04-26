#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from datetime import datetime, timedelta
from h2dp.loghours import log_hours

from h2dp import models
from h2dp.settings import MARK_TAG
from peewee import SqliteDatabase
import mock

HAMSTER_TO_DP_TEST = {'cat1': 10, 'cat2': 4}

class BaseTest(unittest.TestCase):
    def setUp(self):
        # use a memory based db for every model
        test_db = SqliteDatabase(':memory:')
        test_db.connect()
        for model_cls_name in models.__all__:
            model = getattr(models, model_cls_name)
            model._meta.database = test_db
            model.create_table()

        #override HAMSTER_TO_DP dictionary
        test_map = mock.patch.dict('h2dp.settings.HAMSTER_TO_DP',
                                   HAMSTER_TO_DP_TEST,
                                   clear=True)
        test_map.start()
        self.addCleanup(test_map.stop)

        self.mark = models.Tag.get_or_create(name=MARK_TAG)

    def create_fact(self, shortcut, start=None, end=None, tags=''):
        """
        shortcut : string `activity@category[, description]`
        tags: csv string `tag1, tag2, ...`

        """
        start = start or datetime.now()
        #parse things
        splitted = shortcut.split(',')
        if len(splitted) == 2:
            shortcut, description = splitted
        else:
            description = None
        activity, category = shortcut.split('@')
        tags = tags.split(', ')

        #create objects
        category = models.Category.get_or_create(name=category)
        activity = models.Activity.get_or_create(name=activity, category=category)
        tags = [models.Tag.get_or_create(name=t) for t in tags]
        fact = models.Fact.create(activity=activity,
                    description=description,
                    start_time=start,
                    end_time=end)
        return fact



class TestLog(BaseTest):

    def test_fact_posted_is_marked(self):
        now = datetime.now()
        later = datetime.now() + timedelta(minutes=15)
        f = self.create_fact('task@cat1', now, later)
        with mock.patch('h2dp.loghours.DotProjectBot') as dpb:
            log_hours()
        self.assertEqual(f.fact_tags_set.filter(tag=self.mark).count(), 1)
                
    def test_facts_are_not_re_posted(self):
        now = datetime.now()
        later = datetime.now() + timedelta(minutes=15)
        f = self.create_fact('task@cat1', now, later)
        with mock.patch('h2dp.loghours.DotProjectBot') as dpb::
            log_hours()
            log_hours()
        import ipdb;ipdb.set_trace()
        

    def test_nothing_happen_if_there_no_facts_to_post(self):
        pass

    def test_every_fact_in_categories_are_posted(self):
        pass

    def test_facts_not_finished_are_not_posted(self):
        pass

    def test_facts_belong_to_foreign_categories_are_not_posted(self):
        pass

    def test_posted_description_if_own_description(self):
        pass

    def test_posted_description_if_own_description_and_tags(self):
        pass

    def test_posted_description_if_only_tags(self):
        pass

    def test_duration_are_ok(self):
        pass

if __name__ == '__main__':
    unittest.main()
    

    
    
    
    

