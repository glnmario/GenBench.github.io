---
permalink: /visualisations/
title: "Inside the taxonomy: visualisations"
toc: true
author_profile: false
layout: single_wide
toc_sticky: true
---

On this page you can view the results of our survey, in which more than 600 *ACL papers were annotated according to our [taxonomy](/taxonomy).
If you would like to contribute annotations for your paper or papers you think are missing, please [contribute](/contribute).

Are you writing a paper about generalisation in NLP? We would happily provide you with visualisations through the interactive graphs listed on this page.
If you hover over the graphs, you can click on the 📸 (camera) or 💾 (save) icons to download them in `.png` format, or you can contact us for custom adaptations of these graphs (email us at [genbench@gmail.com](genbench@mgail.com)).

```
@article{hupkes2022taxonomy,
  title={State-of-the-art generalisation research in NLP: a taxonomy and review},
  author={Hupkes, Dieuwke, and Giulianelli, Mario and Dankers, Verna and Artetxe, Mikel and Pimentel, Tiago et al.},
  year={2022}
}
```

## 1. Taxonomy overview

The taxonomy characterises research according to five axes. The Sankey diagram below illustrates the main relations between the axes that are most closely related, while illustrating the frequency of labels per class.
Some examples of conclusions that can be drawn are:
- the most frequent motivation for generalisation research is 'practical', but practically motivated studies can still take on any type;
- generalisation research introducing a covariate data shift mostly focuses on the difference between train (or fine-tune) and test data;
- structural generalisation experiments are mostly motivated from a cognitive perspective, and are never about fairness;
- fully generated data shfits tend to be used to create shifts between the train and test data.

{% include interactive_figures/sankey.html %}

If you would like to investigate the relations between all axes, take a look at the Chord diagram below. For readability purposes, we only illustrate connections that occurred more than 50 times.
Each axis has its own colour scheme, and the node labels indicate both the axis's name and the labels within that axis.
If you hover over a node or click on that node, the diagram highlights the connections to other nodes.
Some examples of conclusions that can be drawn are:
- ...
- ...
- ...

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
