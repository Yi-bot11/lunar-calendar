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


def lunar_title(info):
    """
    根据农历信息生成标题
    """
    if info["day"] == 1:
        return f"🌑 农历{info['month_name']}月初一"

    if info["day"] == 15:
        return f"🌕 农历{info['month_name']}月十五"

    return "农历日期"
    
def get_tao_events(current, info):

    festivals = TAO_FESTIVALS.get(
        (info["month"], info["day"]),
        []
    )

    events = []

    for festival in festivals:
        events.append{
    "date": current,
    "title": f"☯ {festival['name']}",
    "description": festival.get("description", ""),
    "category": "道教"
}

    return events
def generate_lunar_dates(start_year, end_year):
    """
    生成指定年份范围内所有农历初一、十五和道教节日
    """
    results = []

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            for day in range(1, 32):

                try:
                    current = date(year, month, day)

                    # 只计算一次农历信息
                    info = get_lunar_day(
                        current.year,
                        current.month,
                        current.day
                    )

                    # 初一、十五
                    if info["day"] in (1, 15):
                        results.append({
                            "date": current,
                            "title": lunar_title(info)
                        })

                    # 道教节日
                    results.extend(
                        get_tao_events(current, info)
                    )

                except ValueError:
                    continue

    return results
