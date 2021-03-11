# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orders.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import items_pb2 as items__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orders.proto',
  package='orders',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0corders.proto\x12\x06orders\x1a\x0bitems.proto\x1a\x1bgoogle/protobuf/empty.proto\"@\n\x05Order\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x1a\n\x05items\x18\x03 \x03(\x0b\x32\x0b.items.Item\"\x12\n\x10OrderListRequest\"\"\n\x14OrderRetrieveRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x32\x89\x02\n\x0fOrderController\x12\x33\n\x04List\x12\x18.orders.OrderListRequest\x1a\r.orders.Order\"\x00\x30\x01\x12(\n\x06\x43reate\x12\r.orders.Order\x1a\r.orders.Order\"\x00\x12\x39\n\x08Retrieve\x12\x1c.orders.OrderRetrieveRequest\x1a\r.orders.Order\"\x00\x12(\n\x06Update\x12\r.orders.Order\x1a\r.orders.Order\"\x00\x12\x32\n\x07\x44\x65stroy\x12\r.orders.Order\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3'
  ,
  dependencies=[items__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_ORDER = _descriptor.Descriptor(
  name='Order',
  full_name='orders.Order',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.Order.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='orders.Order.user_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='items', full_name='orders.Order.items', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=130,
)


_ORDERLISTREQUEST = _descriptor.Descriptor(
  name='OrderListRequest',
  full_name='orders.OrderListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=132,
  serialized_end=150,
)


_ORDERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='OrderRetrieveRequest',
  full_name='orders.OrderRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='orders.OrderRetrieveRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=186,
)

_ORDER.fields_by_name['items'].message_type = items__pb2._ITEM
DESCRIPTOR.message_types_by_name['Order'] = _ORDER
DESCRIPTOR.message_types_by_name['OrderListRequest'] = _ORDERLISTREQUEST
DESCRIPTOR.message_types_by_name['OrderRetrieveRequest'] = _ORDERRETRIEVEREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Order = _reflection.GeneratedProtocolMessageType('Order', (_message.Message,), {
  'DESCRIPTOR' : _ORDER,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.Order)
  })
_sym_db.RegisterMessage(Order)

OrderListRequest = _reflection.GeneratedProtocolMessageType('OrderListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERLISTREQUEST,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderListRequest)
  })
_sym_db.RegisterMessage(OrderListRequest)

OrderRetrieveRequest = _reflection.GeneratedProtocolMessageType('OrderRetrieveRequest', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRETRIEVEREQUEST,
  '__module__' : 'orders_pb2'
  # @@protoc_insertion_point(class_scope:orders.OrderRetrieveRequest)
  })
_sym_db.RegisterMessage(OrderRetrieveRequest)



_ORDERCONTROLLER = _descriptor.ServiceDescriptor(
  name='OrderController',
  full_name='orders.OrderController',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=189,
  serialized_end=454,
  methods=[
  _descriptor.MethodDescriptor(
    name='List',
    full_name='orders.OrderController.List',
    index=0,
    containing_service=None,
    input_type=_ORDERLISTREQUEST,
    output_type=_ORDER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='orders.OrderController.Create',
    index=1,
    containing_service=None,
    input_type=_ORDER,
    output_type=_ORDER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='orders.OrderController.Retrieve',
    index=2,
    containing_service=None,
    input_type=_ORDERRETRIEVEREQUEST,
    output_type=_ORDER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='orders.OrderController.Update',
    index=3,
    containing_service=None,
    input_type=_ORDER,
    output_type=_ORDER,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Destroy',
    full_name='orders.OrderController.Destroy',
    index=4,
    containing_service=None,
    input_type=_ORDER,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ORDERCONTROLLER)

DESCRIPTOR.services_by_name['OrderController'] = _ORDERCONTROLLER

# @@protoc_insertion_point(module_scope)
