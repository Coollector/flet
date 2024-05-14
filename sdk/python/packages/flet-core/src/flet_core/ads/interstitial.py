from typing import Any, Optional, Union

from flet_core.constrained_control import ConstrainedControl
from flet_core.control import OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    AnimationValue,
    OffsetValue,
    ResponsiveNumber,
    RotateValue,
    ScaleValue,
)


class InterstitialAd(ConstrainedControl):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/interstitialad
    """

    def __init__(
        self,
        unit_id: Optional[str] = None,
        on_load=None,
        on_error=None,
        on_open=None,
        on_close=None,
        on_impression=None,
        on_click=None,
        #
        # ConstrainedControl
        #
        ref: Optional[Ref] = None,
        key: Optional[str] = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        left: OptionalNumber = None,
        top: OptionalNumber = None,
        right: OptionalNumber = None,
        bottom: OptionalNumber = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        rotate: RotateValue = None,
        scale: ScaleValue = None,
        offset: OffsetValue = None,
        aspect_ratio: OptionalNumber = None,
        animate_opacity: AnimationValue = None,
        animate_size: AnimationValue = None,
        animate_position: AnimationValue = None,
        animate_rotation: AnimationValue = None,
        animate_scale: AnimationValue = None,
        animate_offset: AnimationValue = None,
        on_animation_end=None,
        tooltip: Optional[str] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            key=key,
            width=width,
            height=height,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            rotate=rotate,
            scale=scale,
            offset=offset,
            aspect_ratio=aspect_ratio,
            animate_opacity=animate_opacity,
            animate_size=animate_size,
            animate_position=animate_position,
            animate_rotation=animate_rotation,
            animate_scale=animate_scale,
            animate_offset=animate_offset,
            on_animation_end=on_animation_end,
            tooltip=tooltip,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.on_load = on_load
        self.on_error = on_error
        self.on_open = on_open
        self.on_close = on_close
        self.on_impression = on_impression
        self.on_click = on_click
        self.unit_id = unit_id

    def _get_control_name(self):
        return "interstitialad"

    def did_mount(self):
        super().did_mount()

    def show(self):
        self.invoke_method("show")

    @property
    def unit_id(self):
        return self._get_attr("unitId")

    @unit_id.setter
    def unit_id(self, value):
        self._set_attr("unitId", value)

    # on_load
    @property
    def on_load(self):
        return self._get_event_handler("load")

    @on_load.setter
    def on_load(self, handler):
        self._add_event_handler("load", handler)

    # on_error
    @property
    def on_error(self):
        return self._get_event_handler("error")

    @on_error.setter
    def on_error(self, handler):
        self._add_event_handler("error", handler)

    # on_open
    @property
    def on_open(self):
        return self._get_event_handler("open")

    @on_open.setter
    def on_open(self, handler):
        self._add_event_handler("open", handler)

    # on_close
    @property
    def on_close(self):
        return self._get_event_handler("close")

    @on_close.setter
    def on_close(self, handler):
        self._add_event_handler("close", handler)

    # on_click
    @property
    def on_click(self):
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler):
        self._add_event_handler("click", handler)

    # on_impression
    @property
    def on_impression(self):
        return self._get_event_handler("impression")

    @on_impression.setter
    def on_impression(self, handler):
        self._add_event_handler("impression", handler)
