# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/hall/GetRoomInfo1821.proto',
  package='protoFile.hall.GetRoomInfo1821',
  serialized_pb='\n$protoFile/hall/GetRoomInfo1821.proto\x12\x1eprotoFile.hall.GetRoomInfo1821\" \n\x12GetRoomInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"n\n\x13GetRoomInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x36\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32(.protoFile.hall.GetRoomInfo1821.RoomInfo\"l\n\x08RoomInfo\x12\x0e\n\x06roomId\x18\x01 \x01(\x05\x12\x11\n\tgroupName\x18\x02 \x01(\t\x12\x15\n\rgroupPassword\x18\x03 \x01(\t\x12\x13\n\x0b\x63opySceneId\x18\x04 \x01(\x05\x12\x11\n\tcopyLevel\x18\x05 \x01(\x05')




_GETROOMINFOREQUEST = descriptor.Descriptor(
  name='GetRoomInfoRequest',
  full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoRequest.id', index=0,
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
  serialized_start=72,
  serialized_end=104,
)


_GETROOMINFORESPONSE = descriptor.Descriptor(
  name='GetRoomInfoResponse',
  full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.hall.GetRoomInfo1821.GetRoomInfoResponse.data', index=2,
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
  serialized_start=106,
  serialized_end=216,
)


_ROOMINFO = descriptor.Descriptor(
  name='RoomInfo',
  full_name='protoFile.hall.GetRoomInfo1821.RoomInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roomId', full_name='protoFile.hall.GetRoomInfo1821.RoomInfo.roomId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupName', full_name='protoFile.hall.GetRoomInfo1821.RoomInfo.groupName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='groupPassword', full_name='protoFile.hall.GetRoomInfo1821.RoomInfo.groupPassword', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='copySceneId', full_name='protoFile.hall.GetRoomInfo1821.RoomInfo.copySceneId', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='copyLevel', full_name='protoFile.hall.GetRoomInfo1821.RoomInfo.copyLevel', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=218,
  serialized_end=326,
)

_GETROOMINFORESPONSE.fields_by_name['data'].message_type = _ROOMINFO
DESCRIPTOR.message_types_by_name['GetRoomInfoRequest'] = _GETROOMINFOREQUEST
DESCRIPTOR.message_types_by_name['GetRoomInfoResponse'] = _GETROOMINFORESPONSE
DESCRIPTOR.message_types_by_name['RoomInfo'] = _ROOMINFO

class GetRoomInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETROOMINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.GetRoomInfo1821.GetRoomInfoRequest)

class GetRoomInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETROOMINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.GetRoomInfo1821.GetRoomInfoResponse)

class RoomInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROOMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.hall.GetRoomInfo1821.RoomInfo)

# @@protoc_insertion_point(module_scope)
