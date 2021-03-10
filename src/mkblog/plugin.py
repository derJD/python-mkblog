#!/usr/bin/env python

# Copyright (c) 2021 Jean-Denis Gebhardt <projects@der-jd.de>
# MIT License
# (see LICENSE or https://opensource.org/licenses/MIT)

from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type


class MkBlog(BasePlugin):
    config_scheme = (
        ('blogdir', Type(str, default='blog/'))
    )

    def __init__(self):
        pass

    # def on_config(self, config)
    # def on_page_read_source(self, page, config):
    # def on_page_markdown(self, markdown, page, config, files):
    #     page.meta
    #     # must contain date / release / release-date
    # def on_nav(self, nav, config, files):
