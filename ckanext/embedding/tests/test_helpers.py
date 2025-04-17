"""Tests for helpers.py."""

import ckanext.embedding.helpers as helpers


def test_embedding_hello():
    assert helpers.embedding_hello() == "Hello, embedding!"
