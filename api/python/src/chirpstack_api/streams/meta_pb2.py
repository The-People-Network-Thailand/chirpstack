# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/streams/meta.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!chirpstack-api/streams/meta.proto\x12\x07streams\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"\xf0\x01\n\nUplinkMeta\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRxInfo\x12\x1e\n\x16phy_payload_byte_count\x18\x04 \x01(\r\x12\x1e\n\x16mac_command_byte_count\x18\x05 \x01(\r\x12&\n\x1e\x61pplication_payload_byte_count\x18\x06 \x01(\r\x12#\n\x0cmessage_type\x18\x07 \x01(\x0e\x32\r.common.MType\"\x81\x02\n\x0c\x44ownlinkMeta\x12\x0f\n\x07\x64\x65v_eui\x18\x01 \x01(\t\x12\x1a\n\x12multicast_group_id\x18\x02 \x01(\t\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\x12\x1e\n\x16phy_payload_byte_count\x18\x04 \x01(\r\x12\x1e\n\x16mac_command_byte_count\x18\x05 \x01(\r\x12&\n\x1e\x61pplication_payload_byte_count\x18\x06 \x01(\r\x12#\n\x0cmessage_type\x18\x07 \x01(\x0e\x32\r.common.MType\x12\x12\n\ngateway_id\x18\x08 \x01(\tBq\n\x19io.chirpstack.api.streamsB\tMetaProtoP\x01Z2github.com/chirpstack/chirpstack/api/go/v4/streams\xaa\x02\x12\x43hirpstack.Streamsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.streams.meta_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031io.chirpstack.api.streamsB\tMetaProtoP\001Z2github.com/chirpstack/chirpstack/api/go/v4/streams\252\002\022Chirpstack.Streams'
  _globals['_UPLINKMETA']._serialized_start=111
  _globals['_UPLINKMETA']._serialized_end=351
  _globals['_DOWNLINKMETA']._serialized_start=354
  _globals['_DOWNLINKMETA']._serialized_end=611
# @@protoc_insertion_point(module_scope)
