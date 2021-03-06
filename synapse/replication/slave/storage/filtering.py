# -*- coding: utf-8 -*-
# Copyright 2015, 2016 OpenMarket Ltd
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

from synapse.storage.data_stores.main.filtering import FilteringStore
from synapse.storage.database import Database

from ._base import BaseSlavedStore


class SlavedFilteringStore(BaseSlavedStore):
    def __init__(self, database: Database, db_conn, hs):
        super(SlavedFilteringStore, self).__init__(database, db_conn, hs)

    # Filters are immutable so this cache doesn't need to be expired
    get_user_filter = FilteringStore.__dict__["get_user_filter"]
