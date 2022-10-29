import datetime

from .models import AC

def create_calender(year, month):

    dt = datetime.date(year, month, 1)

    calender    = []
    week        = []

    if dt.weekday() != 6: # dt.weekday()が6なら日曜日
        week    = [ {"day": ""} for i in range(dt.weekday()+1) ]

    while True:
        week.append({"day": dt.day})
        dt += datetime.timedelta(days=1)

        # 週末になるたびにweekに追加する
        if dt.weekday() == 6:
            calender.append(week)
            week = []

        # 月が変わったら終了
        if month != dt.month:
            if dt.weekday() != 6:
                for i in range(6-dt.weekday()):
                    week.append({"day": ""})

                calender.append(week)
            
            break

    return calender


def create_years(request, selected_date, today):

    if request.user.is_teacher:
        oldest  = AC.objects.all().order_by( "ac_date").first()
        newest  = AC.objects.all().order_by("-ac_date").first()
    else:
        oldest  = AC.objects.filter(user=request.user.id).order_by( "ac_date").first()
        newest  = AC.objects.filter(user=request.user.id).order_by("-ac_date").first()

    if oldest and newest:
        if selected_date < oldest.ac_date:
            years = [ i for i in range(selected_date.year , newest.ac_date.year+1 )]
        elif newest.ac_date < selected_date:
            years = [ i for i in range(oldest.ac_date.year, selected_date.year+1  )]
        else:
            years = [ i for i in range(oldest.ac_date.year, newest.ac_date.year+1 )]
    else:
        if selected_date < today:
            years = [ i for i in range(selected_date.year, today.year+1)]
        else:
            years = [ i for i in range(today.year, selected_date.year+1)]
        
    return years


def create_months(selected_date):

    if selected_date.month == 12:
        next_month   = datetime.date( year=selected_date.year+1 , month=1                     , day=1 )
        last_month   = datetime.date( year=selected_date.year   , month=selected_date.month-1 , day=1 )
    elif selected_date.month == 1:
        next_month   = datetime.date( year=selected_date.year   , month=selected_date.month+1 , day=1 )
        last_month   = datetime.date( year=selected_date.year-1 , month=12 ,                    day=1 )
    else:
        next_month   = datetime.date( year=selected_date.year   , month=selected_date.month+1 , day=1 )
        last_month   = datetime.date( year=selected_date.year   , month=selected_date.month-1 , day=1 )
        
    return next_month, last_month
