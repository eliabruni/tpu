# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Factory to provide model configs."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


import sys
sys.path.append('/content/tpu/models/')



import os
import pprint
from absl import flags

import tensorflow as tf

from configs import retinanet_config
from hyperparameters import params_dict


def config_generator(model):
  """Model function generator."""
  if model == 'retinanet':
    default_config = retinanet_config.RETINANET_CFG
    restrictions = retinanet_config.RETINANET_RESTRICTIONS
  else:
    raise ValueError('Model %s is not supported.' % model)

  return params_dict.ParamsDict(default_config, restrictions)
