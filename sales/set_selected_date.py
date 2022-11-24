from .forms import YearMonthForm
import datetime

def set(request, jst, today):
    form    = YearMonthForm(request.GET)

    if form.is_valid():
        cleaned = form.clean()
        selected_date   = datetime.datetime(year=cleaned["year"], month=cleaned["month"], day=1, tzinfo=jst)
    else:
        selected_date   = datetime.datetime(year=today.year, month=today.month, day=1, tzinfo=jst)

    return selected_date