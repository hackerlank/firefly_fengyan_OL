# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/quest/getCanReceivedquestList.proto',
  package='protoFile.quest.getCanReceivedquestList',
  serialized_pb='\n-protoFile/quest/getCanReceivedquestList.proto\x12\'protoFile.quest.getCanReceivedquestList\",\n\x1egetCanReceivedquestListRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"\x87\x01\n\x1fgetCanReceivedquestListResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x43\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x35.protoFile.quest.getCanReceivedquestList.ResponseData\"\\\n\x0cResponseData\x12L\n\x14\x63\x61nReceivedquestList\x18\x01 \x03(\x0b\x32..protoFile.quest.getCanReceivedquestList.Quest\")\n\x05Quest\x12\x0e\n\x06taskId\x18\x01 \x01(\x05\x12\x10\n\x08taskname\x18\x02 \x01(\t')




_GETCANRECEIVEDQUESTLISTREQUEST = descriptor.Descriptor(
  name='getCanReceivedquestListRequest',
  full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=90,
  serialized_end=134,
)


_GETCANRECEIVEDQUESTLISTRESPONSE = descriptor.Descriptor(
  name='getCanReceivedquestListResponse',
  full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.quest.getCanReceivedquestList.getCanReceivedquestListResponse.data', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=137,
  serialized_end=272,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.quest.getCanReceivedquestList.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='canReceivedquestList', full_name='protoFile.quest.getCanReceivedquestList.ResponseData.canReceivedquestList', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=274,
  serialized_end=366,
)


_QUEST = descriptor.Descriptor(
  name='Quest',
  full_name='protoFile.quest.getCanReceivedquestList.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='taskId', full_name='protoFile.quest.getCanReceivedquestList.Quest.taskId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='taskname', full_name='protoFile.quest.getCanReceivedquestList.Quest.taskname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=368,
  serialized_end=409,
)

_GETCANRECEIVEDQUESTLISTRESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['canReceivedquestList'].message_type = _QUEST
DESCRIPTOR.message_types_by_name['getCanReceivedquestListRequest'] = _GETCANRECEIVEDQUESTLISTREQUEST
DESCRIPTOR.message_types_by_name['getCanReceivedquestListResponse'] = _GETCANRECEIVEDQUESTLISTRESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['Quest'] = _QUEST

class getCanReceivedquestListRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCANRECEIVEDQUESTLISTREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getCanReceivedquestList.getCanReceivedquestListRequest)

class getCanReceivedquestListResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETCANRECEIVEDQUESTLISTRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getCanReceivedquestList.getCanReceivedquestListResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getCanReceivedquestList.ResponseData)

class Quest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _QUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.quest.getCanReceivedquestList.Quest)

# @@protoc_insertion_point(module_scope)
