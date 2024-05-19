from dataclasses import dataclass, asdict
from model_sunset_sunrise import SunsetSunriseModel


@dataclass
class SettingsModel:
    date: str
    sunset_sunrise: SunsetSunriseModel
    email_me: str = ""
    smtp_server: str = ""
    smtp_password: str = ""

    @staticmethod
    def from_dict(obj: dict) -> 'SettingsModel':
        _date = str(obj.get("date"))
        _email_me = str(obj.get("email_me")).lower()
        _smtp_server = str(obj.get("smtp_server")).lower()
        _smtp_password = str(obj.get("smtp_password"))
        _sunset_sunrise = SunsetSunriseModel(**obj.get("sunset_sunrise"))
        return SettingsModel(date=_date,
                             sunset_sunrise=_sunset_sunrise,
                             email_me=_email_me,
                             smtp_server=_smtp_server,
                             smtp_password=_smtp_password)

    def as_dict(self):
        return asdict(self)
