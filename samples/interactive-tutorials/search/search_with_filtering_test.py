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

# Call Retail API to search for a products in a catalog using only search query.
#
import re
import subprocess

from search_with_filtering import search


def test_search_with_filtering_pass():
    output = str(
        subprocess.check_output("python search_with_filtering.py", shell=True)
    )

    assert re.match(".*search request.*", output)
    assert re.match(".*search response.*", output)
    # check the response contains some products
    assert re.match(".*results.*id.*", output)


def test_search_with_filtering():
    response = search()

    assert len(response.results) == 10
    product_title = response.results[0].product.title
    assert re.match(".*Tee.*", product_title)
    assert re.match(".*Black.*", product_title)
    assert "Black" in response.results[0].product.color_info.color_families
    assert response.total_size == 16
