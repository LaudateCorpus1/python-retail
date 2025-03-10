# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START retail_search_for_products_with_filter]
# Call Retail API to search for a products in a catalog, filter the results by different product fields.
#
import os

from google.cloud.retail import SearchRequest, SearchServiceClient

project_number = os.environ["GOOGLE_CLOUD_PROJECT_NUMBER"]


# get search service request:
def get_search_request(query: str, _filter: str):
    default_search_placement = (
        "projects/"
        + project_number
        + "/locations/global/catalogs/default_catalog/placements/default_search"
    )

    search_request = SearchRequest()
    search_request.placement = default_search_placement  # Placement is used to identify the Serving Config name.
    search_request.query = query
    search_request.filter = _filter
    search_request.page_size = 10
    search_request.visitor_id = "123456"  # A unique identifier to track visitors
    search_request.page_size = 10

    print("---search request:---")
    print(search_request)

    return search_request


# call the Retail Search:
def search():
    # TRY DIFFERENT FILTER EXPRESSIONS HERE:
    filter_ = '(colorFamilies: ANY("Black"))'

    search_request = get_search_request("Tee", filter_)
    search_response = SearchServiceClient().search(search_request)
    print("---search response---")
    print(search_response)
    return search_response


search()
# [END retail_search_for_products_with_filter]
