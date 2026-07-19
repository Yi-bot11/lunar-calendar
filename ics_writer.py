from datetime import datetime, timedelta
import pytz


TIMEZONE = "Asia/Shanghai"


def escape_text(text):
    """
    转义 ICS 特殊字符
    """
    text = str(text or "")

    return (
        text.replace("\\", "\\\\")
            .replace(";", "\\;")
            .replace(",", "\\,")
            .replace("\n", "\\n")
    )


def create_event(
    uid,
    event_date,
    title,
    description="",
    category=""
):
    """
    创建一个全天 ICS 事件
    """

    date_string = event_date.strftime("%Y%m%d")

    now = datetime.now(
        pytz.timezone(TIMEZONE)
    ).strftime("%Y%m%dT%H%M%S")

    event = f"""
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{now}
DTSTART;VALUE=DATE:{date_string}
DTEND;VALUE=DATE:{(event_date + timedelta(days=1)).strftime("%Y%m%d")}
SUMMARY:{escape_text(title)}
DESCRIPTION:{escape_text(description or title)}
CATEGORIES:{escape_text(category)}
BEGIN:VALARM
TRIGGER:-PT9H
ACTION:DISPLAY
DESCRIPTION:{escape_text(title)}
END:VALARM
END:VEVENT
"""

    return event.strip()


def create_calendar(events):
    """
    生成完整 ICS 文件
    """

    calendar = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Yi-bot11//Lunar Calendar//CN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-TIMEZONE:Asia/Shanghai",
        ""
    ]

    for index, event in enumerate(events):
        calendar.append(
create_event(
    uid=f"lunar-{index}@yi-bot11",
    event_date=event["date"],
    title=event["title"],
    description=event.get("description", ""),
    category=event.get("category", "")
)
        )
        calendar.append("")

    calendar.append(
        "END:VCALENDAR"
    )

    return "\n".join(calendar)


def save_calendar(filename, events):
    """
    保存 ICS 文件
    """

    content = create_calendar(events)

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(content)
