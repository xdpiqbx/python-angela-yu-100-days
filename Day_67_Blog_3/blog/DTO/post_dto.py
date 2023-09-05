from dataclasses import dataclass, field
from datetime import date


@dataclass
class PostDTO:
    title: str
    subtitle: str
    body: str
    author: str
    id: int = None
    img_url: str = None
    date: str = field(default=date.today().strftime("%B %d, %Y"))  # September 05, 2023
