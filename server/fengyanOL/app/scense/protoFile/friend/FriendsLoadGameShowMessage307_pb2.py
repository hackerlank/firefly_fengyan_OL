# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/friend/FriendsLoadGameShowMessage307.proto',
  package='protoFile.friend.FriendsLoadGameShowMessage307',
  serialized_pb='\n4protoFile/friend/FriendsLoadGameShowMessage307.proto\x12.protoFile.friend.FriendsLoadGameShowMessage307\"V\n!friendsLoadGameShowMessageRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08\x66riendId\x18\x02 \x02(\x05\x12\x13\n\x0bshowMesFlag\x18\x03 \x02(\x08\"E\n\"friendsLoadGameShowMessageResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_FRIENDSLOADGAMESHOWMESSAGEREQUEST = descriptor.Descriptor(
  name='friendsLoadGameShowMessageRequest',
  full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='friendId', full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageRequest.friendId', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='showMesFlag', full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageRequest.showMesFlag', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=104,
  serialized_end=190,
)


_FRIENDSLOADGAMESHOWMESSAGERESPONSE = descriptor.Descriptor(
  name='friendsLoadGameShowMessageResponse',
  full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageResponse.message', index=1,
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
  serialized_start=192,
  serialized_end=261,
)

DESCRIPTOR.message_types_by_name['friendsLoadGameShowMessageRequest'] = _FRIENDSLOADGAMESHOWMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['friendsLoadGameShowMessageResponse'] = _FRIENDSLOADGAMESHOWMESSAGERESPONSE

class friendsLoadGameShowMessageRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDSLOADGAMESHOWMESSAGEREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageRequest)

class friendsLoadGameShowMessageResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDSLOADGAMESHOWMESSAGERESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.friend.FriendsLoadGameShowMessage307.friendsLoadGameShowMessageResponse)

# @@protoc_insertion_point(module_scope)
