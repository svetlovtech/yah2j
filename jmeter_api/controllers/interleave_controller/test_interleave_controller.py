from jmeter_api.controllers.random_controller.elements import InterleaveController
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest


class TestInterleaveController:
    class TestIgnoreSubControllers:
        def test_check(self):
            with pytest.raises(TypeError):
                InterleaveController(ignoreSubControllers = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                InterleaveController(ignoreSubControllers = 1)

        def test_positive(self):
            InterleaveController(ignoreSubControllers = True)           


    class TestAccrossThreads:
        def test_check(self):
            with pytest.raises(TypeError):
                InterleaveController(accrossThreads = "True")

        def test_check2(self):
            with pytest.raises(TypeError):
                InterleaveController(accrossThreads = 1)

        def test_positive(self):
            InterleaveController(accrossThreads = True)

class TestInterleaveControllerRender:
    def test_ignore_sub_controllers(self):
        element = InterleaveController(ignoreSubControllers = True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['InterleaveControll']['intProp']['#text'] == '0'

    def test_accross_threads(self):
        element = InterleaveController(accrossThreads = True)
        rendered_doc = element.to_xml()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['InterleaveControll']['boolProp']['#text'] == 'true'