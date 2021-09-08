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

  # # Images
  # for f in ['zidane.jpg', 'bus.jpg']:
  #   torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images
  # img1 = Image.open('zidane.jpg')  # PIL image
  # img2 = cv2.imread('bus.jpg')[..., ::-1]  # OpenCV image (BGR to RGB)
  # imgs = [img1, img2]  # batch of images

  # # Inference
  # results = model(imgs, size=640)

  return model


def main(_):

  model = agent()

  def get_results(img):
    results = model([img])
    return results

  with android_env.load(
      emulator_path=FLAGS.emulator_path,
      android_sdk_root=FLAGS.android_sdk_root,
      android_avd_home=FLAGS.android_avd_home,
      avd_name=FLAGS.avd_name,
      adb_path=FLAGS.adb_path,
      task_path=FLAGS.task_path,
      run_headless=False) as env:

    action_spec = env.action_spec()

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

    for step in range(FLAGS.num_steps):
      action = get_random_action()
      timestep = env.step(action=action)
      obs = timestep.observation
      resuils = get_results(obs['pixels'])
      print(resuils)
      resuils.show()

      reward = timestep.reward
      logging.info('Step %r, action: %r, reward: %r', step, action, reward)



if __name__ == '__main__':
  logging.set_verbosity('info')
  logging.set_stderrthreshold('info')
  flags.mark_flags_as_required(['avd_name', 'task_path'])
  app.run(main)
