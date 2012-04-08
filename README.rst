h2dp: Hamster to dotProject logs sync tool
------------------------------------------

This tool aims to save your time posting your Hamster_ facts as dotProject_
task logs in an automatic way.

.. _Hamster: http://projecthamster.wordpress.com/
.. _dotProject: http://dotproject.net/


Install
-------

You can install it using pip::

    $ sudo pip install git+git://github.com/nqnwebs/h2dp

Usage
-----

Configure ``~/.h2dp/local_settings.py``. You can use the provided
``local_settings.py.template`` as a template.

Then run the script::

    $ h2dp


How it works
-------------

Setting a dictionary in ``.h2dp/local_settings.py`` , you map each *syncable*
hamster's category to a dotproject's site task_id. For example::

    HAMSTER_TO_DP = {'iteration22': 386, 'project-X': 387}

Then, a hamster fact like  *"#453@iteration22, modeling blah"*, will be posted
into  *https://YOUR_DOT_PROJECT/index.php?m=tasks&a=view&task_id=386 *
with the description *"#453 modeling blah"*. 

Strictly the description format is::
    
    category [tag1[, tag2, ...]:][description] 

.. tip::

    Note you can add tags to your hamster log. For example *"#453@iteration22, blah"* 
    and tagged with *testing* will be posted as *#453 testing: blah*

After sync, each fact posted is marked with a tag (*"_logged_in_dp_"*) to
be ommited the next time.

.. attention::

    Only hamster's facts that are keys in ``HAMSTER_TO_DP`` will be
    logged into dotproject,  so DO NOT forget to mark your task with
    *@category* and update this dictionary when need it.

TODO
----
- Check/edit/update already posted logs
- Tests

