#!/usr/bin/env python3
"""Unittests for base_model.py"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_uuid(self):

        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

