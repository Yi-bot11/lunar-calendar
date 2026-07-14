from lunar_python import Solar
from datetime import date


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


def generate_lunar_dates(start_year, end_year):
    """
    生成指定年份范围内所有农历初一和十五
    """

    results = []

    for year in range(start_year, end_year + 1):

        for month in range(1, 13):

            # 遍历每个月所有可能日期
            for day in range(1, 32):

                try:
                    current = date(year, month, day)

                    if is_lunar_first_or_fifteenth(
                        current.year,
                        current.month,
                        current.day
                    ):
                        results.append(
                            {
                                "date": current,
                                "title": lunar_title(
                                    current.year,
                                    current.month,
                                    current.day
                                ),
                            }
                        )

                except ValueError:
                    continue

    return results
