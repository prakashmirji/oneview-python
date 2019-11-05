# -*- coding: utf-8 -*-
###
# (C) Copyright [2019] Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future import standard_library

standard_library.install_aliases()


from hpOneView.resources.resource import Resource


class InternalLinkSets(Resource):
    """
    Internal Link Sets API client.

    Note:
        This resource is available for API version 300 or later.

    """

    URI = '/rest/internal-link-sets'

    def __init__(self, connection, data=None):
        super(InternalLinkSets, self).__init__(connection, data)

    def get_all(self, start=0, count=-1, filter='', query='', sort='', view='', fields=''):
        """
        Gets a paginated collection of all internal link sets.
        The collection is based on optional sorting and filtering and is constrained by start and count parameters.

        Args:
            start:
                The first item to return, using 0-based indexing.
                If not specified, the default is 0 - start with the first available item.
            count:
                The number of resources to return. A count of -1 requests all items.
                The actual number of items in the response might differ from the requested
                count if the sum of start and count exceeds the total number of items.
            filter (list or str):
                A general filter/query string to narrow the list of items returned. The
                default is no filter; all resources are returned.
            query:
                A general query string to narrow the list of resources returned. The default is
                no query - all resources are returned.
            sort:
                The sort order of the returned data set. By default, the sort order is based
                on create time with the oldest entry first.
            fields:
                Specifies which fields should be returned in the result set.
            view:
                Return a specific subset of the attributes of the resource or collection, by specifying the name
                of a predefined view. The default view is expand - show all attributes of the resource and all
                elements of collections of resources.

        Returns:
            list:  Internal Link Set Collection.
        """
        return self._helper.get_all(start=start, count=count, filter=filter,
                                    query=query, sort=sort, view=view, fields=fields)
