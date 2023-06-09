#! /usr/bin/python
# -*- coding: utf-8 -*-
# @author izhangxm
# @date 2021/4/16
# @fileName __init__.py
# Copyright 2017 izhangxm@gmail.com. All Rights Reserved.
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
import time
from datetime import datetime


def getFTime():
    return datetime.now().strftime('%Y%m%d%H%M%S%f')[:-3]


def getToday():
    return datetime.now().strftime('%Y%m%d')


def getTimeStamp():
    return int(time.time() * 1000)


def timestamp2Formate_time(ts, fmt):
    date = datetime.fromtimestamp(int(ts))
    return date.strftime(fmt)


def formatetime2timestamp(fmt, fmt_str):
    f_time = datetime.strptime(fmt, fmt_str)
    return int(f_time.timestamp())
