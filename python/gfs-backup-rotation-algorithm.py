#!/usr/bin/env pytest
# SPDX-License-Identifier: WTFPL

"""
Snippet implementing the Grandfather-father-son backup rotation scheme.

See https://en.wikipedia.org/wiki/Backup_rotation_scheme#Grandfather-father-son

This is a system designed to deal with a number of snapshots, to keep some of
them to have a meaningful sample over time, and trim the other excess ones.

For instance, this is the system borgbackup's borg-prune uses (the code below
does NOT come from borg's codebase).
"""


from dataclasses import dataclass, fields
import datetime


@dataclass
class Config:
    secondly: int = 0
    minutely: int = 0
    hourly: int = 0
    daily: int = 0
    weekly: int = 0
    monthly: int = 0
    yearly: int = 0


def frame_of_date(date: datetime.datetime, period: str):
    periods = {
        "secondly": ("year", "month", "day", "hour", "minute", "second"),
        "minutely": ("year", "month", "day", "hour", "minute"),
        "hourly": ("year", "month", "day", "hour"),
        "daily": ("year", "month", "day"),
        "weekly": lambda dt: (dt.year, dt.isocalendar().week),
        "monthly": ("year", "month"),
        "yearly": ("year",),
    }

    attrs = periods[period]
    if callable(attrs):
        return attrs(date)
    return tuple(getattr(date, attr) for attr in attrs)


def fit_buckets(snapshots: list[datetime.datetime], config: Config):
    buckets = {
        field.name: []
        for field in fields(Config)
    }

    # we assume the buckets are returned in order from secondly to yearly
    it_bucket = iter(buckets)
    current_bucket = next(it_bucket)
    last_kept_snapshot = None

    for snapshot in snapshots:

        # go to next bucket if current bucket is full
        no_more_buckets = False
        # config may impose that some bucket contains 0 element
        # (full with 0 element)
        # so we may jump several buckets
        while len(buckets[current_bucket]) == getattr(config, current_bucket):
            try:
                current_bucket = next(it_bucket)
            except StopIteration:
                no_more_buckets = True
                break
        if no_more_buckets:
            # discard all remaining snapshots
            break

        # here, we know we have a bucket that can contain 1 more element
        assert getattr(config, current_bucket) > 0

        if not last_kept_snapshot:
            # this is the first snapshot of all, we must keep it
            buckets[current_bucket].append(snapshot)
            last_kept_snapshot = snapshot
            continue

        # compare last snapshot with current, on the context of current bucket
        # even if last kept snapshot is in a different bucket
        if (
            frame_of_date(snapshot, current_bucket)
            != frame_of_date(last_kept_snapshot, current_bucket)
        ):
            buckets[current_bucket].append(snapshot)
            last_kept_snapshot = snapshot
            continue

    return [
        snapshot
        for snapshots in buckets.values()
        for snapshot in snapshots
    ]


def parse_datestring(datestring: str):
    return datetime.datetime.strptime(datestring, "%Y-%m-%d_%H:%M:%S")


def test():
    def parse_slist(s: str):
        return [parse_datestring(datestring) for datestring in s.strip().split()]

    snapshots = parse_slist("""
        2022-09-10_20:14:01
        2022-08-24_19:38:38
        2022-08-20_16:30:16
        2022-08-12_21:03:28
        2022-08-09_09:30:13
        2022-07-31_19:36:55
        2022-07-23_21:51:35
        2022-07-15_14:55:55
        2022-06-20_16:57:45
        2022-05-27_09:11:56
        2022-04-23_11:06:25
        2022-03-28_09:31:12
        2022-01-31_18:07:51
    """)

    config = Config(daily=7, monthly=3)

    assert fit_buckets(snapshots, config) == parse_slist("""
        2022-09-10_20:14:01
        2022-08-24_19:38:38
        2022-08-20_16:30:16
        2022-08-12_21:03:28
        2022-08-09_09:30:13
        2022-07-31_19:36:55
        2022-07-23_21:51:35
        2022-06-20_16:57:45
        2022-05-27_09:11:56
        2022-04-23_11:06:25
    """)
