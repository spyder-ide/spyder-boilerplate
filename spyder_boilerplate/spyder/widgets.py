# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2020, Gonzalo Peña-Castellanos
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Boilerplate Main Widget.
"""

# Third party imports
from spyder.api.translations import get_translation
from spyder.api.widgets import PluginMainWidget

# Localization
_ = get_translation('spyder_boilerplate.spyder')


class SpyderBoilerplateWidget(PluginMainWidget):
    DEFAULT_OPTIONS = {
    }

    # Signals

    def __init__(self, name, plugin, parent=None, options=DEFAULT_OPTIONS):
        super().__init__(name, plugin, parent=parent, options=options)

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def get_title(self):
        return _("Spyder Boilerplate")

    def get_focus_widget(self):
        pass

    def setup(self):
        pass

    def on_option_update(self, option, value):
        pass

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
