#!/usr/bin/env python3
# SPDX-License-Identifier: WTFPL
# this tool is used to delete your comments (notes in Gitlab parlance)
# left on merge requests.

import datetime
import getpass
import sys

import gitlab
import dateutil.relativedelta


password = getpass.getpass("Gitlab token? ")
g = gitlab.Gitlab(private_token=password, url=sys.argv[1])

# cache for avoiding to query the same projects everytime
projects = {}

events = g.events.list(
    #before=datetime.datetime.now() - dateutil.relativedelta.relativedelta(months=6),
    iterator=True,
)
for event in events:
    if event.attributes["action_name"] == "commented on":
        assert event.attributes["target_type"] in ("DiscussionNote", "DiffNote", "Note")
        print("\n\n")
        print("--------------")
        print(event.attributes["note"]["body"])

        if event.project_id not in projects:
            projects[event.project_id] = g.projects.get(event.project_id)
        if projects[event.project_id].attributes["archived"]:
            print("Can't delete note in archived project")
            continue

        if input("Delete? ") == "y":
            g.http_request(
                "delete",
                f"/projects/{event.attributes['project_id']}/merge_requests/{event.note['noteable_iid']}/notes/{event.note['id']}"
            )
            print("Done!")
