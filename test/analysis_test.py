import unittest

from . import ci
from . import ti


class AnalysisTest(unittest.TestCase):

    def test_add_analysis(self):

        name = "analysis x"
        program = "Magic"
        programversion = "1.0"
        algorithm = "mind"
        sourcename = "src"
        sourceversion = "2.1beta"
        sourceuri = "http://example.org/"
        description = "Bla bla bla"
        date_executed = "2018-02-03"

        ana = self.ti.analysis.add_analysis(name=name, program=program, programversion=programversion, algorithm=algorithm, sourcename=sourcename, sourceversion=sourceversion, sourceuri=sourceuri, description=description, date_executed=date_executed)

        assert int(ana["nid"]) > 0, "ana properly created"

        ana = self.ti.analysis.get_analyses(name=name)[0]

        assert ana["name"] == name, "analysis chado record properly created"
        assert ana["program"] == program, "analysis chado record properly created"
        assert ana["programversion"] == programversion, "analysis chado record properly created"
        assert ana["algorithm"] == algorithm, "analysis chado record properly created"
        assert ana["sourcename"] == sourcename, "analysis chado record properly created"
        assert ana["sourceversion"] == sourceversion, "analysis chado record properly created"
        assert ana["sourceuri"] == sourceuri, "analysis chado record properly created"
        assert ana["description"] == description, "analysis chado record properly created"
        assert ana["timeexecuted"] == '2018-02-03 00:00:00', "analysis chado record properly created"

        ana = self.ti.analysis.get_analyses_tripal()

        assert len(ana) > 0, "ana node/entity properly created"

        found_an = False
        for an in ana:
            if an['title'] == name:
                found_an = True

        assert found_an, "ana node/entity properly created"

    def test_sync_analysis(self):

        name = "analysis x"
        program = "Magic"
        programversion = "1.0"
        algorithm = "mind"
        sourcename = "src"
        sourceversion = "2.1beta"
        sourceuri = "http://example.org/"
        description = "Bla bla bla"
        date_executed = "2018-02-03"

        ana = self.ci.analysis.add_analysis(name=name, program=program, programversion=programversion, algorithm=algorithm, sourcename=sourcename, sourceversion=sourceversion, sourceuri=sourceuri, description=description, date_executed=date_executed)

        assert ana["analysis_id"] > 0, "ana properly created"

        ana = self.ti.analysis.get_analyses(name=name)[0]

        ana_chado_id = ana['analysis_id']

        assert ana["name"] == name, "analysis chado record properly created"
        assert ana["program"] == program, "analysis chado record properly created"
        assert ana["programversion"] == programversion, "analysis chado record properly created"
        assert ana["algorithm"] == algorithm, "analysis chado record properly created"
        assert ana["sourcename"] == sourcename, "analysis chado record properly created"
        assert ana["sourceversion"] == sourceversion, "analysis chado record properly created"
        assert ana["sourceuri"] == sourceuri, "analysis chado record properly created"
        assert ana["description"] == description, "analysis chado record properly created"
        assert ana["timeexecuted"] == '2018-02-03 00:00:00', "analysis chado record properly created"

        ana = self.ti.analysis.get_analyses_tripal()

        found_ana = False
        for ana in ana:
            if ana['title'] == '%s' % (name):
                found_ana = True

        assert found_ana is False, "ana not yet synced"

        org = self.ti.analysis.sync(analysis_id=ana_chado_id)

        org = self.ti.analysis.get_analyses_tripal()

        found_ana = False
        for org in org:
            if org['title'] == '%s' % (name):
                found_ana = True

        assert found_ana, "ana properly synced"

    def setUp(self):
        self.ci = ci
        self.ti = ti

        self.ci.analysis.delete_analyses()

        self.ci.session.commit()

    def tearDown(self):
        self.ci.analysis.delete_analyses()
        self.ti.analysis.delete_orphans()

        self.ci.session.commit()
