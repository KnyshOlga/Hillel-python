# def convert_seconds(seconds):
#     if seconds < 0 or seconds >= 8640000:
#         raise ValueError("Введене число не є допустимим. Воно має бути більше або дорівнювати 0 і менше ніж 8640000.")
#
#     days = seconds // (24 * 60 * 60)
#     seconds %= (24 * 60 * 60)
#     hours = seconds // (60 * 60)
#     seconds %= (60 * 60)
#     minutes = seconds // 60
#     seconds %= 60
#
#     days_str = "дні" if days > 1 else "день"
#     hours_str = f"{hours:02d}".zfill(2) if hours < 10 else f"{hours:02d}"
#     minutes_str = f"{minutes:02d}".zfill(2) if minutes < 10 else f"{minutes:02d}"
#     seconds_str = f"{seconds:02d}".zfill(2) if seconds < 10 else f"{seconds:02d}"
#
#     return f"{days} {days_str}, {hours_str}:{minutes_str}:{seconds_str}"
#
#
# try:
#     seconds = int(input("Введіть кількість секунд: "))
#     print(convert_seconds(seconds))
# except ValueError as e:
#     print(e)


def convert_seconds(seconds):
    if seconds < 0 or seconds >= 8640000:
        raise ValueError

    days = seconds // (24 * 60 * 60)
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60

    days_str = "днів" if days > 1 else "день"
    hours_str = f"0{hours:02d}" if hours < 10 else f"{hours:02d}"
    minutes_str = f"0{minutes:02d}" if minutes < 10 else f"{minutes:02d}"
    seconds_str = f"0{seconds:02d}" if seconds < 10 else f"{seconds:02d}"

    return f"{days} {days_str}, {hours_str}:{minutes_str}:{seconds_str}"


try:
    seconds = int(input("Введіть кількість секунд: "))
    print(convert_seconds(seconds))
except ValueError as e:
    print(e)
