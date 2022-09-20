---
permalink: /visualisations/
title: "Inside the taxonomy: visualisations"
toc: true
author_profile: false
layout: single_wide
toc_sticky: true
---

* Intro statement: on this page you can dynamically view our survey existing generalisation (with [link to explanations on the taxonomy page](/taxonomy) + survey)
* Some information about how you can contribute to the survey data, what the requirements are, and when the last paper was added (?), and how many papers are currently surveyed.
* The possibility to visualise the data in different ways, using click and play plotting possibilities
* Some indication for people that want to use plots generated on our website (we want them to!)
* [A link to a page with the full list of papers, including how they are characterised](/bibliography) (also there it might be nice if we have some options for listing them differently, e.g.: give me all papers that fall in this specific category in the taxonomy).

## 1. Taxonomy overview

{% include interactive_figures/sankey.html %}


{% include interactive_figures/chord_diagram.html %}

## 2. Individual axes analysed over tasks and time

### 2.1 The motivation axis
{% include interactive_figures/tasks_barplot_motivation.html %}
{% include interactive_figures/over_time_motivation.html %}

###  2.2 The type axis
{% include interactive_figures/tasks_barplot_type.html %}
{% include interactive_figures/over_time_type.html %}

###  2.3 The data shift axis
{% include interactive_figures/tasks_barplot_data_shift.html %}
{% include interactive_figures/over_time_data_shift.html %}

###  2.4 The shift's locus axis
{% include interactive_figures/tasks_barplot_shift_locus.html %}
{% include interactive_figures/over_time_shift_locus.html %}

###  2.5 The shift's source axis
{% include interactive_figures/tasks_barplot_shift_source.html %}
{% include interactive_figures/over_time_shift_source.html %}

## 3. Relations between axes
{% include interactive_figures/heatmap_data_shift.html %}
{% include interactive_figures/heatmap_type.html %}
