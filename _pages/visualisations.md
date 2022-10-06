---
permalink: /visualisations/
title: "Inside the taxonomy: visualisations"
excerpt: "Explore generalisation research in NLP visually"
toc: true
author_profile: false
layout: single_wide
toc_sticky: true
markdown: kramdown
header:
  <!-- overlay_image: /assets/images/unsplash-image-1.jpg -->
  overlay_color: "#268"

---

<!-- Load plotly.js into the DOM -->
<script src='https://cdn.plot.ly/plotly-2.11.1.min.js'></script>
<script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>


On this page you can view the results of our review, which contains [taxonomy](/taxonomy) annotations of more than 600 \*ACL papers.
If you would like to contribute annotations for your paper or (new) papers you think are missing, please [contribute](/contribute).
You can view the entries considered for our review on our [references](page).
If you are curious about our conclusions based on these results, have a look at the results section of our [paper](../taxonomy_paper.pdf)!

## In need of visualisations for your paper?
Are you writing a paper about generalisation in NLP and would you like to motivate your work with some graphics?
We would happily provide you with visualisations through the interactive graphs listed on this page.
If you hover over the graphs, you can click on the 📸 (camera) or 💾 (save) icons to download them in `.png` format, or you can contact us for custom adaptations of these graphs (send us a message via twitter).

```
@article{hupkes2022taxonomy,
  title={State-of-the-art generalisation research in NLP: a taxonomy and review},
  author={Hupkes, Dieuwke, and Giulianelli, Mario and Dankers, Verna and Artetxe, Mikel and Pimentel, Tiago et al.},
  year={2022}
}
```
[Download bib entry](../hupkes2022taxonomy.bib)

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

NB: this plot renders best on relatively wide screens


<script type="module">
import sankeyData from '../plot_data/sankey.json' assert {type: "json" };


Plotly.newPlot('sankey', sankeyData.data, sankeyData.layout, {responsive: true} );
</script>

<div id='sankey'><!-- Plotly chart will be drawn inside this DIV --></div>

#### Chord diagram

If you would like to investigate the relations between all axes, take a look at the Chord diagram below. For readability purposes, we only illustrate connections that occurred more than 50 times.
Each axis has its own colour scheme, and the node labels indicate both the axis's name and the labels within that axis.
If you hover over a node or click on that node, the diagram highlights the connections to other nodes.


<div align="center">
  <iframe id="chord_diagram" style="display:block;height:max(900px,80vh);width:70%;border:none" scrolling=no frameborder="0" src="/visualisations/interactive_figures/chord_diagram.html"></iframe>
</div>

### Individual axes over time

Visualise how distribution over the axes values changes over time.
Use the radio buttons to indicate which axis you would like to view, and to choose how to normalise your plot.

<div>
  <iframe id="barplot_time_outer" style="height:750px;width:100%;border:none" scrolling=no frameborder="0" src="/visualisations/barplot_time.html"></iframe>
</div>


### Individual axes over tasks

Here, you can visualise how the different axes values are distributed over different tasks.
Use the radio buttons to indicate which taxonomy axis you would like to view, click on the tasks to remove them from the plot.


<div id="portrait">
  <iframe id="barplot_tasks_outer" style="height:60vh;width:100%;border:no;" scrolling=no frameborder="0" src="/visualisations/tasks_barplot.html"></iframe>
</div>

### Relations between axes in a heatmap

Generate heatmaps of the relations between the different axes.
Use the radio buttons to indicate which axis you would like on the x- and y-axis, and choose how to normalise your plot.

<div>
  <iframe id="heatmap_outer" style="height:750px;width:100%;border:none" scrolling=no frameborder="0" src="/visualisations/heatmap.html"></iframe>
</div>
