# -*- coding: utf-8 -*-
import logging
import json
from towhee import pipe


# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')

def handler(event, context):
  # evt = json.loads(event)
  logger = logging.getLogger()
  # logger.info('hello world')
  p = pipe.input('num').output('num')
  res = p(1)
  print(res.to_list())
  return '200'

# p = pipe.input('num').output('num')
# res = p(1)
# print(res.to_list())