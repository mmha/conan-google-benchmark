#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import platform

from bincrafters import build_template_default

if __name__ == "__main__":

    builder = build_template_default.get_builder()
    if platform.system() == "Windows":
        builder.add_common_builds(shared_option_name=False)
    else:
        builder.add_common_builds()
    builder.run()
