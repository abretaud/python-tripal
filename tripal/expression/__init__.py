from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from tripal.client import Client

logging.getLogger("requests").setLevel(logging.CRITICAL)
log = logging.getLogger()


class ExpressionClient(Client):
    """Manage Tripal expressions"""

    def add_expression(self, organism, analysis, match_type, file_path,
                       biomaterial_provider=None, array_design=None, assay_id=None,
                       acquisition_id=None, quantification_id=None, file_extension=None,
                       start_regex=None, stop_regex=None, use_column=False, no_wait=False):
        """
        :type organism: str
        :param organism: Organism Id

        :type analysis: str
        :param analysis: Id of the analysis

        :type match_type: str
        :param match_type: Match to features using either name or uniquename

        :type file_path: str
        :param file_path: Path to the expression file, or directory containing multiple expression files.

        :type biomaterial_provider: str
        :param biomaterial_provider: The contact who provided the biomaterial. (optional)

        :type array_design: str
        :param array_design: The array design associated with this analysis. This is not required if the experimental data was gathered from next generation sequencing methods. (optional)

        :type assay_id: str
        :param assay_id: The id of the assay associated with the experiment. (optional)

        :type acquisition_id: str
        :param acquisition_id: The id of the acquisition associated with the experiment (optional)

        :type quantification_id: str
        :param quantification_id: The id of the quantification associated with the experiment (optional)

        :type file_extension: str
        :param file_extension: File extension for the file(s) to be loaded into Chado. Do not include the ".". Not required for matrix files. (optional)

        :type start_regex: str
        :param start_regex: A regular expression to describe the line that occurs before the start of the expression data. If the file has no header, this is not needed. (optional)

        :type stop_regex: str
        :param stop_regex: A regular expression to describe the line that occurs after the end of the expression data. If the file has no footer text, this is not needed. (optional)

        :type use_column: bool
        :param use_matrix: Set to true if the expression file is a column

        :type no_wait: bool
        :param no_wait: Do not wait for job to complete

        :rtype: str
        :return: Loading information
        """

        if use_column:
            file_type = "col"
        else:
            file_type = "mat"

        if file_type == "col" and not file_extension:
            raise Exception("File_extension is required for column files")

        if match_type == "uniquename":
            match_type = "uniq"

        job_args = [organism, analysis, biomaterial_provider, array_design, assay_id, acquisition_id, quantification_id, file_path, file_extension, file_type, start_regex, stop_regex, match_type]

        r = self.tripal.job.add_job("Add Expression", 'tripal_analysis_expression', 'tripal_expression_loader', job_args)

        if 'job_id' not in r or not r['job_id']:
            raise Exception("Failed to create job, received %s" % r)

        if no_wait:
            return r
        else:
            return self._run_job_and_wait(r['job_id'])

    def add_biomaterial(self, organism_id, file_path, file_type, no_wait=False):
        """
        Add a new biomaterial to the database

        :type organism_id: str
        :param organism_id: The id of the associated organism

        :type file_path: str
        :param file_path: The path to the biomaterial file

        :type file_type: str
        :param file_type: The type of the biomaterial file (xml, tsv or csv)

        :rtype: dict
        :return: Job information
        """

        if file_type not in ['xml', 'tsv', 'csv']:
            raise Exception("File format must be one of ['xml', 'tsv', 'csv']")

        if file_type == "xml":
            job_args = [file_path, organism_id]
            callback = 'xml_biomaterial_parser'

        else:
            job_args = [file_path, organism_id, file_type]
            callback = 'flat_biomaterial_parser'

        r = self.tripal.job.add_job("Add Biomaterial", 'tripal_analysis_expression', callback, job_args)

        if 'job_id' not in r or not r['job_id']:
            raise Exception("Failed to create job, received %s" % r)

        if no_wait:
            return r
        else:
            return self._run_job_and_wait(r['job_id'])
