import os
import sys
import yaml


def check_packages(packages):
    for pkg in packages:
        if not os.path.exists(pkg):
            raise RuntimeError("Failed to find package {0}".format(pkg))
        if not os.path.exists(pkg + "/top.sls"):
            raise RuntimeError(
                "Failed to find top.sls file for {0}".format(pkg)
            )


def collect_states(packages):
    states_list = []
    for pkg in packages:
        f = pkg + "/top.sls"
        with open(f) as fh:
            sls = yaml.load(fh.read())

        if not sls or not "base" in sls:
            raise RuntimeError("{0} has no base section?".format(f))

        if not "*" in sls["base"]:
            raise RuntimeError("{0} has no \"*\" section?".format(f))

        states_list.append(sls["base"]["*"])

    return states_list


def merge_sls_list(states_list):
    items = []
    for states in states_list:
        items = items + states

    sls = {
        "base": {
            "*": items
        }
    }

    return sls


def print_yaml(sls):
    print(yaml.dump(sls, default_flow_style=False))


if __name__ == "__main__":
    packages = sys.argv[1:]

    check_packages(packages)
    states_list = collect_states(packages)
    sls = merge_sls_list(states_list)

    print_yaml(sls)
