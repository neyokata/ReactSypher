# test_reactsypher.py
"""
Tests for ReactSypher module.
"""

import unittest
from reactsypher import ReactSypher

class TestReactSypher(unittest.TestCase):
    """Test cases for ReactSypher class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ReactSypher()
        self.assertIsInstance(instance, ReactSypher)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ReactSypher()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
