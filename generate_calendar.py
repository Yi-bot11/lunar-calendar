from datetime import datetime
import os

from lunar_utils import generate_lunar_dates
from ics_writer import save_calendar


START_YEAR = datetime.now().year
END_YEAR = START_YEAR + 10

OUTPUT_FILE = "docs/lunar.ics"


def main():

    print("开始生成农历日历...")

    events = generate_lunar_dates(
        START_YEAR,
        END_YEAR
    )

    print(
        f"生成事件数量: {len(events)}"
    )

    os.makedirs(
        "docs",
        exist_ok=True
    )

    save_calendar(
        OUTPUT_FILE,
        events
    )

    print(
        f"日历已生成: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()
