#!/usr/bin/env python

from distutils.core import setup

setup(name='django-taggit-bootstrap',
      version='0.2',
      description='Django Taggit widget with autosuggestion support on top of Bootstrap 3',
      author='Michael Boyarov',
      author_email='mi666gan@gmail.com',
      url='https://github.com/mi6gan/django-taggit-bootstrap',
      packages=['taggit_bootstrap'],
      package_data={'taggit_bootstrap':["templates/taggit_bootstrap/*.html","static/css/*.css","static/js/*.js"]},
      requires=['django', 'django_taggit']
     )
