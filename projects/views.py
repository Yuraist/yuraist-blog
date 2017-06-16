# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from projects.models import Project


class ProjectListView(ListView):
    model = Project
    queryset = Project.objects.order_by("-date_time")
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        return context
