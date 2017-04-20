#!/usr/bin/python

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
