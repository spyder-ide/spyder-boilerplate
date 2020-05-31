# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2020, Gonzalo Peña-Castellanos
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Boilerplate Preferences Page.
"""

# Third party imports
from spyder.api.preferences import PluginConfigPage
from spyder.api.translations import get_translation

# Localization
_ = get_translation("spyder_boilerplate.spyder")


class SpyderBoilerplateConfPage(PluginConfigPage):

    # --- PluginConfigPage API
    # ------------------------------------------------------------------------
    def setup_page(self):
        pass
