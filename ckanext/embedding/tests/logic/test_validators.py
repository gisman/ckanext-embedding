"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.embedding.logic import validators


def test_embedding_reauired_with_valid_value():
    assert validators.embedding_required("value") == "value"


def test_embedding_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.embedding_required(None)
