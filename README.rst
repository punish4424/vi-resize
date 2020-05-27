===============================
vi-resize website
===============================
Requirements
------------

* Django 2.1+
* Python 3.6


Installation
----------------------------

#. Clone the git repository.

#. Install all third party packages by running::

    $ pip install -r requirements.txt

#. Apply migrations::

    $ python manage.py migrate

#. To upload a story/ get all stories you need to run the url mentioned below::

    $ {{domain}}/story

#. To resize a file use the below mentioned url::

    $ {{domain}}/resize

#. You can download the reformatted video using this url::

    $ {{domain}}/media/{{file_name}}


