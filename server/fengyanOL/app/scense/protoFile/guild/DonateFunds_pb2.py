# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protoFile/guild/DonateFunds.proto',
  package='protoFile.guild.DonateFunds',
  serialized_pb='\n!protoFile/guild/DonateFunds.proto\x12\x1bprotoFile.guild.DonateFunds\"2\n\x12\x44onateFundsRequest\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x10\n\x08\x66undsNum\x18\x02 \x02(\x05\"6\n\x13\x44onateFundsResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t')




_DONATEFUNDSREQUEST = descriptor.Descriptor(
  name='DonateFundsRequest',
  full_name='protoFile.guild.DonateFunds.DonateFundsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='protoFile.guild.DonateFunds.DonateFundsRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fundsNum', full_name='protoFile.guild.DonateFunds.DonateFundsRequest.fundsNum', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=66,
  serialized_end=116,
)


_DONATEFUNDSRESPONSE = descriptor.Descriptor(
  name='DonateFundsResponse',
  full_name='protoFile.guild.DonateFunds.DonateFundsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='protoFile.guild.DonateFunds.DonateFundsResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='message', full_name='protoFile.guild.DonateFunds.DonateFundsResponse.message', index=1,
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
  serialized_start=118,
  serialized_end=172,
)

DESCRIPTOR.message_types_by_name['DonateFundsRequest'] = _DONATEFUNDSREQUEST
DESCRIPTOR.message_types_by_name['DonateFundsResponse'] = _DONATEFUNDSRESPONSE

class DonateFundsRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DONATEFUNDSREQUEST
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.DonateFunds.DonateFundsRequest)

class DonateFundsResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DONATEFUNDSRESPONSE
  
  # @@protoc_insertion_point(class_scope:protoFile.guild.DonateFunds.DonateFundsResponse)

# @@protoc_insertion_point(module_scope)
