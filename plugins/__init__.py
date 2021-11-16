#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .utils import (
   get_filter_results,
   get_file_details,
   is_subscribed,
   get_poster,
   Media
)
from .channel import (
   RATING,
   GENRES
)

HELP = """
**Basic Commands**

/start : Check Bot Alive.
"""

ABOUT = """
**About Bot 🤖**

**➥ 🤖 Name: [Sensiari](http://t.me/ZoMovieBot).
    
➥ 👨‍💻 Creator: [Zaute Km](https://t.me/ZauteKm)

➥ 🌏 Languag: Python3

➥ ♻️ Library: Pyrogram Asyncio 1.13.0**
"""
