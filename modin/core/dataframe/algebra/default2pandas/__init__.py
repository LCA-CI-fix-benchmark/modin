# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

"""Module default2pandas provides templates for a query compiler default-to-pandas methods."""

from .binary import BinaryDefault
from .cat import CatDefault
from .dataframe import DataFrameDefault
from .datetime import DateTimeDefault
from .default import DefaultMethod
from .groupby import GroupByDefault, SeriesGroupByDefault
from .resample import ResampleDefault
from .rolling import ExpandingDefault, RollingDefault
from .series import SeriesDefault
from .str import StrDefault

__all__ = [
    "DataFrameDefault",
    "DateTimeDefault",
    "SeriesDefault",
    "StrDefault",
    "BinaryDefault",
    "ResampleDefault",
    "RollingDefault",
    "ExpandingDefault",
    "DefaultMethod",
    "CatDefault",
    "GroupByDefault",
    "SeriesGroupByDefault",
]
