# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Simon Fang <sifang@cisco.com> AND Stien Vanderhallen <stienvan@cisco.com>"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"

# Webex integration credentials
webex_integration_client_id = "<insert_webex_integration_client_id>"
webex_integration_client_secret= "<insertwebex_integration_client_secret>"
webex_integration_redirect_uri = "http://127.0.0.1:5000/webexoauth"
webex_integration_scope = "meeting:preferences_read meeting:recordings_read meeting:admin_recordings_read spark-compliance:meetings_write spark:all"

# AWS Variables
AWS_ACCESS_KEY_ID = "<insert_AWS_ACCESS_KEY_ID>"
AWS_SECRET_ACCESS_KEY = "<insert_AWS_SECRET_ACCESS_KEY>"
REGION_NAME = "<insert_REGION_NAME>"
BUCKET_NAME = "<insert_BUCKET_NAME>"