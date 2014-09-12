REVIEW
=======================
After hours of searching couldn't find any easy-in-use Django taggit solution with two main features:
1. Tag style input
2. Autosuggest support

The application includes Bootstrap Tags Input ( http://timschlechter.github.io/bootstrap-tagsinput/examples/ ) and typeahead.js ( http://twitter.github.io/typeahead.js/ ) jQuery plugins with some css fixes required for my projects. These plugins mainly supposed to be used with Bootstrap 3 Framework but I believe it applicable in other cases.


CONFIGURATION
=======================
1. Install and configure django-taggit with easy_install, pip or directly from https://github.com/alex/django-taggit .
2. Add taggit_bootstrap into your INSTALLED_APPS.
3. Add taggit_bootstrap.urls into your urls patterns. E.q.

urlpatterns = patterns('',
  ...  
  url(r'^taggit/',include('taggit_bootstrap.urls')),
)

4. Use TagsInput widget like this

import taggit_bootstrap
class TaggitTestForm(forms.Form):
        tags=TagField(widget=taggit_bootstrap.TagsInput)


TODO LIST
=======================
1. Fix some few annoying css issues.
2. Improve tags search.
3. Add few settings (don't know which ones, lol).
