#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""month_schedules_view -- DESCRIPTION

"""
from home.models import MainEvent
from home.management.commands.synccal import Command as SynccalCommand
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import admin

import os
import shutil
import xlwt
import glob
from time import sleep
from copy import deepcopy
from sato import settings
import datetime
from dateutil.relativedelta import relativedelta


SCHEDULE_PATH = os.path.join(settings.MEDIA_ROOT, 'schedules',)


ALIGN_CENTER = xlwt.Alignment()
ALIGN_CENTER.horz = 2
FONT = xlwt.Font()
FONT.height = 11 * 20 # for 11point

TITLE_FONT = xlwt.Font()
TITLE_FONT.height = 20 * 20 # for 11point
TITLE_STYLE = xlwt.XFStyle()
TITLE_STYLE.font = TITLE_FONT
TITLE_STYLE.alignment = ALIGN_CENTER

SUBTITLE_FONT = xlwt.Font()
SUBTITLE_FONT.bold = True
SUBTITLE_FONT.height = 11 * 20 # for 11point
SUBTITLE_STYLE = xlwt.XFStyle()
SUBTITLE_STYLE.font = SUBTITLE_FONT

TOP_LEFT_BORDER = xlwt.Borders()
TOP_LEFT_BORDER.top = xlwt.Borders.THICK
TOP_LEFT_BORDER.left = xlwt.Borders.THICK
TOP_LEFT_BORDER.bottom = xlwt.Borders.THIN
TOP_LEFT_BORDER.right = xlwt.Borders.THIN
TOP_LEFT_STYLE = xlwt.XFStyle()
TOP_LEFT_STYLE.borders = TOP_LEFT_BORDER
TOP_LEFT_STYLE.alignment = ALIGN_CENTER
TOP_LEFT_STYLE.font = FONT

TOP_MIDDLE_BORDER = xlwt.Borders()
TOP_MIDDLE_BORDER.top = xlwt.Borders.THICK
TOP_MIDDLE_BORDER.left = xlwt.Borders.THIN
TOP_MIDDLE_BORDER.right = xlwt.Borders.THIN
TOP_MIDDLE_BORDER.bottom = xlwt.Borders.THIN
TOP_MIDDLE_STYLE = xlwt.XFStyle()
TOP_MIDDLE_STYLE.borders = TOP_MIDDLE_BORDER
TOP_MIDDLE_STYLE.alignment = ALIGN_CENTER
TOP_MIDDLE_STYLE.font = FONT

LEFT_MIDDLE_BORDER = xlwt.Borders()
LEFT_MIDDLE_BORDER.top = xlwt.Borders.THIN
LEFT_MIDDLE_BORDER.left = xlwt.Borders.THICK
LEFT_MIDDLE_BORDER.right = xlwt.Borders.THIN
LEFT_MIDDLE_BORDER.bottom = xlwt.Borders.THIN
LEFT_MIDDLE_STYLE = xlwt.XFStyle()
LEFT_MIDDLE_STYLE.borders = LEFT_MIDDLE_BORDER
LEFT_MIDDLE_STYLE.alignment = ALIGN_CENTER
LEFT_MIDDLE_STYLE.font = FONT

RIGHT_TOP_BORDER = xlwt.Borders()
RIGHT_TOP_BORDER.top = xlwt.Borders.THICK
RIGHT_TOP_BORDER.left = xlwt.Borders.THIN
RIGHT_TOP_BORDER.right = xlwt.Borders.THICK
RIGHT_TOP_BORDER.bottom = xlwt.Borders.THIN
RIGHT_TOP_STYLE = xlwt.XFStyle()
RIGHT_TOP_STYLE.borders = RIGHT_TOP_BORDER
RIGHT_TOP_STYLE.alignment = ALIGN_CENTER
RIGHT_TOP_STYLE.font = FONT

RIGHT_MIDDLE_BORDER = xlwt.Borders()
RIGHT_MIDDLE_BORDER.top = xlwt.Borders.THIN
RIGHT_MIDDLE_BORDER.left = xlwt.Borders.THIN
RIGHT_MIDDLE_BORDER.right = xlwt.Borders.THICK
RIGHT_MIDDLE_BORDER.bottom = xlwt.Borders.THIN
RIGHT_MIDDLE_STYLE = xlwt.XFStyle()
RIGHT_MIDDLE_STYLE.borders = RIGHT_MIDDLE_BORDER
RIGHT_MIDDLE_STYLE.alignment = ALIGN_CENTER
RIGHT_MIDDLE_STYLE.font = FONT

LEFT_BOTTOM_BORDER = xlwt.Borders()
LEFT_BOTTOM_BORDER.top = xlwt.Borders.THIN
LEFT_BOTTOM_BORDER.left = xlwt.Borders.THICK
LEFT_BOTTOM_BORDER.right = xlwt.Borders.THIN
LEFT_BOTTOM_BORDER.bottom = xlwt.Borders.THIN
LEFT_BOTTOM_STYLE = xlwt.XFStyle()
LEFT_BOTTOM_STYLE.borders = LEFT_BOTTOM_BORDER
LEFT_BOTTOM_STYLE.alignment = ALIGN_CENTER
LEFT_BOTTOM_STYLE.font = FONT

RIGHT_BOTTOM_BORDER = xlwt.Borders()
RIGHT_BOTTOM_BORDER.top = xlwt.Borders.THIN
RIGHT_BOTTOM_BORDER.left = xlwt.Borders.THIN
RIGHT_BOTTOM_BORDER.right = xlwt.Borders.THICK
RIGHT_BOTTOM_BORDER.bottom = xlwt.Borders.THIN
RIGHT_BOTTOM_STYLE = xlwt.XFStyle()
RIGHT_BOTTOM_STYLE.borders = RIGHT_BOTTOM_BORDER
RIGHT_BOTTOM_STYLE.alignment = ALIGN_CENTER
RIGHT_BOTTOM_STYLE.font = FONT

BOTTOM_MIDDLE_BORDER = xlwt.Borders()
BOTTOM_MIDDLE_BORDER.top = xlwt.Borders.THIN
BOTTOM_MIDDLE_BORDER.left = xlwt.Borders.THIN
BOTTOM_MIDDLE_BORDER.right = xlwt.Borders.THIN
BOTTOM_MIDDLE_BORDER.bottom = xlwt.Borders.THIN
BOTTOM_MIDDLE_STYLE = xlwt.XFStyle()
BOTTOM_MIDDLE_STYLE.borders = BOTTOM_MIDDLE_BORDER
BOTTOM_MIDDLE_STYLE.alignment = ALIGN_CENTER
BOTTOM_MIDDLE_STYLE.font = FONT

MIDDLE_MIDDLE_BORDER = xlwt.Borders()
MIDDLE_MIDDLE_BORDER.top = xlwt.Borders.THIN
MIDDLE_MIDDLE_BORDER.left = xlwt.Borders.THIN
MIDDLE_MIDDLE_BORDER.right = xlwt.Borders.THIN
MIDDLE_MIDDLE_BORDER.bottom = xlwt.Borders.THIN
MIDDLE_MIDDLE_STYLE = xlwt.XFStyle()
MIDDLE_MIDDLE_STYLE.borders = MIDDLE_MIDDLE_BORDER
MIDDLE_MIDDLE_STYLE.alignment = ALIGN_CENTER
MIDDLE_MIDDLE_STYLE.font = FONT

# 備考
MEMO_TOP_LEFT_STYLE = deepcopy(TOP_LEFT_STYLE)
MEMO_TOP_LEFT_STYLE.font = xlwt.Font()
MEMO_TOP_LEFT_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_TOP_LEFT_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_TOP_MIDDLE_STYLE = deepcopy(TOP_MIDDLE_STYLE)
MEMO_TOP_MIDDLE_STYLE.font = xlwt.Font()
MEMO_TOP_MIDDLE_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_TOP_MIDDLE_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_TOP_MIDDLE_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_RIGHT_TOP_STYLE = deepcopy(RIGHT_TOP_STYLE)
MEMO_RIGHT_TOP_STYLE.font = xlwt.Font()
MEMO_RIGHT_TOP_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_RIGHT_TOP_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_LEFT_MIDDLE_STYLE = deepcopy(LEFT_MIDDLE_STYLE)
MEMO_LEFT_MIDDLE_STYLE.font = xlwt.Font()
MEMO_LEFT_MIDDLE_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_LEFT_MIDDLE_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_LEFT_MIDDLE_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_MIDDLE_MIDDLE_STYLE = deepcopy(MIDDLE_MIDDLE_STYLE)
MEMO_MIDDLE_MIDDLE_STYLE.font = xlwt.Font()
MEMO_MIDDLE_MIDDLE_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_MIDDLE_MIDDLE_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_MIDDLE_MIDDLE_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_MIDDLE_MIDDLE_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_RIGHT_MIDDLE_STYLE = deepcopy(RIGHT_MIDDLE_STYLE)
MEMO_RIGHT_MIDDLE_STYLE.font = xlwt.Font()
MEMO_RIGHT_MIDDLE_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_RIGHT_MIDDLE_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_RIGHT_MIDDLE_STYLE.borders.bottom = xlwt.Borders.NO_LINE

MEMO_LEFT_BOTTOM_STYLE = deepcopy(LEFT_BOTTOM_STYLE)
MEMO_LEFT_BOTTOM_STYLE.font = xlwt.Font()
MEMO_LEFT_BOTTOM_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_LEFT_BOTTOM_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_LEFT_BOTTOM_STYLE.borders.left = xlwt.Borders.THICK
MEMO_LEFT_BOTTOM_STYLE.borders.bottom = xlwt.Borders.THICK

MEMO_BOTTOM_MIDDLE_STYLE = deepcopy(BOTTOM_MIDDLE_STYLE)
MEMO_BOTTOM_MIDDLE_STYLE.font = xlwt.Font()
MEMO_BOTTOM_MIDDLE_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_BOTTOM_MIDDLE_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_BOTTOM_MIDDLE_STYLE.borders.right = xlwt.Borders.NO_LINE
MEMO_BOTTOM_MIDDLE_STYLE.borders.bottom = xlwt.Borders.THICK

MEMO_RIGHT_BOTTOM_STYLE = deepcopy(RIGHT_BOTTOM_STYLE)
MEMO_RIGHT_BOTTOM_STYLE.font = xlwt.Font()
MEMO_RIGHT_BOTTOM_STYLE.borders.top = xlwt.Borders.NO_LINE
MEMO_RIGHT_BOTTOM_STYLE.borders.left = xlwt.Borders.NO_LINE
MEMO_RIGHT_BOTTOM_STYLE.borders.right = xlwt.Borders.THICK
MEMO_RIGHT_BOTTOM_STYLE.borders.bottom = xlwt.Borders.THICK

PATTERN = xlwt.Pattern()
PATTERN.pattern = xlwt.Pattern.SOLID_PATTERN
PATTERN.pattern_fore_colour = 0x16
CANCELL_BORDER = xlwt.Borders()
CANCELL_BORDER.bottom = xlwt.Borders.DOUBLE
CANCELL_FONT = xlwt.Font()
CANCELL_FONT.bold = True
CANCELL_FONT.height = 12 * 20 # for 11point

CANCELL_STYLE = xlwt.XFStyle()
CANCELL_STYLE.pattern = PATTERN
CANCELL_STYLE.borders = CANCELL_BORDER
CANCELL_STYLE.font = CANCELL_FONT


WEEKDAY = {0: u'月',
           1: u'火',
           2: u'水',
           3: u'木',
           4: u'金',
           5: u'土',
           6: u'日',
}


class ScheduleBuilder(object):
    r"""ScheduleBuilder

    ScheduleBuilder is a object.
    Responsibility:
    """
    def __init__(self, sheet, row=0):
        r"""

        @Arguments:
        - `args`:
        - `kwargs`:
        """
        self._sheet = sheet
        self.row = row

    def insert_blank(self, ):
        r"""SUMMARY

        insert_blank()

        @Return:

        @Error:
        """
        self.row += 1

    def insert_title(self, title):
        r"""SUMMARY

        insert_title(title)

        @Arguments:
        - `title`:

        @Return:

        @Error:
        """
        self._sheet.write_merge(self.row, 1, 0, 5, title, TITLE_STYLE)
        self.row += 1

    def insert_subtitle(self, subtitle):
        r"""SUMMARY

        insert_subtitle(subtitle)

        @Arguments:
        - `subtitle`:

        @Return:

        @Error:
        """
        self._sheet.write(self.row, 0, subtitle, SUBTITLE_STYLE)
        self.row += 1

    def insert_header(self, ):
        r"""SUMMARY

        insert_header()

        @Return:

        @Error:
        """
        self._sheet.write(self.row, 0, u'日', TOP_LEFT_STYLE)
        self._sheet.write(self.row, 1, u'曜日', TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'集合時間', TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 3, u'行事開始', TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 4, u'行事', TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'参加者', RIGHT_TOP_STYLE)
        self.row += 1

    def insert_event(self, day, eventname):
        r"""SUMMARY

        insert_event()

        @Return:

        @Error:
        """
        self._sheet.write(self.row, 0, unicode(day.day), LEFT_BOTTOM_STYLE)
        self._sheet.write(
            self.row, 1, WEEKDAY.get(day.weekday()), BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'', BOTTOM_MIDDLE_STYLE) # 集合時間
        self._sheet.write(
            self.row, 3, unicode(day.strftime('%H:%M')), BOTTOM_MIDDLE_STYLE) # 開始時間
        self._sheet.write(self.row, 4, eventname, BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'',RIGHT_BOTTOM_STYLE)
        self.row += 1

    def insert_memo(self, ):
        r"""SUMMARY

        insert_memo()

        @Return:

        @Error:
        """
        self._sheet.write(self.row, 0, u'備考', MEMO_TOP_LEFT_STYLE)
        self._sheet.write(self.row, 1, u'', MEMO_TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'', MEMO_TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 3, u'', MEMO_TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 4, u'', MEMO_TOP_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'', MEMO_RIGHT_TOP_STYLE)
        self.row += 1
        self._sheet.write(self.row, 0, u'', MEMO_LEFT_MIDDLE_STYLE)
        self._sheet.write(self.row, 1, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 3, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 4, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'', MEMO_RIGHT_MIDDLE_STYLE)
        self.row += 1
        self._sheet.write(self.row, 0, u'', MEMO_LEFT_MIDDLE_STYLE)
        self._sheet.write(self.row, 1, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 3, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 4, u'', MEMO_MIDDLE_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'', MEMO_RIGHT_MIDDLE_STYLE)
        self.row += 1
        self._sheet.write(self.row, 0, u'', MEMO_LEFT_BOTTOM_STYLE)
        self._sheet.write(self.row, 1, u'', MEMO_BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 2, u'', MEMO_BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 3, u'', MEMO_BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 4, u'', MEMO_BOTTOM_MIDDLE_STYLE)
        self._sheet.write(self.row, 5, u'', MEMO_RIGHT_BOTTOM_STYLE)
        self.row += 1

    def insert_notify(self, ):
        r"""SUMMARY

        insert_notify()

        @Return:

        @Error:
        """
        self._sheet.write(
            self.row, 0, u'※　欠席される場合は、会長、副会長に必ず連絡下さい',
            CANCELL_STYLE)
        self._sheet.write(self.row, 1, u'', CANCELL_STYLE)
        self._sheet.write(self.row, 2, u'', CANCELL_STYLE)
        self._sheet.write(self.row, 3, u'', CANCELL_STYLE)
        self._sheet.write(self.row, 4, u'', CANCELL_STYLE)
        self._sheet.write(self.row, 5, u'', CANCELL_STYLE)



def get_heisei_fisical_year(day):
    r"""SUMMARY

    get_heisei_fisical_year(day)

    @Arguments:
    - `day`:

    @Return:

    @Error:
    """
    year = day.year
    if day.month in (1, 2, 3):
        year -= 1
    return year - 1988


UNICODE_NUMBER = {'0': u'０',
                  '1': u'１',
                  '2': u'２',
                  '3': u'３',
                  '4': u'４',
                  '5': u'５',
                  '6': u'６',
                  '7': u'７',
                  '8': u'８',
                  '9': u'９',
}


def num_to_wide_unicode(num):
    r"""SUMMARY

    num_to_wide_unicode(num)

    @Arguments:
    - `num`:

    @Return:

    @Error:
    """
    numstr = str(num)
    result = u''
    for char in numstr:
        if char not in '1234567890':
            continue
        result += UNICODE_NUMBER.get(char)
    return result


def align_column(sheet):
    r"""SUMMARY

    insert_schedule(sheet, month)

    @Arguments:
    - `sheet`:
    - `month`

    @Return:

    @Error:
    """
    sheet.col(0).width = 1280 # 日
    sheet.col(1).width = 1520 # 曜日
    sheet.col(2).width = 2640 # 集合時間
    sheet.col(3).width = 2640 # 行事開始
    sheet.col(4).width = 10800 # 行事
    sheet.col(5).width = 7100 # 参加者


def insert_month(builder, year, month):
    r"""SUMMARY

    insert_month(builder, year, month)

    @Arguments:
    - `sheet`:
    - `month`:

    @Return:

    @Error:
    """
    start = datetime.datetime(year, month, 1)
    _end = start + relativedelta(months=1)
    _end = _end - datetime.timedelta(1)
    end = datetime.datetime.combine(_end, datetime.time.max)
    yearstr = num_to_wide_unicode(get_heisei_fisical_year(
        datetime.datetime(year, month, 1)))
    monthstr = num_to_wide_unicode(month)
    builder.insert_blank()
    builder.insert_subtitle(u'平成{0}年{1}月'.format(yearstr, monthstr))
    builder.insert_header()
    for event in MainEvent.objects.between_events(
            start, end).confirmed().order_by('start'):
        builder.insert_event(event.start, event.summary)
    builder.insert_memo()
    builder.insert_blank()


def diff_month(d1, d2):
    return (d1.year - d2.year)*12 + d1.month - d2.month

def insert_schedules(builder, start, end):
    r"""SUMMARY

    insert_schedules()

    @Return:

    @Error:
    """
    diff = diff_month(end, start)
    current = start
    for _ in xrange(abs(diff) + 1):
        insert_month(builder, current.year, current.month)
        current = current + relativedelta(months=1)

def create_sheet(book, first, second):
    r"""SUMMARY

    create_sheet(first, second)

    @Arguments:
    - `first`:
    - `second`:

    @Return:

    @Error:
    """
    sheet = book.add_sheet(u'{},{}月'.format(first.month, second.month))

    sheet.col(0).width = 1425 # 日
    sheet.col(1).width = 1700 # 曜日
    sheet.col(2).width = 2750 # 集合時間
    sheet.col(3).width = 2750 # 行事開始
    sheet.col(4).width = 12000 # 行事
    sheet.col(5).width = 7875 # 参加者

    align_column(sheet)
    builder = ScheduleBuilder(sheet, 1)

    builder.insert_title(
        u'平成○年度 里自治会行事予定表 【{0}・{1}月】'
        .format(num_to_wide_unicode(first.month),
                num_to_wide_unicode(second.month)))
    insert_schedules(builder, first, second)
    builder.insert_blank()
    builder.insert_notify()

    maxrow = max(sheet.rows.keys())

    for row in range(0, maxrow + 1):
        sheet.row(row).height_mismatch = 1
        sheet.row(row).height = 360

    # head
    sheet.row(0).height_mismatch = 1
    sheet.row(0).height = 280
    sheet.row(1).height_mismatch = 1
    sheet.row(1).height = 550
    sheet.row(2).height_mismatch = 1
    sheet.row(2).height = 440
    sheet.row(3).height_mismatch = 1
    sheet.row(3).height = 390


def create_shedule_book(start, end):
    r"""SUMMARY

    tes()

    @Return:

    @Error:
    """
    book = xlwt.Workbook()
    create_sheet(book, start, end)
    fname = u'H{}_{}_{}月里自治会予定表_仮.xls'.format(
            get_heisei_fisical_year(datetime.datetime.now()),
            start.month, end.month)
    book.save(os.path.join(SCHEDULE_PATH, fname,))


@admin.site.register_view('genfiles', u'月別予定ファイル生成')
def shedule_view(request):
    r"""SUMMARY

    shedule_view(*args, **kwargs)

    @Arguments:
    - `args`:
    - `kwargs`:

    @Return:

    @Error:
    """
    cmd = SynccalCommand()
    cmd.handle(counts='10', main=True, start='', garbage=False, hall=False)
    if os.path.exists(SCHEDULE_PATH):
        shutil.rmtree(SCHEDULE_PATH, ignore_errors=True)
    if not os.path.exists(SCHEDULE_PATH):
        os.mkdir(SCHEDULE_PATH)
    now = datetime.datetime.now()
    current_month = datetime.datetime(now.year, now.month, 1)
    next_month = current_month + relativedelta(months=1)
    next_2month = next_month + relativedelta(months=1)
    create_shedule_book(current_month, next_month)
    create_shedule_book(next_month, next_2month)
    sleep(2)
    files = [os.path.basename(f) for f in
             glob.glob(os.path.join(SCHEDULE_PATH, '*.xls'))]
    context = {'filenames': files,}
    return render_to_response(
        'schedules/index.html', context,
        context_instance=RequestContext(request))



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# month_schedules_view.py ends here
