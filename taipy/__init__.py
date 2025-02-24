# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

from importlib.util import find_spec
from importlib import import_module

# Check if "taipy" package exists
if find_spec("taipy"):
    submodules = [
        "common.config._init",
        "gui._init",
        "core._init",
        "rest._init",
        "gui_core._init",
        "enterprise._init",
        "designer._init",
    ]

    # Dynamically import available submodules
    for submodule in submodules:
        module_path = f"taipy.{submodule}"
        if find_spec(module_path):
            import_module(module_path)

    # Import taipy._run if available
    if find_spec("taipy._run"):
        from taipy._run import _run as run
