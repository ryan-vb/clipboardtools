import unittest
from clipboardtools.plugins.pluginbase import PluginBase


class PluginRegistration(unittest.TestCase):
    def test_should_provide_abstract_plugin_class(self):
        class TestPlugin(PluginBase):
            def meta(self):
                return True

            def run(self):
                return True

        test_plugin = TestPlugin()
        self.assertIsInstance(test_plugin, PluginBase)

    # def test_should_register_available_plugins(self):
    #
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
