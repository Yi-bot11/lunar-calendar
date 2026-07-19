from lunar_python import Solar
from datetime import date
from tao_festivals import TAO_FESTIVALS

def get_lunar_day(year, month, day):
    """
    返回指定公历日期对应的农历信息
    """
    solar = Solar.fromYmd(year, month, day)
    lunar = solar.getLunar()

    return {
        "month": lunar.getMonth(),
        "day": lunar.getDay(),
        "month_name": lunar.getMonthInChinese(),
        "day_name": lunar.getDayInChinese(),
    }


def is_lunar_first_or_fifteenth(year, month, day):
    """
    判断是否为农历初一或十五
    """
    info = get_lunar_day(year, month, day)

    return info["day"] in (1, 15)


def lunar_title(year, month, day):
    """
    生成日历事件标题
    """
    info = get_lunar_day(year, month, day)

    if info["day"] == 1:
        return f"🌑 农历{info['month_name']}月初一"

    if info["day"] == 15:
        return f"🌕 农历{info['month_name']}月十五"

    return "农历日期"
    
def get_tao_events(current):
    info = get_lunar_day(
        current.year,
        current.month,
        current.day
    )

    festivals = TAO_FESTIVALS.get(
        (info["month"], info["day"]),
        []
    )

    events = []

    for festival in festivals:
        print(
            "发现道教节日:",
            current,
            festival["name"]
        )

        events.append({
            "date": current,
            "title": f"☯ {festival['name']}"
        })

    return events
