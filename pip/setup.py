#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="spcs",
    version="0.0.1",
    keywords=["pakistan", "sindh", "police", "complaint", "query", "search"],

    description="Pakistan Sindh Police complaint status check.",
    long_description=open('README.md').read(),

    project_urls={
        'Homepage': 'https://www.techtum.dev/work-spcs-220121.html#work-spcs-220121',
        'Source': 'https://github.com/siphr/spcs',
        'Tracker': 'https://github.com/siphr/spcs/issues',
    },

    author="siphr",
    author_email="pypi@techtum.dev",

    packages=['spcs'],
    platforms="any",
)
