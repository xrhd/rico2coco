# coding=utf-8
# Copyright 2021 DeepMind Technologies Limited.
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

"""Example script demonstrating usage of AndroidEnv."""

import cv2
import torch
from PIL import Image

from typing import Dict
from absl import app
from absl import flags
from absl import logging

import android_env
from dm_env import specs
import numpy as np

FLAGS = flags.FLAGS

# Simulator args.
flags.DEFINE_string('avd_name', None, 'Name of AVD to use.')
flags.DEFINE_string('android_avd_home', '~/.android/avd', 'Path to AVD.')
flags.DEFINE_string('android_sdk_root', '~/Android/Sdk', 'Path to SDK.')
flags.DEFINE_string('emulator_path',
                    '~/Android/Sdk/emulator/emulator', 'Path to emulator.')
flags.DEFINE_string('adb_path',
                    '~/Android/Sdk/platform-tools/adb', 'Path to ADB.')

# Environment args.
flags.DEFINE_string('task_path', None, 'Path to task textproto file.')

# Experiment args.
flags.DEFINE_integer('num_steps', 1000, 'Number of steps to take.')


def agent():
  # Model
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='rico2coco_click_best.pt')
  return model


def main(_):
  model = agent()

  with android_env.load(
      emulator_path=FLAGS.emulator_path,
      android_sdk_root=FLAGS.android_sdk_root,
      android_avd_home=FLAGS.android_avd_home,
      avd_name=FLAGS.avd_name,
      adb_path=FLAGS.adb_path,
      task_path=FLAGS.task_path,
      run_headless=False) as env:

    action_spec = env.action_spec()
    action_type_dtype = action_spec["action_type"].dtype
    touch_position_dtyep = action_spec["touch_position"].dtype

    def get_random_action_from_yolo(observation):
      image = observation["pixels"]
      results = model([image])
      pred_df = results.pandas().xyxy[0]

      if (pred_df.shape[0] == 0) and (0 not in pred_df['class']):
        return {
          'action_type':  np.random.randint(low=0, high=1, dtype=action_type_dtype), 
          'touch_position': np.array([.1, .1]).astype(touch_position_dtyep)
        }

      try:
        counted = pred_df['class'].value_counts()
        if 0 not in counted:
          clickable_weights, not_clickable_weights = 1, 1
        else:
          clickable_weights, not_clickable_weights = (0.7*counted[0], 0.3*counted[1]) / counted.sum()

        pred_df['weights'] = np.where(pred_df['class'] == 0, clickable_weights, not_clickable_weights)
        gui_element = pred_df.sample(n=1, weights='weights').iloc[0]
        image.shape
        x = (gui_element.xmin + gui_element.xmax) / (2*image.shape[1])
        y = (gui_element.ymin + gui_element.ymax) / (2*image.shape[0])
        return {
          'action_type':  np.random.randint(low=0, high=3, dtype=action_type_dtype), 
          'touch_position': np.array([x, y]).astype(touch_position_dtyep)
        }

      except Exception as e:
        logging.info(e)
        return {
          'action_type':  np.random.randint(low=0, high=1, dtype=action_type_dtype), 
          'touch_position': np.array([.1, .1]).astype(touch_position_dtyep)
        }
        

    def get_random_action() -> Dict[str, np.ndarray]:
      """Returns a random AndroidEnv action."""
      action = {}
      for k, v in action_spec.items():
        if isinstance(v, specs.DiscreteArray):
          action[k] = np.random.randint(low=0, high=v.num_values, dtype=v.dtype)
        else:
          action[k] = np.random.random(size=v.shape).astype(v.dtype)
      return action

    _ = env.reset()
    
    action = get_random_action()
    for step in range(FLAGS.num_steps):
      timestep = env.step(action=action)
      action = get_random_action_from_yolo(timestep.observation)
      print(action)
      reward = timestep.reward
      logging.info('Step %r, action: %r, reward: %r', step, action, reward)



if __name__ == '__main__':
  logging.set_verbosity('info')
  logging.set_stderrthreshold('info')
  flags.mark_flags_as_required(['avd_name', 'task_path'])
  app.run(main)
