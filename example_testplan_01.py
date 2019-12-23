from jmeter_api.configs.http_cache_manager.elements import HTTPCacheManager
from jmeter_api.timers.constant_throughput_timer.elements import ConstantThroughputTimer
from jmeter_api.timers.constant_timer.elements import ConstantTimer
from jmeter_api.non_test_elements.test_plan.elements import TestPlan
from jmeter_api.controllers.loop_controller.elements import LoopController
from jmeter_api.controllers.random_controller.elements import RandomController
from jmeter_api.samplers.http_request.elements import HttpRequest
from jmeter_api.thread_groups.common_thread_group.elements import CommonThreadGroup

if __name__ == "__main__":
    test_plan = TestPlan(name='NewTestPlan')
    test_plan.append(HTTPCacheManager(clear_each_iteration=True))
    test_plan.append(CommonThreadGroup(continue_forever=True, name='FirstThreadGroup')
                     .append(HttpRequest(host='www.google.com'))
                     .append(HttpRequest(host='www.google.com'))
                     .append(HttpRequest(host='www.google.com'))
                     .append(ConstantTimer(delay=1000))
                     )
    second_thread_group = CommonThreadGroup(continue_forever=True, name='SecondThreadGroup')
    for x in range(20):
        second_thread_group.append(HttpRequest(host='www.google.com', path=f'/new-{x}', name=f'NewSampler{x}'))
    second_thread_group.append(ConstantThroughputTimer(targ_throughput=10))
    test_plan.append(second_thread_group)

    third_thread_group = CommonThreadGroup(continue_forever=True, name='ThirdThreadGroup')
    lc = LoopController(loops = 3, name = 'loop3')
    lc2 = RandomController(ignoreSubControllers = True)
    lc2.append(HttpRequest(host='www.google.com'))
    lc.append(HttpRequest(host='www.google.com'))
    lc.append(lc2)
    lc3 = LoopController()
    third_thread_group.append(lc)
    third_thread_group.append(lc3)
    test_plan.append(third_thread_group)
    
    open('example_testplan_01.jmx', 'w').write(test_plan.to_xml())
