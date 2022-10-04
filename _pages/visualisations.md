---
permalink: /visualisations/
title: "Inside the taxonomy: visualisations"
toc: true
author_profile: false
layout: single_wide
toc_sticky: true
markdown: kramdown
---

On this page you can view the results of our review, which contains [taxonomy](/taxonomy) annotations of more than 600 *ACL papers.
If you would like to contribute annotations for your paper or (new) papers you think are missing, please [contribute](/contribute).
You can view the entries considered for our review on our [references](page).
If you are curious about *our* conclusions based on these results, have a look at the results section of our [paper](paper)!

## In need of visualisations for your paper?
Are you writing a paper about generalisation in NLP and would you like to motivate your work with some graphics?
We would happily provide you with visualisations through the interactive graphs listed on this page.
If you hover over the graphs, you can click on the 📸 (camera) or 💾 (save) icons to download them in `.png` format, or you can contact us for custom adaptations of these graphs (email us at [genbench@gmail.com](genbench@mgail.com)).

```
@article{hupkes2022taxonomy,
  title={State-of-the-art generalisation research in NLP: a taxonomy and review},
  author={Hupkes, Dieuwke, and Giulianelli, Mario and Dankers, Verna and Artetxe, Mikel and Pimentel, Tiago et al.},
  year={2022}
}
```

## Explore visualisations

###  Taxonomy overview

We provide two interactive plots that provide an overview of all five axes at the same time.

#### Sankey diagram
The taxonomy characterises research according to five axes. The Sankey diagram below illustrates the main relations between the axes that are most closely related, while illustrating the frequency of labels per class.
You can see, for instance, that:
- the most frequent motivation for generalisation research is 'practical', but practically motivated studies can still take on any type;
- generalisation research introducing a covariate data shift mostly focuses on the difference between train (or fine-tune) and test data;
- structural generalisation experiments are mostly motivated from a cognitive perspective, and are never about fairness;
- fully generated data shfits tend to be used to create shifts between the train and test data.

{% include interactive_figures/sankey.html %}

#### Chord diagram

If you would like to investigate the relations between all axes, take a look at the Chord diagram below. For readability purposes, we only illustrate connections that occurred more than 50 times.
Each axis has its own colour scheme, and the node labels indicate both the axis's name and the labels within that axis.
If you hover over a node or click on that node, the diagram highlights the connections to other nodes.

{% include interactive_figures/chord_diagram.html %}

### Individual axes over time

Plot the development of individual axes over time.

NB: goal is to include check-boxes like on the citation page, so that different plots can be 'generated' by the reader.

<div>
  <iframe id="barplot_time_outer" style="height:600px;width:100%;border:none" scrolling=no frameborder="0" src="/visualisations/barplot_time.html"></iframe>
</div>


### Individual axes over tasks

NB: this probably should be cleaned up first, do we already want to include it?

{% include interactive_figures/tasks_barplot_motivation.html %}

### Relations between axes in a heatmap

Generate heatmaps to explore the relationships between different axes.

NB: would rather have that there is just one here, and could we also add boxes that allow different normalisations?


<div>
  <iframe id="heatmap_outer" style="height:750px;width:100%;border:none" scrolling=no frameborder="0" src="/visualisations/heatmap.html"></iframe>
</div>
