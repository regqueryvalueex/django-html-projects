#! -*- coding: utf-8 -*-
import os
from core.settings import base
from django.views.generic import TemplateView


class Template(TemplateView):
    def get_template_names(self):
        return ["%s.html" % self.kwargs['template']]

    def dispatch(self, request, project, template, *args, **kwargs):
        base.TEMPLATES[0]['DIRS'] = [
            os.path.join(base.WEBSITE_ROOT, 'projects', project, 'templates')
        ]
        base.STATICFILES_DIRS = [
            os.path.join(base.WEBSITE_ROOT, 'projects', project, 'static')
        ]

        return super(Template, self).dispatch(request, *args, **kwargs)

template = Template.as_view()
