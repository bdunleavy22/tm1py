import typing
import unittest

from charset_normalizer.md import annotations

import TM1py.Objects
from TM1py.Objects.Application import ApplicationTypes
from TM1py.Objects.TM1Object import TM1Object
from TM1py.Objects.ChoreStartTime import ChoreStartTime
from TM1py.Objects.ChoreFrequency import ChoreFrequency
from TM1py.Objects.ChoreTask import ChoreTask
from TM1py.Objects.Element import Element
from TM1py.Objects.ElementAttribute import ElementAttribute
from TM1py.Objects.ProcessDebugBreakpoint import BreakPointType, HitMode

class TestTM1Objects(unittest.TestCase):
    def setUp(self) -> None: ...
    type_to_default_values = {
        str: 'default_string',
        typing.Iterable[str]: ('default', 'Iterable', 'str'),
        typing.Union[ApplicationTypes, str]: ApplicationTypes.VIEW,
        ChoreStartTime: ChoreStartTime(1, 1, 1, 1, 1, 1, ),
        bool: True,
        ChoreFrequency: ChoreFrequency(1, 1, 1, 1),
        typing.Iterable[ChoreTask]: (ChoreTask(1, '', [{'':''}]), ),
        int: 1,
        typing.Union[Element.Types, str]: Element.Types.STRING,
        typing.List[str]: ('default', 'List', 'str'),
        typing.Union[ElementAttribute.Types, str]: ElementAttribute.Types.STRING,
        typing.Union[BreakPointType, str]: BreakPointType.PROCESS_DEBUG_CONTEXT_LINE_BREAK_POINT,
        typing.Union[HitMode, str]: HitMode.BREAK_ALWAYS,
    }
    list_of_objects = [(object_name, obj) for object_name, obj in TM1py.Objects.__dict__.items() if object_name[0] != '_' and isinstance(obj, type) if issubclass(obj, TM1Object)]

    def test_object_initialization(self):
        for object_name, obj in self.list_of_objects:
            object_params = obj.__init__.__annotations__.items()
            obj(**{keyword_arg: self.type_to_default_values.get(keyword_type, None) for keyword_arg, keyword_type in object_params})


    def test_object_initialization_from_object(self):
        for object_name, obj in self.list_of_objects:
            object_params = obj.__init__.__annotations__.items()
            old_obj = obj(**{keyword_arg: self.type_to_default_values.get(keyword_type, None) for keyword_arg, keyword_type in object_params})
            print(obj)
            print(old_obj)
            new_obj = obj.from_object(old_obj)
