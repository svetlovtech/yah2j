from jmeter_api.timers.constant_throughput_timer.elements import ConstThroughputTimer, ConstThroughputTimerXML, BasedOn
from jmeter_api.basics.utils import tag_wrapper
import xmltodict
import pytest
import logging


class TestConstThroughputTimer:
    def test_args_type_check(self):
        # name type check
        with pytest.raises(TypeError, match=r".*arg: name must be str. name*"):
            ConstThroughputTimer(name=123)

        # comments type check
        with pytest.raises(TypeError, match=r".*arg: comments must be str. comments*"):
            ConstThroughputTimer(comments=123)

        # is_enabled type check
        with pytest.raises(TypeError, match=r".*arg: is_enable must be bool. is_enable*"):
            ConstThroughputTimer(is_enabled="True")

        # targ_throughput type check (negative number input)
        with pytest.raises(TypeError, match=r".*arg: targ_throughput should be positive int or float.*"):
            ConstThroughputTimer(targ_throughput=-1)

        # arg: targ_throughput should be positive int or float. (wrong data type input)
        with pytest.raises(TypeError, match=r".*arg: targ_throughput should be positive int or float.*"):
            ConstThroughputTimer(targ_throughput='123')

        # based_on type check (wrong data type input)
        with pytest.raises(TypeError, match=r".*arg: based_on should be BasedOn.*"):
            ConstThroughputTimer(based_on=123)


class TestConstantThroughputTimerXML:
    def test_render(self):
        element = ConstThroughputTimerXML(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.render_element()
        parsed_doc = xmltodict.parse(tag_wrapper(rendered_doc, 'test_results'))
        assert parsed_doc['test_results']['ConstantThroughputTimer']['intProp']['#text'] == '0'
        assert parsed_doc['test_results']['ConstantThroughputTimer']['@testname'] == 'My tp timer'
        assert parsed_doc['test_results']['ConstantThroughputTimer']['@enabled'] == 'false'
        assert parsed_doc['test_results']['ConstantThroughputTimer']['doubleProp']['value'] == '2'
        assert parsed_doc['test_results']['ConstantThroughputTimer']['stringProp']['#text'] == 'My comments'

    def test_render_hashtree_contain(self):
        element = ConstThroughputTimerXML(name='My tp timer',
                                          targ_throughput=2,
                                          based_on=BasedOn.THIS_THREAD_ONLY,
                                          comments='My comments',
                                          is_enabled=False)
        rendered_doc = element.render_element()
        assert '<hashTree />' in rendered_doc