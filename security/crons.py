#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""crons -- DESCRIPTION

"""
import os
from django_cron import CronJobBase, Schedule


class SyncTimeCron(CronJobBase):
    r"""SyncTimeCron

    SyncTimeCron is a CronJobBase.
    Responsibility:
    """
    RUN_EVERY_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'for_river_cam'

    def do(self, ):
        r"""SUMMARY

        do()

        @Return:

        @Error:
        """
        print('DEBUG-1-crons.py')
        os.system('touch /tmp/hello')
        os.system('/usr/sbin/ntpdate eagle.center.osakafu-u.ac.jp ntp.nict.jp')


CRON_CLASSES = [
    'for_river_cam.SyncTimeCron',
]



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# crons.py ends here
