import requests
from datetime import datetime, timedelta
import logging


logger = logging.getLogger(__name__)


def get_date_time(request):
    URL = 'https://api.taxideli.ru/test/gettime'
    WEEKDAYS_ENG_RUS = {
        'Sunday': 'Воскресенье',
        'Monday': 'Понедельник',
        'Tuesday': 'Вторник',
        'Wednesday': 'Среда',
        'Thursday': 'Четверг',
        'Friday': 'Пятница',
        'Saturday': 'Суббота'
    }
    r = requests.post(URL)
    if r.status_code != 200:
        logger.error(f'Error when trying to get the date, {r.status_code}')
        return ''
    result = (
            datetime.utcfromtimestamp(r.json()['dataAns']/1000) + timedelta(hours=3)
    ).strftime('%A, %d.%m.%Y %H:%M').split(',')
    return {
        'get_date_time': WEEKDAYS_ENG_RUS[result[0]] + ', ' + result[1]
    }
