#!/usr/bin/python

# (c) 2017, Alberto Murillo <alberto.murillo.silva@intel.com>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: roulette
short_description: Russian Roulette
description:
  - This task will has 1 in M(chambers) chance of failure.
version_added: "2.4"
author: Alberto Murillo (@albertomurillo)
options:
  chambers:
    description:
      - Number of chambers in the gun.
    required: false
    default: 8
'''

EXAMPLES = '''
- name: Play russian roulette
  roulette:
    chambers: 8

- name: Suicide
  roulette:
    chambers: 1
'''

import random
from ansible.module_utils.basic import AnsibleModule


def roulette(chambers):
    return not random.randint(1, chambers) % chambers


def main():
    module = AnsibleModule(
        argument_spec=dict(
            chambers=dict(default=8, type="int"),
        ),
    )

    chambers = module.params["chambers"]
    shot = roulette(chambers)

    if shot:
        module.fail_json(msg="You died")
    else:
        module.exit_json(msg="You survived")


if __name__ == '__main__':
    main()
