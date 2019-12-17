from jmeter_api.basics.config.elements import BasicConfig
from jmeter_api.basics.sampler.elements import BasicSampler
from jmeter_api.basics.utils import FileEncoding, Renderable
from xml.etree.ElementTree import tostring
from typing import List
from enum import Enum
import os


class ShareMode(Enum):
    ALL = 'shareMode.all'
    GROUP = 'shareMode.group'
    THREAD = 'shareMode.thread'


class CsvDataSetConfig(BasicConfig, Renderable):

    root_element_name = 'CSVDataSet'
    TEMPLATE = 'csv_data_set_config_template.xml'

    def __init__(self,
                 file_path,
                 variable_names: List[str],
                 file_encoding: FileEncoding = FileEncoding.UTF8,
                 ignore_first_line: bool = False,
                 delimiter: str = ",",
                 quoted_data: bool = False,
                 recycle: bool = True,
                 stop_thread: bool = False,
                 share_mode: ShareMode = ShareMode.ALL,
                 name: str = 'CsvDataSetConfig',
                 comments: str = '',
                 is_enabled: bool = True):
        self.file_path = file_path
        self.delimiter = delimiter
        self.variable_names = variable_names
        self.file_encoding = file_encoding
        self.ignore_first_line = ignore_first_line
        self.quoted_data = quoted_data
        self.recycle = recycle
        self.stop_thread = stop_thread
        self.share_mode = share_mode
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, value):
        if os.path.isfile(value):
            self._file_path = value
        else:
            raise FileNotFoundError(f'{value} is not file')

    @property
    def variable_names(self) -> List[str]:
        return self._variable_names

    @variable_names.setter
    def variable_names(self, value):
        if not isinstance(value, list):
            raise TypeError(
                f'variable_names must be List[str]. variable_names {type(value)} = {value}')
        else:
            for element in value:
                if not isinstance(element, str):
                    raise TypeError(
                        f'All elements must be str. element: {type(element)} = {element}')
                elif element.isdigit():
                    raise TypeError(
                        f'elements must contain chars: {type(element)} = {element}')
            self._variable_names = self.delimiter.join(value)

    @property
    def file_encoding(self) -> FileEncoding:
        return self._fileEncoding

    @file_encoding.setter
    def file_encoding(self, value):
        if not isinstance(value, FileEncoding):
            raise TypeError(
                f'file_encoding must be FileEncoding. file_encoding {type(value)} = {value}')
        else:
            self._fileEncoding = value

    @property
    def ignore_first_line(self) -> bool:
        return self._ignore_first_line

    @ignore_first_line.setter
    def ignore_first_line(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'ignore_first_line must be bool. ignore_first_line {type(value)} = {value}')
        else:
            self._ignore_first_line = str(value).lower()

    @property
    def delimiter(self) -> str:
        return self._delimiter

    @delimiter.setter
    def delimiter(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'delimiter must be str. delimiter {type(value)} = {value}')
        else:
            self._delimiter = value

    @property
    def quoted_data(self) -> bool:
        return self._quoted_data

    @quoted_data.setter
    def quoted_data(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'quoted_data must be bool. quoted_data {type(value)} = {value}')
        else:
            self._quoted_data = str(value).lower()

    @property
    def recycle(self) -> bool:
        return self._recycle

    @recycle.setter
    def recycle(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'recycle must be bool. recycle {type(value)} = {value}')
        else:
            self._recycle = str(value).lower()

    @property
    def stop_thread(self) -> bool:
        return self._stop_thread

    @stop_thread.setter
    def stop_thread(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'stop_thread must be bool. stop_thread {type(value)} = {value}')
        else:
            self._stop_thread = str(value).lower()

    @property
    def share_mode(self) -> ShareMode:
        return self._share_mode

    @share_mode.setter
    def share_mode(self, value):
        if not isinstance(value, ShareMode):
            raise TypeError(
                f'share_mode must be ShareMode. share_mode {type(value)} = {value}')
        else:
            self._share_mode = value

    def to_xml(self) -> str:
        element_root, xml_tree = super().to_xml()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'TestPlan.comments':
                    element.text = self.comments
                elif element.attrib['name'] == 'delimiter':
                    element.text = self.delimiter
                elif element.attrib['name'] == 'fileEncoding':
                    element.text = self.file_encoding.value
                elif element.attrib['name'] == 'filename':
                    element.text = self.file_path
                elif element.attrib['name'] == 'ignoreFirstLine':
                    element.text = self.ignore_first_line
                elif element.attrib['name'] == 'quotedData':
                    element.text = self.quoted_data
                elif element.attrib['name'] == 'recycle':
                    element.text = self.recycle
                elif element.attrib['name'] == 'shareMode':
                    element.text = self.share_mode.value
                elif element.attrib['name'] == 'stopThread':
                    element.text = self.stop_thread
                elif element.attrib['name'] == 'variableNames':
                    element.text = self.variable_names
            except KeyError:
                continue
        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data


class HTTPCacheManager(BasicSampler, Renderable):

    root_element_name = 'CacheManager'
    TEMPLATE = 'http_cache_manager.xml'

    def __init__(self,
                 clear_each_iteration: bool = False,
                 use_cache_control: bool = True,
                 max_elements_in_cache: int = 300,
                 name: str = 'HTTP_Cache_Manager',
                 comments: str = '',
                 is_enabled: bool = True):
        self.clear_each_iteration = clear_each_iteration
        self.use_cache_control = use_cache_control
        self.max_elements_in_cache = max_elements_in_cache
        super().__init__(name=name, comments=comments, is_enabled=is_enabled)

    @property
    def clear_each_iteration(self) -> bool:
        return self._clear_each_iteration

    @clear_each_iteration.setter
    def clear_each_iteration(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'clear_each_iteration must be bool. \
                    clear_each_iteration {type(value)} = {value}')
        else:
            self._clear_each_iteration = str(value).lower()

    @property
    def use_cache_control(self) -> bool:
        return self._use_cache_control

    @use_cache_control.setter
    def use_cache_control(self, value):
        if not isinstance(value, bool):
            raise TypeError(
                f'use_cache_control must be bool. use_cache_control {type(value)} = {value}')
        else:
            self._use_cache_control = str(value).lower()

    @property
    def max_elements_in_cache(self) -> int:
        return self._max_elements_in_cache

    @max_elements_in_cache.setter
    def max_elements_in_cache(self, value):
        if not isinstance(value, int):
            raise TypeError(
                f'max_elements_in_cache must be int. \
                max_elements_in_cache {type(value)} = {value}')
        else:
            self._max_elements_in_cache = str(value)

    def to_xml(self) -> str:
        element_root, xml_tree = super().to_xml()

        for element in list(element_root):
            try:
                if element.attrib['name'] == 'clearEachIteration':
                    element.text = self.clear_each_iteration
                elif element.attrib['name'] == 'useExpires':
                    element.text = self.use_cache_control
                elif element.attrib['name'] == 'maxSize':
                    element.text = self.max_elements_in_cache
            except KeyError:
                continue

        xml_data = ''
        for element in list(xml_tree):
            xml_data += tostring(element).decode('utf8')
        return xml_data