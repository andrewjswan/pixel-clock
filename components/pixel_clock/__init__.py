"""PixelClock ex EspHoMaTriX component for ESPHome."""

import io
import json
import logging
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import esphome.codegen as cg
import esphome.components.image as espImage  # noqa: N812
import esphome.config_validation as cv
import requests
from esphome import automation, core
from esphome.components import display, font, graph, time
from esphome.components.image import CONF_CHROMA_KEY, IMAGE_TYPE
from esphome.const import (
    CONF_BRIGHTNESS,
    CONF_COLOR_CORRECT,
    CONF_FILE,
    CONF_ID,
    CONF_RAW_DATA_ID,
    CONF_RESIZE,
    CONF_TRIGGER_ID,
)
from esphome.cpp_generator import RawExpression
from PIL import Image

_LOGGER = logging.getLogger(__name__)

CODEOWNERS = ["@andrewjswan", "@lubeda"]

DEPENDENCIES = ["display", "light"]

AUTO_LOAD = ["json", "image", "animation", "web_server_base"]

_LOGGER.info("Load Pixel-Clock component https://github.com/andrewjswan/pixel-clock")
_LOGGER.info("If you like the Pixel-Clock, you can support it with a star ⭐ on GitHub.")

pixel_clock_ns = cg.esphome_ns.namespace("pixel_clock")
PixelClock_ = pixel_clock_ns.class_("PixelClock", cg.Component)
Icons_ = pixel_clock_ns.class_("PixelClock_Icon")

MAXFRAMES = 110
MAXICONS = 100
ICONWIDTH = 8
ICONHEIGHT = 8

CONF_URL = "url"
CONF_CLOCKINTERVAL = "clock_interval"
CONF_ALWAYS_SHOW_RLINDICATORS = "always_show_rl_indicators"
CONF_TIMECOMPONENT = "time_component"
CONF_LAMEID = "lameid"
CONF_RGB565ARRAY = "str565"
CONF_LIFETIME = "lifetime"
CONF_ICONS = "icons"
CONF_SHOWDOW = "show_dow"
CONF_RTL = "rtl"
CONF_VERTICAL = "vertical_scroll"
CONF_CLOCK = "advanced_clock"
CONF_FLIP_FLOP = "flip_flop_clock"
CONF_FLIP_FLOP_SPEED = "flip_flop_speed"
CONF_BITMAP = "advanced_bitmap"
CONF_BOOTLOGO = "boot_logo"
CONF_BOOTLOGOMODE = "boot_logo_mode"
CONF_FRAMEDURATION = "frame_duration"
CONF_SCROLLCOUNT = "scroll_count"
CONF_MATRIXCOMPONENT = "matrix_component"
CONF_HTML = "icons2html"
CONF_CACHE = "iconscache"
CONF_SCROLLINTERVAL = "scroll_interval"
CONF_BLENDSTEPS = "blend_steps"
CONF_RAINBOWINTERVAL = "rainbow_interval"
CONF_RAINBOWSHIMMER = "rainbow_shimmer"
CONF_MULTICOLOR_TEXT = "multicolor_text"
CONF_FRAMEINTERVAL = "frame_interval"
CONF_DEFAULT_FONT_ID = "default_font_id"
CONF_DEFAULT_FONT = "default_font"
CONF_DEFAULT_FONT_XOFFSET = "default_font_xoffset"
CONF_DEFAULT_FONT_YOFFSET = "default_font_yoffset"
CONF_SPECIAL_FONT_ID = "special_font_id"
CONF_SPECIAL_FONT_XOFFSET = "special_font_xoffset"
CONF_SPECIAL_FONT_YOFFSET = "special_font_yoffset"
CONF_PINGPONG = "pingpong"
CONF_TIME_FORMAT = "time_format"
CONF_TIME_FORMAT_BIG = "time_format_big"
CONF_DATE_FORMAT = "date_format"
CONF_DATE_FORMAT_BIG = "date_format_big"
CONF_ON_START_RUNNING = "on_start_running"
CONF_ON_EMPTY_QUEUE = "on_empty_queue"
CONF_ON_NEXT_SCREEN = "on_next_screen"
CONF_ON_NEXT_CLOCK = "on_next_clock"
CONF_ON_ICON_ERROR = "on_icon_error"
CONF_ON_ADD_SCREEN = "on_add_screen"
CONF_ON_SHOW_DISPLAY = "on_show_display"
CONF_ON_NIGHT_MODE = "on_night_mode"
CONF_WEEKDAYTEXT = "weekdays"
CONF_REPLACE_TIME_DATE_FROM = "replace_time_date_from"
CONF_REPLACE_TIME_DATE_TO = "replace_time_date_to"
CONF_ON_EXPIRED_SCREEN = "on_expired_screen"
CONF_SHOW_SECONDS = "show_seconds"
CONF_SCROLL_SMALL_TEXT = "scroll_small_text"
CONF_WEEK_START_MONDAY = "week_start_monday"
CONF_ICON = "icon_name"
CONF_TEXT = "text"
CONF_GRAPH = "display_graph"
CONF_NIGHT_MODE_SCREENS = "night_mode_screens"
DEFAULT_NIGHT_MODE_SCREENS = [2, 3, 16]
CONF_ICON_INDICATOR_SCREENS = "icon_indicator_screens"
DEFAULT_ICON_INDICATOR_SCREENS = [15, 18]
DEF_TYPE = "RGB565"
CONF_RCINDICATOR = "right_center_indicator"
CONF_RBINDICATOR = "right_bottom_indicator"
CONF_LTINDICATOR = "left_top_indicator"
CONF_LCINDICATOR = "left_center_indicator"
CONF_LBINDICATOR = "left_bottom_indicator"
CONF_ICINDICATOR = "icon_indicator"
CONF_GAUGE = "gauge"
CONF_FIRE = "fire_screen"

SVG_ICONSTART = '<svg width="80px" height="80px" viewBox="0 0 80 80">'
SVG_FULL_SCREEN_START = '<svg width="320px" height="80px" viewBox="0 0 320 80">'
SVG_END = "</svg>"

StartRunningTrigger = pixel_clock_ns.class_(
    "PixelClockStartRunningTrigger",
    automation.Trigger.template(),
)

EmptyQueueTrigger = pixel_clock_ns.class_(
    "PixelClockEmptyQueueTrigger",
    automation.Trigger.template(),
)

NextScreenTrigger = pixel_clock_ns.class_(
    "PixelClockNextScreenTrigger",
    automation.Trigger.template(cg.std_string, cg.std_string),
)

IconErrorTrigger = pixel_clock_ns.class_(
    "PixelClockIconErrorTrigger",
    automation.Trigger.template(cg.std_string),
)

ExpiredScreenTrigger = pixel_clock_ns.class_(
    "PixelClockExpiredScreenTrigger",
    automation.Trigger.template(cg.std_string, cg.std_string),
)

NextClockTrigger = pixel_clock_ns.class_(
    "PixelClockNextClockTrigger",
    automation.Trigger.template(),
)

AddScreenTrigger = pixel_clock_ns.class_(
    "PixelClockAddScreenTrigger",
    automation.Trigger.template(cg.std_string, cg.uint8),
)

ShowDisplayTrigger = pixel_clock_ns.class_(
    "PixelClockShowDisplayTrigger",
    automation.Trigger.template(cg.bool_),
)

NightModeTrigger = pixel_clock_ns.class_(
    "PixelClockNightModeTrigger",
    automation.Trigger.template(cg.bool_),
)

PIXEL_CLOCK_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_ID): cv.declare_id(PixelClock_),
        cv.Required(CONF_TIMECOMPONENT): cv.use_id(time),
        cv.Required(CONF_MATRIXCOMPONENT): cv.use_id(display),
        cv.Required(CONF_DEFAULT_FONT_ID): cv.use_id(font),
        cv.Required(CONF_SPECIAL_FONT_ID): cv.use_id(font),
        cv.Optional(CONF_GRAPH): cv.use_id(graph),
        cv.Optional(CONF_CLOCKINTERVAL, default="0"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_HTML, default=False): cv.boolean,
        cv.Optional(CONF_CACHE, default=False): cv.boolean,
        cv.Optional(CONF_RTL, default=False): cv.boolean,
        cv.Optional(CONF_VERTICAL, default=False): cv.boolean,
        cv.Optional(CONF_CLOCK, default=False): cv.boolean,
        cv.Optional(CONF_FLIP_FLOP, default=False): cv.boolean,
        cv.Optional(CONF_FLIP_FLOP_SPEED, default="2"): cv.templatable(cv.int_range(min=1, max=10)),
        cv.Optional(CONF_BITMAP, default=False): cv.boolean,
        cv.Optional(CONF_BOOTLOGO): cv.string,
        cv.Optional(CONF_BOOTLOGOMODE, default="0"): cv.templatable(cv.int_range(min=0, max=7)),
        cv.Optional(CONF_SHOW_SECONDS, default=False): cv.boolean,
        cv.Optional(CONF_WEEK_START_MONDAY, default=True): cv.boolean,
        cv.Optional(CONF_SHOWDOW, default=True): cv.boolean,
        cv.Optional(CONF_SCROLL_SMALL_TEXT, default=False): cv.boolean,
        cv.Optional(CONF_TIME_FORMAT, default="%H:%M"): cv.string,
        cv.Optional(CONF_TIME_FORMAT_BIG, default="%H:%M:%S"): cv.string,
        cv.Optional(CONF_WEEKDAYTEXT, default="SUMOTUWETHFRSA"): cv.string,
        cv.Optional(CONF_REPLACE_TIME_DATE_FROM, default=""): cv.string,
        cv.Optional(CONF_REPLACE_TIME_DATE_TO, default=""): cv.string,
        cv.Optional(CONF_ALWAYS_SHOW_RLINDICATORS, default=False): cv.boolean,
        cv.Optional(CONF_DATE_FORMAT, default="%d.%m."): cv.string,
        cv.Optional(CONF_DATE_FORMAT_BIG, default="%d.%m."): cv.string,
        cv.Optional(CONF_DEFAULT_FONT_XOFFSET, default="1"): cv.templatable(
            cv.int_range(min=-32, max=32),
        ),
        cv.Optional(CONF_DEFAULT_FONT_YOFFSET, default="6"): cv.templatable(
            cv.int_range(min=-32, max=32),
        ),
        cv.Optional(CONF_SPECIAL_FONT_XOFFSET, default="1"): cv.templatable(
            cv.int_range(min=-32, max=32),
        ),
        cv.Optional(CONF_SPECIAL_FONT_YOFFSET, default="6"): cv.templatable(
            cv.int_range(min=-32, max=32),
        ),
        cv.Optional(CONF_SCROLLINTERVAL, default="80"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_BLENDSTEPS, default="0"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_RAINBOWINTERVAL, default="32"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_RAINBOWSHIMMER, default=False): cv.boolean,
        cv.Optional(CONF_MULTICOLOR_TEXT, default=False): cv.boolean,
        cv.Optional(CONF_SCROLLCOUNT, default="2"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_FRAMEINTERVAL, default="192"): cv.templatable(cv.positive_int),
        cv.Optional(CONF_BRIGHTNESS, default=80): cv.templatable(cv.int_range(min=0, max=255)),
        cv.Optional(CONF_COLOR_CORRECT): cv.All([cv.percentage], cv.Length(min=3, max=3)),
        cv.Optional(CONF_RCINDICATOR, default=False): cv.boolean,
        cv.Optional(CONF_RBINDICATOR, default=True): cv.boolean,
        cv.Optional(CONF_LTINDICATOR, default=False): cv.boolean,
        cv.Optional(CONF_LCINDICATOR, default=False): cv.boolean,
        cv.Optional(CONF_LBINDICATOR, default=True): cv.boolean,
        cv.Optional(CONF_ICINDICATOR, default=True): cv.boolean,
        cv.Optional(CONF_GAUGE, default=True): cv.boolean,
        cv.Optional(CONF_FIRE, default=True): cv.boolean,
        cv.Optional(CONF_NIGHT_MODE_SCREENS, default=DEFAULT_NIGHT_MODE_SCREENS): cv.All(
            cv.ensure_list(
                cv.one_of(
                    1,
                    2,
                    3,
                    4,
                    5,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                ),
            ),
            cv.Length(min=1, max=5),
        ),
        cv.Optional(CONF_ICON_INDICATOR_SCREENS, default=DEFAULT_ICON_INDICATOR_SCREENS): cv.All(
            cv.ensure_list(
                cv.one_of(
                    1,
                    2,
                    3,
                    4,
                    5,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26,
                ),
            ),
            cv.Length(min=1, max=5),
        ),
        cv.Required(CONF_ICONS): cv.All(
            cv.ensure_list(
                {
                    cv.Required(CONF_ID): cv.declare_id(Icons_),
                    cv.Exclusive(CONF_FILE, "uri"): cv.file_,
                    cv.Exclusive(CONF_URL, "uri"): cv.url,
                    cv.Exclusive(CONF_LAMEID, "uri"): cv.string,
                    cv.Exclusive(CONF_RGB565ARRAY, "uri"): cv.string,
                    cv.Optional(CONF_RESIZE): cv.dimensions,
                    cv.Optional(CONF_FRAMEDURATION, default="0"): cv.templatable(cv.positive_int),
                    cv.Optional(CONF_PINGPONG, default=False): cv.boolean,
                    cv.GenerateID(CONF_RAW_DATA_ID): cv.declare_id(cg.uint8),
                },
            ),
            cv.Length(max=MAXICONS),
        ),
        cv.Optional(CONF_ON_NEXT_SCREEN): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(NextScreenTrigger),
            },
        ),
        cv.Optional(CONF_ON_EMPTY_QUEUE): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(EmptyQueueTrigger),
            },
        ),
        cv.Optional(CONF_ON_ICON_ERROR): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(IconErrorTrigger),
            },
        ),
        cv.Optional(CONF_ON_ADD_SCREEN): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(AddScreenTrigger),
            },
        ),
        cv.Optional(CONF_ON_NEXT_CLOCK): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(NextClockTrigger),
            },
        ),
        cv.Optional(CONF_ON_START_RUNNING): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(StartRunningTrigger),
            },
        ),
        cv.Optional(CONF_ON_EXPIRED_SCREEN): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(ExpiredScreenTrigger),
            },
        ),
        cv.Optional(CONF_ON_SHOW_DISPLAY): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(ShowDisplayTrigger),
            },
        ),
        cv.Optional(CONF_ON_NIGHT_MODE): automation.validate_automation(
            {
                cv.GenerateID(CONF_TRIGGER_ID): cv.declare_id(NightModeTrigger),
            },
        ),
    },
)

CONFIG_SCHEMA = cv.All(PIXEL_CLOCK_SCHEMA)


def rgb565_svg(x: int, y: int, r: int, g: int, b: int, a: int) -> str:  # noqa: PLR0913, PLR0917
    """Convert an RGB565 pixel with alpha to an SVG rectangle element."""
    red = (r << 3) | (r >> 2)
    green = (g << 2) | (g >> 4)
    blue = (b << 3) | (b >> 2)
    return (
        f'<rect style="fill:rgb({red},{green},{blue});'
        f'fill-opacity:{(a / 255)};" x="{x * 10}" y="{y * 10}" width="10" height="10"/>'
    )


def rgb565_888(v565: int) -> tuple[int, int, int]:
    """Convert a 16-bit RGB565 integer value to an 8-bit RGB888 tuple."""
    b = ((v565) & 0x001F) << 3
    g = ((v565) & 0x07E0) >> 3
    r = ((v565) & 0xF800) >> 8
    return (r, g, b)


def open_image_file(path: Path | str) -> Image.Image:
    """Open an image file from disk and raise EsphomeError on failure."""
    try:
        return Image.open(path)
    except OSError as e:
        msg = f"  Icons: Could not load image file {path}: {e}"
        raise core.EsphomeError(msg) from e


async def to_code(config: dict[str, Any]) -> None:  # noqa: C901, PLR0912, PLR0915
    """Generate C++ configuration code for the PixelClock component."""
    var = cg.new_Pvariable(config[CONF_ID])

    _LOGGER.info("Preparing icons, this may take some seconds.")

    html_string = f"<html><head><title>{core.CORE.config_path}</title></head>"
    html_string += """\
    <style>
    svg { padding-top: 2x; padding-right: 2px; padding-bottom: 2px; padding-left: 2px; }
    body { background-color: black; color: white; }
    </style><body>\
"""

    cg.add_define("MAXICONS", MAXICONS)

    yaml_string = ""
    for conf in config[CONF_ICONS]:
        if CONF_FILE in conf:
            path = core.CORE.relative_config_path(conf[CONF_FILE])
            image = open_image_file(path)

        elif CONF_LAMEID in conf:
            path = core.CORE.relative_config_path(".cache/icons/lameid/" + conf[CONF_LAMEID])
            if config[CONF_CACHE] and Path(path).is_file():
                image = open_image_file(path)
                _LOGGER.info("  Icons: Load %s from cache.", conf[CONF_LAMEID])
            else:
                r = requests.get(
                    "https://developer.lametric.com/content/apps/icon_thumbs/" + conf[CONF_LAMEID],
                    headers={
                        "Cache-Control": "no-cache, no-store, must-revalidate",
                        "Pragma": "no-cache",
                    },
                    timeout=4.0,
                )
                if r.status_code != requests.codes.ok:
                    msg = (
                        f"  Icons: Could not download image file {conf[CONF_LAMEID]}: "
                        f"{conf[CONF_ID]}"
                    )
                    raise core.EsphomeError(msg)
                image = Image.open(io.BytesIO(r.content))

                if config[CONF_CACHE]:
                    cache_path = Path(path)
                    cache_path.parent.mkdir(parents=True, exist_ok=True)
                    with cache_path.open("wb") as f:
                        f.write(r.content)
                    _LOGGER.info("  Icons: Save %s to cache.", conf[CONF_LAMEID])

        elif CONF_URL in conf:
            a = urlparse(conf[CONF_URL])
            path = core.CORE.relative_config_path(".cache/icons/url/" + Path(a.path).name)
            if config[CONF_CACHE] and Path(path).is_file():
                image = open_image_file(path)
                _LOGGER.info("  Icons: Load %s from cache.", conf[CONF_URL])
            else:
                r = requests.get(
                    conf[CONF_URL],
                    headers={
                        "Cache-Control": "no-cache, no-store, must-revalidate",
                        "Pragma": "no-cache",
                    },
                    timeout=4.0,
                )
                if r.status_code != requests.codes.ok:
                    msg = (
                        f"  Icons: Could not download image file {conf[CONF_URL]}: {conf[CONF_ID]}"
                    )
                    raise core.EsphomeError(msg)
                image = Image.open(io.BytesIO(r.content))

                if config[CONF_CACHE]:
                    cache_path = Path(path)
                    cache_path.parent.mkdir(parents=True, exist_ok=True)
                    with cache_path.open("wb") as f:
                        f.write(r.content)
                    _LOGGER.info("  Icons: Save %s to cache.", conf[CONF_URL])

        elif CONF_RGB565ARRAY in conf:
            r = list(json.loads(conf[CONF_RGB565ARRAY]))
            if len(r) == 64:
                image = Image.new("RGB", [8, 8])
                image.putdata([rgb565_888(v) for v in r])
            elif len(r) == 256:
                image = Image.new("RGB", [32, 8])
                image.putdata([rgb565_888(v) for v in r])

        width, height = image.size

        if CONF_RESIZE in conf:
            new_width_max, new_height_max = conf[CONF_RESIZE]
            ratio = min(new_width_max / width, new_height_max / height)
            width, height = int(width * ratio), int(height * ratio)

        if hasattr(image, "n_frames"):
            frames = min(image.n_frames, MAXFRAMES)
            _LOGGER.info("Animation %s with %s frame(s)", conf[CONF_ID], frames)
        else:
            frames = 1

        if height != ICONHEIGHT or width not in (ICONWIDTH, 4 * ICONWIDTH):
            _LOGGER.warning("Icon wrong size valid 8x8 or 32x8: %s skipped!", conf[CONF_ID])
        else:
            if conf[CONF_FRAMEDURATION] == 0:
                try:
                    duration = image.info["duration"]
                except KeyError:
                    duration = config[CONF_FRAMEINTERVAL]
            else:
                duration = conf[CONF_FRAMEDURATION]

            yaml_string += f'"{conf[CONF_ID]}",'

            dither = Image.Dither.NONE
            transparency = CONF_CHROMA_KEY
            invert_alpha = False

            total_rows = height * frames
            encoder = IMAGE_TYPE[DEF_TYPE](
                width,
                total_rows,
                transparency,
                dither,
                invert_alpha,
            )
            encoder.set_big_endian(False)
            for frame_index in range(frames):
                image.seek(frame_index)
                pixels = encoder.convert(image.resize((width, height)), path).getdata()
                for row in range(height):
                    for col in range(width):
                        encoder.encode(pixels[row * width + col])
                    encoder.end_row()

            rhs = [core.HexInt(x) for x in encoder.data]
            prog_arr = cg.progmem_array(conf[CONF_RAW_DATA_ID], rhs)

            image_type = espImage.get_image_type_enum(DEF_TYPE)
            trans_value = espImage.get_transparency_enum(encoder.transparency)

            _LOGGER.debug("  Icons: Icon %s %s", conf[CONF_ID], rhs)

            cg.new_Pvariable(
                conf[CONF_ID],
                prog_arr,
                width,
                height,
                frames,
                image_type,
                str(conf[CONF_ID]),
                conf[CONF_PINGPONG],
                duration,
                trans_value,
            )
            cg.add(var.add_icon(RawExpression(str(conf[CONF_ID]))))

            html_string += (
                f"<br/>Icon: <b>{conf[CONF_ID]}</b>&nbsp;-&nbsp;({duration} ms):<br/><br/>"
            )
            html_string += f"<div id={conf[CONF_ID]}>"
            for frame_index in range(frames):
                image.seek(frame_index)
                frame = image.convert("RGBA")

                if CONF_RESIZE in conf:
                    frame = frame.resize([width, height])

                pixels = list(frame.getdata())

                # width, height = image.size  # noqa: ERA001
                if width == 8:
                    html_string += SVG_ICONSTART
                else:
                    html_string += SVG_FULL_SCREEN_START
                for i, pix in enumerate(pixels):
                    r, g, b, a = pix
                    r = r >> 3
                    g = g >> 2
                    b = b >> 3

                    x = i % width
                    y = i // width

                    html_string += rgb565_svg(x, y, r, g, b, a)
                html_string += SVG_END
            html_string += "</div>"
    html_string += "</body></html>"

    if config[CONF_HTML]:
        htmlfn = str(core.CORE.config_path).replace(".yaml", "") + ".html"
        try:
            with Path(htmlfn).open("w", encoding="utf-8") as f:
                f.write(html_string)
            _LOGGER.info("PixelClock: Wrote HTML file with icon preview: %s", htmlfn)
        except OSError:
            _LOGGER.warning("PixelClock: Error writing HTML file: %s", htmlfn)

    _LOGGER.info("List of icons for e.g. Blueprint:\n\n\r[%s]\n", yaml_string)

    disp = await cg.get_variable(config[CONF_MATRIXCOMPONENT])
    cg.add(var.set_display(disp))

    if CONF_GRAPH in config:
        pixel_clock_graph = await cg.get_variable(config[CONF_GRAPH])
        cg.add(var.set_graph(pixel_clock_graph))

    pixel_clock_time = await cg.get_variable(config[CONF_TIMECOMPONENT])
    cg.add(var.set_clock(pixel_clock_time))

    f = await cg.get_variable(config[CONF_DEFAULT_FONT_ID])
    cg.add(var.set_default_font(f))

    f = await cg.get_variable(config[CONF_SPECIAL_FONT_ID])
    cg.add(var.set_special_font(f))

    cg.add(var.set_brightness(config[CONF_BRIGHTNESS]))
    if (color_correct := config.get(CONF_COLOR_CORRECT)) is not None:
        r, g, b = color_correct
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_R", round(r, 4))
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_G", round(g, 4))
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_B", round(b, 4))
        _LOGGER.info(
            "[X] Color Correct: R=%d%%, G=%d%%, B=%d%%",
            round(r * 100),
            round(g * 100),
            round(b * 100),
        )
    else:
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_R", 1.0)
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_G", 1.0)
        cg.add_define("PIXEL_CLOCK_COLOR_CORRECT_B", 1.0)

    if config[CONF_ALWAYS_SHOW_RLINDICATORS]:
        cg.add_define("PIXEL_CLOCK_ALWAYS_SHOW_RLINDICATORS")

    if config[CONF_WEEKDAYTEXT]:
        if (len(config[CONF_WEEKDAYTEXT])) == 7:
            cg.add(var.set_weekday_char_count(7))

        elif (len(config[CONF_WEEKDAYTEXT])) == 14:
            cg.add(var.set_weekday_char_count(14))
        else:
            _LOGGER.warning(
                "weekdays: must be 7 or 14 characters... "
                "your config may have unpredictable results!",
            )
            cg.add(var.set_weekday_char_count(len(config[CONF_WEEKDAYTEXT])))

    cg.add_define("PIXEL_CLOCK_WEEKDAYTEXT", config[CONF_WEEKDAYTEXT])
    cg.add_define("PIXEL_CLOCK_REPLACE_TIME_DATE_TO", config[CONF_REPLACE_TIME_DATE_TO])
    cg.add_define("PIXEL_CLOCK_REPLACE_TIME_DATE_FROM", config[CONF_REPLACE_TIME_DATE_FROM])

    if config[CONF_REPLACE_TIME_DATE_FROM] and config[CONF_REPLACE_TIME_DATE_TO]:
        from_parts = config[CONF_REPLACE_TIME_DATE_FROM].split()
        if len(from_parts) != len(config[CONF_REPLACE_TIME_DATE_TO].split()):
            _LOGGER.warning(
                "replace_time_date_from: and replace_time_date_to: do not have matching pairs! "
                "(not using replacements)",
            )
            cg.add(var.set_replace_time_date_active(False))
        elif len(from_parts) > 50:
            _LOGGER.warning(
                "replace_time_date_from: and replace_time_date_to: exceeds 50! "
                "(not using replacements)",
            )
            cg.add(var.set_replace_time_date_active(False))
        else:
            _LOGGER.info(
                "replace_time_date_from: and replace_time_date_to: defined (using replacements)",
            )
            cg.add(var.set_replace_time_date_active(True))
    else:
        cg.add(var.set_replace_time_date_active(False))
        if config[CONF_REPLACE_TIME_DATE_TO]:
            _LOGGER.warning(
                "replace_time_date_to: defined but no replace_time_date_from:! "
                "(not using replacements)",
            )
        if config[CONF_REPLACE_TIME_DATE_FROM]:
            _LOGGER.warning(
                "replace_time_date_from: defined but no replace_time_date_to:! "
                "(not using replacements)",
            )

    cg.add_define("PIXEL_CLOCK_SCROLL_INTERVAL", config[CONF_SCROLLINTERVAL])
    cg.add_define("PIXEL_CLOCK_RAINBOW_INTERVAL", config[CONF_RAINBOWINTERVAL])
    cg.add_define("PIXEL_CLOCK_FRAME_INTERVAL", config[CONF_FRAMEINTERVAL])
    cg.add_define("PIXEL_CLOCK_CLOCK_INTERVAL", config[CONF_CLOCKINTERVAL])
    cg.add_define("PIXEL_CLOCK_SCROLL_COUNT", config[CONF_SCROLLCOUNT])
    cg.add_define("PIXEL_CLOCK_WEEK_START", config[CONF_WEEK_START_MONDAY])
    cg.add_define("PIXEL_CLOCK_DEFAULT_FONT_OFFSET_X", config[CONF_DEFAULT_FONT_XOFFSET])
    cg.add_define("PIXEL_CLOCK_DEFAULT_FONT_OFFSET_Y", config[CONF_DEFAULT_FONT_YOFFSET])
    cg.add_define("PIXEL_CLOCK_SPECIAL_FONT_OFFSET_X", config[CONF_SPECIAL_FONT_XOFFSET])
    cg.add_define("PIXEL_CLOCK_SPECIAL_FONT_OFFSET_Y", config[CONF_SPECIAL_FONT_YOFFSET])
    cg.add_define("PIXEL_CLOCK_TIME_FORMAT", config[CONF_TIME_FORMAT])
    cg.add_define("PIXEL_CLOCK_DATE_FORMAT", config[CONF_DATE_FORMAT])

    if config[CONF_TIME_FORMAT_BIG]:
        cg.add_define("PIXEL_CLOCK_TIME_FORMAT_BIG", config[CONF_TIME_FORMAT_BIG])
    else:
        cg.add_define("PIXEL_CLOCK_TIME_FORMAT_BIG", config[CONF_TIME_FORMAT])

    if config[CONF_DATE_FORMAT_BIG]:
        cg.add_define("PIXEL_CLOCK_DATE_FORMAT_BIG", config[CONF_DATE_FORMAT_BIG])
    else:
        cg.add_define("PIXEL_CLOCK_DATE_FORMAT_BIG", config[CONF_DATE_FORMAT])

    if config[CONF_RAINBOWSHIMMER]:
        cg.add_define("PIXEL_CLOCK_RAINBOW_SHIMMER")
        _LOGGER.info("[X] Rainbow shimmer")

    if config[CONF_MULTICOLOR_TEXT]:
        cg.add_define("PIXEL_CLOCK_MULTICOLOR_TEXT")
        _LOGGER.info("[X] Multi color text")

    if config[CONF_SCROLL_SMALL_TEXT]:
        cg.add_define("PIXEL_CLOCK_SCROLL_SMALL_TEXT")

    if (config[CONF_BLENDSTEPS]) > 0:
        cg.add_define("PIXEL_CLOCK_BLEND_STEPS", config[CONF_BLENDSTEPS])

    if config[CONF_RTL]:
        cg.add_define("PIXEL_CLOCK_USE_RTL")

    if config[CONF_VERTICAL]:
        cg.add_define("PIXEL_CLOCK_USE_VERTICAL_SCROLL")
        _LOGGER.info("[X] Vertical scroll")

    if config[CONF_CLOCK]:
        cg.add_define("PIXEL_CLOCK_ADV_CLOCK")
        _LOGGER.info("[X] Advanced clock mode")

    if config[CONF_CLOCK] and config[CONF_FLIP_FLOP]:
        cg.add_define("PIXEL_CLOCK_FLIP_FLOP")
        _LOGGER.info("[X] Flip Flop clock mode")
        if config[CONF_FLIP_FLOP_SPEED]:
            cg.add_define("PIXEL_CLOCK_FLIP_FLOP_SPEED", config[CONF_FLIP_FLOP_SPEED])
            _LOGGER.info("[X] Flip Flop Speed %s", config[CONF_FLIP_FLOP_SPEED])

    if config[CONF_BITMAP]:
        cg.add_define("PIXEL_CLOCK_ADV_BITMAP")
        _LOGGER.info("[X] Advanced bitmap mode")

    if config.get(CONF_BOOTLOGO):
        cg.add(var.set_boot_logo(config[CONF_BOOTLOGO]))
        cg.add_define("PIXEL_CLOCK_ADV_BOOT")
        _LOGGER.info("[X] Advanced boot")

        if config[CONF_BOOTLOGOMODE] == 0:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_0")
            _LOGGER.info("[X] Advanced boot mode 0")
        if config[CONF_BOOTLOGOMODE] == 1:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_1")
            _LOGGER.info("[X] Advanced boot mode 1")
        if config[CONF_BOOTLOGOMODE] == 2:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_2")
            _LOGGER.info("[X] Advanced boot mode 2")
        if config[CONF_BOOTLOGOMODE] == 3:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_3")
            _LOGGER.info("[X] Advanced boot mode 3")
        if config[CONF_BOOTLOGOMODE] == 4:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_4")
            _LOGGER.info("[X] Advanced boot mode 4")
        if config[CONF_BOOTLOGOMODE] == 5:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_5")
            _LOGGER.info("[X] Advanced boot mode 5")
        if config[CONF_BOOTLOGOMODE] == 6:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_6")
            _LOGGER.info("[X] Advanced boot mode 6")
        if config[CONF_BOOTLOGOMODE] == 7:
            cg.add_define("PIXEL_CLOCK_ADV_BOOT_MODE_7")
            _LOGGER.info("[X] Advanced boot mode 7")

    if config[CONF_NIGHT_MODE_SCREENS]:
        cg.add_define("PIXEL_CLOCK_CONF_NIGHT_MODE_SCREENS", config[CONF_NIGHT_MODE_SCREENS])

    if config[CONF_ICON_INDICATOR_SCREENS]:
        cg.add_define(
            "PIXEL_CLOCK_CONF_ICON_INDICATOR_SCREENS",
            config[CONF_ICON_INDICATOR_SCREENS],
        )

    cg.add(var.set_show_day_of_week(config[CONF_SHOWDOW]))

    cg.add(var.set_show_seconds(config[CONF_SHOW_SECONDS]))

    _LOGGER.info("[X] Right Top Indicator - Alarm")
    if config[CONF_RCINDICATOR]:
        cg.add_define("PIXEL_CLOCK_RCINDICATOR")
        _LOGGER.info("[X] Right Center Indicator")
    if config[CONF_RBINDICATOR]:
        cg.add_define("PIXEL_CLOCK_RBINDICATOR")
        _LOGGER.info("[X] Right Bottom Indicator - Right")
    if config[CONF_LTINDICATOR]:
        cg.add_define("PIXEL_CLOCK_LTINDICATOR")
        _LOGGER.info("[X] Left Top Indicator")
    if config[CONF_LCINDICATOR]:
        cg.add_define("PIXEL_CLOCK_LCINDICATOR")
        _LOGGER.info("[X] Left Center Indicator")
    if config[CONF_LBINDICATOR]:
        cg.add_define("PIXEL_CLOCK_LBINDICATOR")
        _LOGGER.info("[X] Left Bottom Indicator - Left")
    if config[CONF_ICINDICATOR]:
        cg.add_define("PIXEL_CLOCK_ICINDICATOR")
        _LOGGER.info("[X] Icon Indicator")
    if config[CONF_GAUGE]:
        cg.add_define("PIXEL_CLOCK_GAUGE")
        _LOGGER.info("[X] Gauge")
    if config[CONF_FIRE]:
        cg.add_define("PIXEL_CLOCK_USE_FIRE_PLUGIN")
        _LOGGER.info("[X] Fire screen")

    for conf in config.get(CONF_ON_NEXT_SCREEN, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(
            trigger,
            [(cg.std_string, "icon"), (cg.std_string, "text")],
            conf,
        )

    for conf in config.get(CONF_ON_EMPTY_QUEUE, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [], conf)

    for conf in config.get(CONF_ON_NEXT_CLOCK, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [], conf)

    for conf in config.get(CONF_ON_EXPIRED_SCREEN, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(
            trigger,
            [(cg.std_string, "icon"), (cg.std_string, "text")],
            conf,
        )

    for conf in config.get(CONF_ON_ICON_ERROR, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [(cg.std_string, "icon")], conf)

    for conf in config.get(CONF_ON_ADD_SCREEN, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(
            trigger,
            [(cg.std_string, "icon"), (cg.uint8, "mode")],
            conf,
        )

    for conf in config.get(CONF_ON_START_RUNNING, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [], conf)

    for conf in config.get(CONF_ON_SHOW_DISPLAY, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [(cg.bool_, "state")], conf)

    for conf in config.get(CONF_ON_NIGHT_MODE, []):
        trigger = cg.new_Pvariable(conf[CONF_TRIGGER_ID], var)
        await automation.build_automation(trigger, [(cg.bool_, "state")], conf)

    await cg.register_component(var, config)
