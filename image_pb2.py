# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: image.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bimage.proto\"\"\n\x0cImageRequest\x12\x12\n\nimage_data\x18\x01 \x01(\x0c\"\x1f\n\rImageResponse\x12\x0e\n\x06status\x18\x01 \x01(\t2:\n\x0cImageService\x12*\n\tSaveImage\x12\r.ImageRequest\x1a\x0e.ImageResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGEREQUEST._serialized_start=15
  _IMAGEREQUEST._serialized_end=49
  _IMAGERESPONSE._serialized_start=51
  _IMAGERESPONSE._serialized_end=82
  _IMAGESERVICE._serialized_start=84
  _IMAGESERVICE._serialized_end=142
# @@protoc_insertion_point(module_scope)
