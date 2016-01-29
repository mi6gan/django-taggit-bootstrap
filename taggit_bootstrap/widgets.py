from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt
from django.utils.encoding import force_text

from taggit.utils import parse_tags, edit_string_for_tags
from django.utils import six

class TagsInput(forms.TextInput):
	class Media:
        	css = { 'all': ('css/bootstrap-tagsinput.css','css/typeahead.css') }
	        js = ('js/typeahead.jquery.min.js', 'js/bootstrap-tagsinput.min.js')

	def render(self, name, value, attrs={}):
		if value is not None and not isinstance(value, six.string_types):
			value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
		final_attrs = self.build_attrs(attrs, name=name)
		return mark_safe(render_to_string('taggit_bootstrap/widget.html', {
				'final_attrs': flatatt(final_attrs),
				'value': value if value else '',
				'id': final_attrs['id']
		}))
