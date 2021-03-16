#!/usr/bin/env python3

# Copyright (c) 2021 Jean-Denis Gebhardt <projects@der-jd.de>
# MIT License
# (see LICENSE or https://opensource.org/licenses/MIT)

"""
Yet an other blog plugin for MkDocs.
"""

from datetime import datetime
from pathlib import Path

import logging
import markdown

from mkdocs.config.config_options import Type
from mkdocs.config import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import Files, File

log = logging.getLogger('mkdocs.config')


class MkBlog(BasePlugin):
    """
    This mkdocs plugin gives you the ability to write blog posts in
    `blog_dir` (defaults to `blog/`) separate from `docs_dir`.
    However files are arranged in `blog_dir`, they will be published under
    `/<blog_dir>/<release_date>/<title>/`.
    For determening a release date markdown metadata `date` is used.

    Example:
        blog/first-post.md:
        ```markdown
        ---
        author: JD
        date: 1990-01-01
        ---

        # My first Blogpost

        ## intro

        Hi

        ## Conclusion

        Bye

        ```

        This will be published under /blog/1990/01/01/first-post/
    """
    config_scheme = (
        ('blog_dir', Type(str, default='blog')),
    )

    def __init__(self):
        self._blog_md_file = None

    def get_blog_md(self):
        """
        searches for markdown files in `blog_dir`.

        Returns:
        files collection from all blogposts as list
        """
        basedir = Path(self.config['docs_dir']).parent
        blogdir = Path(f'{str(basedir)}/{self.config["blog_dir"]}')

        blog_md_files = list(blogdir.rglob('*.md'))
        return blog_md_files

    def get_blog_post_date(self):
        """
        Search markdown metadata for a releasedate from given file.

        Parameters:
        file: absolute path to blogpost markdown file
        Returns:
        blogpost's release date as uri path
        """
        m_d = markdown.Markdown(extensions=['meta'])
        m_d.convert(self._blog_md_file.read_text())
        # Prevent pylint from false positive report:
        #   Instance of 'Markdown' has no 'Meta' member
        metadata = m_d.Meta  # pylint: disable=E1101

        # TODO: search for different date metadata(release-date, date, release)
        #       if no metadata is found, use file's ctime or mtime instead.
        release_date = datetime.strptime(metadata['date'][0], '%Y-%m-%d')

        return str(release_date.strftime('%Y/%m/%d'))

    def build_blog_dest(self):
        """
        Before appending new file object to mkdocs, this method
        rewrites the destination path and url for the blogpost.

        Returns:
        new destination for html file and url
        """
        path = (
            f'{self.config["blog_dir"]}/'
            f'{self.get_blog_post_date()}/'
            f'{self._blog_md_file.stem}')
        blog_dest = {
            path: dict(
                path=f'{path}.md',
                src_dir=self._blog_md_file.resolve(),
                dest_dir=self.config['site_dir'],
                url=f'{path}/'
                )
        }

        log.debug('Rewritten Blog Destination: %s', blog_dest)
        return blog_dest

    def on_files(self, files: Files, config: Config):
        """
        From `https://www.mkdocs.org/user-guide/plugins/#on_files`:
        The files event is called after the files collection is populated from
        the docs_dir. Use this event to add, remove, or alter files in the
        collection. Note that Page objects have not yet been associated with
        the file objects in the collection.
        Use Page Events to manipulate page specific data.

        Parameters:
        files: global files collection
        config: global configuration object
        Returns:
        global files collection
        """
        _posts_by_date = dict()
        self.config.update(dict(
            docs_dir=config['docs_dir'],
            site_dir=config['site_dir']
        ))

        for self._blog_md_file in self.get_blog_md():
            _posts_by_date.update(self.build_blog_dest())

        for post in sorted(_posts_by_date):
            post = _posts_by_date[post]

            blogpost = File(
                path=post['path'],
                src_dir=post['src_dir'],
                dest_dir=post['dest_dir'],
                use_directory_urls=config['use_directory_urls']
            )
            blogpost.abs_src_path = post['src_dir']
            files.append(blogpost)

        return files
