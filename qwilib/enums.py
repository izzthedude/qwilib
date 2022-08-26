import os
from pathlib import Path


class Paths:
    PROJECT_ROOT = Path(__file__).parent
    RESOURCES = Path(PROJECT_ROOT / "resources")


class Icons:
    DIR = os.path.join(str(Paths.RESOURCES), "icons")

    APP_LOGO = os.path.join(DIR, "icons8-lemon-32.png")
    DEFAULT_PROFILE = os.path.join(DIR, "default_account_circle.svg")
    ADD_DEFAULT = os.path.join(DIR, "default_add.svg")
    FILTER_DEFAULT = os.path.join(DIR, "default_filter.svg")
    REFRESH_DEFAULT = os.path.join(DIR, "default_refresh.svg")
    COLLAPSE_DEFAULT = os.path.join(DIR, "default_double_arrow_down.svg")
    NOTIFICATION_DEFAULT = os.path.join(DIR, "default_notifications.svg")
    INFO_DEFAULT = os.path.join(DIR, "default_info.svg")
    GRIDVIEW_DEFAULT = os.path.join(DIR, "default_view_grid.svg")
    LISTVIEW_DEFAULT = os.path.join(DIR, "default_view_list.svg")


class Styles:
    DIR = os.path.join(str(Paths.RESOURCES), "styles")

    LIGHT = os.path.join(DIR, "style_light.css")
    DARK = os.path.join(DIR, "style_dark.css")


class IconSizes:
    XSMALL = 10
    SMALL = 20
    MEDIUM = 35
    LARGE = 50
    XLARGE = 65


class PosterSizes:
    SMALL = 160
    MEDIUM = 210
    LARGE = 260
