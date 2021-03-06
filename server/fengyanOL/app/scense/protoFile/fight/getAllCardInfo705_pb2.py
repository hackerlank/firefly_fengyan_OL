# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/fight/getAllCardInfo705.proto',
  package='protoFile.fight.getAllCardInfo705',
  serialized_pb='\n\'protoFile/fight/getAllCardInfo705.proto\x12!protoFile.fight.getAllCardInfo705\"#\n\x15getAllCardInfoRequest\x12\n\n\x02id\x18\x01 \x02(\x05\"x\n\x16getAllCardInfoResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\x12=\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32/.protoFile.fight.getAllCardInfo705.ResponseData\"J\n\x0cResponseData\x12:\n\x04\x63\x61rd\x18\x01 \x03(\x0b\x32,.protoFile.fight.getAllCardInfo705.CardsInfo\"o\n\tCardsInfo\x12\x0e\n\x06\x63\x61rdId\x18\x01 \x01(\x05\x12\x12\n\ncoinBounds\x18\x02 \x01(\x05\x12>\n\titemBound\x18\x03 \x01(\x0b\x32+.protoFile.fight.getAllCardInfo705.ItemInfo\")\n\x08ItemInfo\x12\x0e\n\x06itemId\x18\x01 \x01(\x05\x12\r\n\x05stack\x18\x02 \x01(\x05')




_GETALLCARDINFOREQUEST = descriptor.Descriptor(
  name='getAllCardInfoRequest',
  full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoRequest.id', index=0,
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
  serialized_start=78,
  serialized_end=113,
)


_GETALLCARDINFORESPONSE = descriptor.Descriptor(
  name='getAllCardInfoResponse',
  full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoResponse.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='protoFile.fight.getAllCardInfo705.getAllCardInfoResponse.data', index=2,
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
  serialized_start=115,
  serialized_end=235,
)


_RESPONSEDATA = descriptor.Descriptor(
  name='ResponseData',
  full_name='protoFile.fight.getAllCardInfo705.ResponseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='card', full_name='protoFile.fight.getAllCardInfo705.ResponseData.card', index=0,
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
  serialized_start=237,
  serialized_end=311,
)


_CARDSINFO = descriptor.Descriptor(
  name='CardsInfo',
  full_name='protoFile.fight.getAllCardInfo705.CardsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cardId', full_name='protoFile.fight.getAllCardInfo705.CardsInfo.cardId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='coinBounds', full_name='protoFile.fight.getAllCardInfo705.CardsInfo.coinBounds', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='itemBound', full_name='protoFile.fight.getAllCardInfo705.CardsInfo.itemBound', index=2,
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
  serialized_start=313,
  serialized_end=424,
)


_ITEMINFO = descriptor.Descriptor(
  name='ItemInfo',
  full_name='protoFile.fight.getAllCardInfo705.ItemInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='itemId', full_name='protoFile.fight.getAllCardInfo705.ItemInfo.itemId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stack', full_name='protoFile.fight.getAllCardInfo705.ItemInfo.stack', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=426,
  serialized_end=467,
)

_GETALLCARDINFORESPONSE.fields_by_name['data'].message_type = _RESPONSEDATA
_RESPONSEDATA.fields_by_name['card'].message_type = _CARDSINFO
_CARDSINFO.fields_by_name['itemBound'].message_type = _ITEMINFO
DESCRIPTOR.message_types_by_name['getAllCardInfoRequest'] = _GETALLCARDINFOREQUEST
DESCRIPTOR.message_types_by_name['getAllCardInfoResponse'] = _GETALLCARDINFORESPONSE
DESCRIPTOR.message_types_by_name['ResponseData'] = _RESPONSEDATA
DESCRIPTOR.message_types_by_name['CardsInfo'] = _CARDSINFO
DESCRIPTOR.message_types_by_name['ItemInfo'] = _ITEMINFO

class getAllCardInfoRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETALLCARDINFOREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.fight.getAllCardInfo705.getAllCardInfoRequest)

class getAllCardInfoResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETALLCARDINFORESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.fight.getAllCardInfo705.getAllCardInfoResponse)

class ResponseData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSEDATA
  
  # @@protoc_insertion_point(class_scope:protoFile.fight.getAllCardInfo705.ResponseData)

class CardsInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CARDSINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.fight.getAllCardInfo705.CardsInfo)

class ItemInfo(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ITEMINFO
  
  # @@protoc_insertion_point(class_scope:protoFile.fight.getAllCardInfo705.ItemInfo)

# @@protoc_insertion_point(module_scope)
