#!/usr/bin/env python3

def pytest_itemcollected(item):
    """Customize the display names of test items in pytest reports."""
    par = item.parent.obj
    node = item.obj
    pref = par.__doc__.strip() if par.__doc__ else par.__name__
    suf = node.__doc__.strip() if node.__doc__ else node.__name__
    
    # Join prefix and suffix with a space and update the node ID
    if pref or suf:
        item._nodeid = ' '.join(filter(None, [pref, suf]))

# Ensure that the function is registered as a pytest hook
def pytest_configure(config):
    config.pluginmanager.register(CustomItemDisplay())

class CustomItemDisplay:
    """Plugin to customize item display in pytest."""

    @staticmethod
    def pytest_itemcollected(item):
        """Modify item display using class and method docstrings or names."""
        par = item.parent.obj
        node = item.obj
        pref = par.__doc__.strip() if par.__doc__ else par.__name__
        suf = node.__doc__.strip() if node.__doc__ else node.__name__
        
        # Join prefix and suffix with a space and update the node ID
        if pref or suf:
            item._nodeid = ' '.join(filter(None, [pref, suf]))
