import unittest  #  am importat toata libraria unittest
import HtmlTestRunner
from selenium_automation.intalnirea9.test4_unittest import Test
from selenium_automation.intalnirea9.test5_ex import Test2
from selenium_automation.intalnirea10.test3_alerts import Alerts
from selenium_automation.intalnirea10.test4_auth import Authentication
from selenium_automation.intalnirea10.test5_context_menu import ContextMenu
from selenium_automation.intalnirea10.test6_keys import Keyboard

class TestSuite(unittest.TestCase): # pentru ca am importat toata libraria este nevoie sa specificam in fata clasei TestCase
                                                         # libraria din care sa fie extrasa
                                        # Daca importam doar libraria, sistemul va avea doar adresa de identificare a librariei,
                                                         # nu si a clasei TestCase
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Test),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test2),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(smoke_test)