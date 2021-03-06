# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/securitycenter_v1beta1/proto/source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/securitycenter_v1beta1/proto/source.proto',
  package='google.cloud.securitycenter.v1beta1',
  syntax='proto3',
  serialized_pb=_b('\n6google/cloud/securitycenter_v1beta1/proto/source.proto\x12#google.cloud.securitycenter.v1beta1\x1a\x1cgoogle/api/annotations.proto\"A\n\x06Source\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\tB|\n\'com.google.cloud.securitycenter.v1beta1ZQgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1beta1;securitycenterb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='google.cloud.securitycenter.v1beta1.Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.cloud.securitycenter.v1beta1.Source.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.cloud.securitycenter.v1beta1.Source.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.cloud.securitycenter.v1beta1.Source.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=125,
  serialized_end=190,
)

DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'google.cloud.securitycenter_v1beta1.proto.source_pb2'
  ,
  __doc__ = """Security Center's finding source. A finding source is an entity or a
  mechanism that can produce a finding. A source can also be thought of as
  a container of findings that come from the same scanner, logger,
  monitor, etc.
  
  
  Attributes:
      name:
          The relative resource name of this source. See: https://cloud.
          google.com/apis/design/resource\_names#relative\_resource\_nam
          e Example: "organizations/123/sources/456"
      display_name:
          The source’s display name. A source’s display name must be
          unique amongst its siblings, e.g. no two sources with the same
          parent can share the same display name. The display name must
          start and end with a letter or digit, may contain letters,
          digits, spaces, hyphens and underscores and can be no longer
          than 30 characters. This is captured by the regular
          expression: `:raw-latex:`\p{L}`:raw-latex:`\p{N}` <%7B\p%7BL%7
          D\p%7BN%7D_-%20%5D%7B0,28%7D%5B\p%7BL%7D\p%7BN%7D%5D>`__?.
      description:
          The description of the source (max of 1024 characters).
          Example: "Cloud Security Scanner is a web security scanner for
          common vulnerabilities in Google App Engine applications. It
          can automatically scan and detect four common vulnerabilities,
          including cross-site-scripting (XSS), Flash injection, mixed
          content (HTTP in HTTPS), and outdated/insecure libraries."
  """,
  # @@protoc_insertion_point(class_scope:google.cloud.securitycenter.v1beta1.Source)
  ))
_sym_db.RegisterMessage(Source)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'com.google.cloud.securitycenter.v1beta1ZQgoogle.golang.org/genproto/googleapis/cloud/securitycenter/v1beta1;securitycenter'))
# @@protoc_insertion_point(module_scope)
