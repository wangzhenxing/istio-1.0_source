# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mixer/adapter/model/v1beta1/template.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mixer/adapter/model/v1beta1/template.proto',
  package='istio.mixer.adapter.model.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n*mixer/adapter/model/v1beta1/template.proto\x12!istio.mixer.adapter.model.v1beta1\"\x1e\n\x08Template\x12\x12\n\ndescriptor\x18\x01 \x01(\tB*Z(istio.io/api/mixer/adapter/model/v1beta1b\x06proto3')
)




_TEMPLATE = _descriptor.Descriptor(
  name='Template',
  full_name='istio.mixer.adapter.model.v1beta1.Template',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='istio.mixer.adapter.model.v1beta1.Template.descriptor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=81,
  serialized_end=111,
)

DESCRIPTOR.message_types_by_name['Template'] = _TEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Template = _reflection.GeneratedProtocolMessageType('Template', (_message.Message,), dict(
  DESCRIPTOR = _TEMPLATE,
  __module__ = 'mixer.adapter.model.v1beta1.template_pb2'
  # @@protoc_insertion_point(class_scope:istio.mixer.adapter.model.v1beta1.Template)
  ))
_sym_db.RegisterMessage(Template)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z(istio.io/api/mixer/adapter/model/v1beta1'))
# @@protoc_insertion_point(module_scope)
