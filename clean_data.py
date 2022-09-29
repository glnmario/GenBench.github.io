import pandas as pd
import csv
import numpy as np
import re

class TaxonomyData:
    # columns that we will use
    AXES = ["type", "motivation",  "shift locus", "data shift", "shift source", "year"]
    META = ["tag", "title", "Website"]

    REMAP_DICT = {'natural data splits': 'artificially partitioned natural data',
         'naturally occurring shifts': 'natural shifts',
         'all': 'multiple loci',
         'double': 'multiple shifts',
         'data shift': 'shift',
         'shift locus': 'locus',
         'shift source': 'source',
         'fully generated': 'fully generated data',
         'all': 'multiple',
         'double': 'multiple'
        }

    def __init__(self, raw_data_path):
        self.data = self.read_data(raw_data_path)

    def clean_data(self, remap_dict=REMAP_DICT, write='taxonomy_clean.tsv'):
        # I included this function just so that the data is clean,
        # not because it needs to be included for the page, I will
        # run it before uploading things. The data that I have sent you
        # should be clean, but I kept the function because I'll
        # will need to run it myself again whenever I update the data

        keep=self.META+self.AXES

        # get indices of axes
        index_dict = {col_title: index for index, col_title in enumerate(self.data[0]) if col_title in keep}
        keep_indices = [index for index, col_title in enumerate(self.data[0]) if col_title in keep]

        cleaned_data = []
        for line in self.data:
            cleaned_line = [line[i] for i in keep_indices if line[i] != '']
            # ensure that line contains all data
            if len(cleaned_line) == len(keep_indices):
                remapped_line = [remap_dict.get(val, val) for val in cleaned_line]
                cleaned_data.append(remapped_line)

        # write to file
        out_file = open(write, 'w')
        for line in cleaned_data:
            out_file.write('\t'.join(line)+'\n')
        out_file.close()

        self.data = cleaned_data

        return

    def read_data(self, data_path):
        raw_data = csv.reader(open(data_path, "r"), delimiter="\t")
        lines = []
        for line in raw_data:
            lines.append(line)
        return lines

    def query(self):
        # simple mock-up, ideally these would be prefilled menues where you can fill in things,
        # or something like that
        user_input = {}

        # NB capped to the first two now for simplicity
        # for axis in self.AXES[:3]:
        for axis in ['motivation', 'type', 'data shift', 'shift source']:
            user_input[axis] = input(self.get_query_question(axis))

        # clean up by removing entries that are 'any'
        # NB: I am assuming here that the user input is correct,
        # this should be ensured somewhere.
        # Ideally users wouldn't be able to type anything that is
        # wrong but I don't want to implement that loop now as I
        # don't think it is interesting for understanding the logic
        cleaned_user_input = {axis: value for axis, value in user_input.items() if value != 'any' and value != ''}

        return cleaned_user_input

    def get_query_question(self, axes):

        if axes == 'motivation':
            query_string = "Which motivation? (choose from 'practical', 'cognitive', 'intrinsic', 'fairness', 'any') "
        elif axes == 'type':
            query_string = "Which type? (choose from: 'compositional', 'structural', 'robustness', 'across domain', 'across task', 'across language', 'any') "
        elif axes == 'data shift':
            query_string = "Which shift occurs? (choose from: 'covariate', 'label', 'full', 'double', 'assumed', 'any'): "
        elif axes == 'shift source':
            query_string = "Which shift source? (choose from: 'naturally occurring shifts', 'natural data splits', 'generated shifts', 'fully generated', 'any') "
        else:
            # Wouldn't need all in a mockup, can extend myself
            query_string = ""

        return query_string

    def fetch_entries(self, user_input):

        # generate new index dict and set as attribute
        index_dict = {col_title: index for index, col_title in enumerate(self.data[0])}

        fetched_entries = []
        # fetch relevant column indices
        for line in self.data[1:]:
            keep=True
            for axis, value in user_input.items():
                if line[index_dict[axis]] != value:
                    # print(line[index_dict[axis]], value)
                    keep=False
            if keep:
                fetched_entries.append(line)
        return fetched_entries, index_dict

    def print_entries(self, entries, index_dict, reorder=None):
        # I am actually not 100% sure how I want to print this
        # If I'd go full-on python I might put the line in 
        # a separate class to make sure I have different options
        for line in entries: 
            print(line[index_dict["title"]]+f' Annotators:   \
                {line[index_dict["Annotator 1"]]} {line[index_dict["Annotator 2"]]}'+'\n')


if __name__ == '__main__':
    taxonomy_data = TaxonomyData('taxonomy.tsv')
    taxonomy_data.clean_data()


