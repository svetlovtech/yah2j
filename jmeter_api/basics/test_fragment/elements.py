from abc import ABC
from typing import Union

from jmeter_api.basics.element.elements import BasicElement
from jmeter_api.basics.controller.elements import BasicController
from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.timer.elements import BasicTimer
from jmeter_api.basics.utils import IncludesElements


class BasicTestFragment(BasicElement, IncludesElements, ABC):
    def __init__(self,
                 name: str = 'BasicTestFragment',
                 comments: str = '',
                 is_enabled: bool = True):
        super().__init__(name=name,
                         comments=comments,
                         is_enabled=is_enabled)

    def append(self, new_element: Union[BasicSampler, BasicTimer, BasicConfig, BasicController]):
        if not isinstance(new_element, (BasicSampler, BasicTimer, BasicConfig, BasicController)):
            raise TypeError(
                f'new_element must be BasicSampler, BasicTimer, \
                BasicConfig or BasicController. {type(new_element)} was given')
        self._elements.append(new_element)
        return self


print.__call__()
