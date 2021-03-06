# -*- coding: utf-8 -*-

import pytest

from . import constants


@pytest.mark.parametrize('page', constants.TOPIC_PAGES)
@pytest.mark.parametrize('version', constants.TOPICS_VERSIONS, ids=constants.VERSION_IDS)
def test_topic_pages(browser, version, page):

    # Load the main page.
    browser.get(version)

    # Visit one of the topic pages.
    browser.find_element_by_link_text(page).click()

    # Did we get it?
    assert page in browser.page_source

    # Does it have a table of contents?
    assert 'Contents' in browser.page_source
