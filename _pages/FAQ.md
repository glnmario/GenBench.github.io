---
permalink: /FAQ/
title: "Frequently Asked Annotation Questions"
layout: single_wide
toc: true
toc_sticky: true

excerpt: "Making generalisation testing the new status-quo in NLP"
header:
  <!-- overlay_image: /assets/images/unsplash-image-1.jpg -->
  overlay_color: "#268"
---

NB: work in progress

## Questions about the motivation

**Should I submit a paper two times if I think it has two motivations?**

_Answer_

## Questions about the generalisation type

**What if a paper is unclear about its generalisation type?**
_Answer_

## Questions about the shift type

**Does using masked language modeling as the pretraining objective imply that there is a covariate shift from pretraining to finetuning, given that all pretraining inputs contain special masked tokens and finetuning inputs do not?**

_Answer_

**Even when leaving masking aside, isn't there always a covariate shift between pretraining and finetuning? The opposite would imply that random samples from the pretraining corpus would be indistinguishable from those from the downstream task. Even if there is data leakage this will never be the case in practice, as the leaked data will be mixed with other content in the pretraining corpus and their distribution will therefore not be strictly the same.**

_Answer_

**If no new parameters are added for finetuning, does that imply that there is no label shift? How should we annotate T5 and similar approaches?**
_Answer_

## Questions about the data source

## Questions about the shift locus

**When a pretrained language model is evaluated on language modeling itself, is the locus pretrain-test or train-test?**
_Answer_

## Other questions

**What if a paper has multiple experiments that have different values on the axes?**
_Answer_

**Why do you also ask to annotate the task that the paper is looking at?**
_Answer_

**Should I submit a paper two times if there are multiple tasks?**
_Answer_
