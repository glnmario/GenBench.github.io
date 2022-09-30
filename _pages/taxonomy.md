---
permalink: /taxonomy/
title: "A taxonomy to characterise generalisation research"
toc: true
author_profile: false
layout: single_wide
toc_sticky: true
---

The ability to generalise well is one of the primary desiderata of natural language processing, yet how 'good generalisation' should be defined and what it entails in practice is not well understood.
To be able to better talk about generalisation research in NLP, and identify what is needed to move towards a more sound and exhaustive approach to test generalisation, we present a (nominal) axes-based taxonomy along which research can be categorised.
Below the infographic, we describe the meaning of the different axes.
If you are interested in exploring the results of our taxonomy-based review of over 400 generalisation research papers, check our [generalisation map exploration](/visualisations) page, or <a href="references">search through the references</a>.
For a more detailed description of the taxonomy and the survey, have a look at [our paper]().

<br>

<center>
    <img src="/assets/images/taxonomy_infographic.png" alt="Infographic for the generalisation taxonomy">
</center>

<br>


## The taxonomy axes

The generalisation taxonomy contains five different (nominal) axes along which generalisation research can differ: their main <i>motivation</i>, the <i>type of generalisation</i> they aim to solve, the type of <i>data shift</i> they are considering, the <i>source</i> by which the datashift was obtained, and the <i>locus</i> of the shift.

###  Motivation
The motivation axis illustrates what kind of motivations are used in a generalisation test.
We distinguish four different types of motivations: the <i>practical</i> motivation, which characterises studies that evaluate generalisation to understand in which scenarios models can be applied, or with the concrete aim to improve them; the <i>cognitive</i> motivation, which includes papers that study generalisation from a cognitive angle, or because they would like to learn more about humans; the <i>intrinsic</i> motivation, which instead considers studies that look at generalisation purely from an intrinsic perspective, to better understand what kind of solutions a model implements or what factors impact that; and the <i>fairness and inclusivity</i> motivation, which is used for studies that are motivated from the idea that models should generalise fairly, for instance to different sub-demographics or low-resource languages.

### Generalisation type
The second axis describes the type of generalisation a study looks at.
On this axis, we consider five different types: <i>compositional generalisation</i>, which considers whether models can compositionally assign meanings to new inputs (or broader, compositionally map new inputs to outputs); <i>structural generalisation</i>, which includes studies that consider whether models can generalise to correct syntactic or morphological structures -- without considering whether those structures can also be correctly interpreted; <i>generalisation across tasks</i> and <i>generalisation across languages</i>, encompassing studies that consider whether a single model can generalise from one task or language to another, respectively; <i>generalisation across domain</i>, which considers whether models can generalise from one domain to another, considering a broad definition of `domain'; and <i>robustness generalisation</i> which considers how robustly models generalise when faced with different input distributions representing the same task.

### Data shift type
Axis three is statisticaly inspired and describes what data shift is considered in the generalisation test.
We consider three well-knows shifts from the literature: <i>covariate shifts</i> -- shifts in the input distribution only; <i>label shifts</i> -- shifts in the conditional probability of the output given the input; and <i>full shift</i>, which describes a shift in both input and conditional output distribution at the same time.
Because shifts can occur in multiple stages in the modelling pipeline -- as described in the next section -- we furthermore include the category <i>double shift</i>, used for cases where the experimental design investigates multiple shifts at the same time.
Lastly, we observed that several studies in the literature claim to investigate generalisation, but do not actually check the relationship between the different data distributions involved in their experiments.
For those kind of studies, we -- hopefully temporarily -- include the label <i>assumed shift</i> on our data shift type axis.

### Shift source
On axis four of our taxonomy, we consider what is the source of the data used in the experiment.
The source of the data shift determines how much control the experimenter has over the training and testing data and, consequently, what kind of conclusions can be drawn from an experiment.
We consider four different scenarios.
The first possibility is the scenario in which the train and test corpora mark <i>natural shifts</i>: they are naturally different corpora, that are not systematically adjusted in any way.
In the second scenario, instead, all data involved is natural, but the data is split along unnatural dimensions, we refer to this source with the term <i>natural data splits</i>.
Scenario three -- <i>generated shifts</i> encompasses the case in which the training corpus is a fully natural corpus, but the test corpus is (adversarially) generated -- or the other way around; the fourth and last option is used for studies that use data that is <i>fully generated</i>, for instance using templates or a grammar.

### Shift locus
The last axis of our taxonomy describes the where in the modelling pipeline generalisation is considered, or, in other words, what is the <b>locus</b> of the shift in the experiment.
Given the three broad stages in the contemporary modelling pipeline -- pretraining, training and testing -- we mark five different loci: the <i>train-test locus</i>, used for experiments that focus on the classical case where a model is trained on one distribution and tested on another; the <i>finetune train-test locus</i>, indicating experiments where a pretrained model is finetuned on some data and then tested on a dataset that is o.o.d.\ w.r.t. the finetuning data; the <i>pretrain-train locus</i>, which includes studies that consider shifts between pretraining and training data, but not between the finetuning and testing data; the <i>pretrain-test locus</i>, which we use to indicate papers that use a pretrained model that is not further finetuned but tested directly; and, lastly, <i>multiple loci</i>, which we use for studies where there are shifts between all stages of the modelling pipeline, and those are also all subject in the generalisation experiment.

## Contribute to the review

We would love to hear what you think about the taxonomy and include more papers in our review.
Did you also work on generalisation, and would you like to have your work included in our review and generalisation database?
Check instructions on the [contributions](/contributions) page.
