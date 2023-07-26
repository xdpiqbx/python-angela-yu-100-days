from datetime import datetime as dt

class DataValidator:
    def __init__(self):
        self.dt_now = dt.now()

    def validate_date(self, date: str) -> str:
        try:
            if self.dt_now < dt.strptime(date, "%d.%m.%Y") or not date:
                # if date from future I will return today date
                date = self.dt_now.strftime('%d.%m.%Y')
        except ValueError:
            # in this case I will return today date
            user_input = date
            date = self.dt_now.strftime('%d.%m.%Y')
            print(f"Your input [{user_input}] was incorrect and not equals format [DD.MM.YYYY].")
            print(f"Date was set to default: [{date}]")
        return date
