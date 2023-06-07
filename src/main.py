from yapsy.PluginManager import PluginManager

import os


def main():
    """
    Load plugins from the 'plugins' directory and apply the "Upper Case Plugin" to a string.
    """
    # Compute the absolute path of the 'plugins' directory, which is assumed
    # to be a subdirectory of the directory where this script is located.
    plugin_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plugins")

    # Create a PluginManager and tell it to load plugins from the 'plugins' directory.
    manager = PluginManager()
    manager.setPluginPlaces([plugin_dir])
    manager.collectPlugins()

    # Print the names of all loaded plugins.
    for plugin in manager.getAllPlugins():
        print(f"Loaded plugin: {plugin.name}")

    # Prepare some text to be processed by the plugins.
    text = "hello, world!"
    print("Before processing:", text)

    # Pass the text to the "Upper Case Plugin" for processing.
    for plugin in manager.getAllPlugins():
        if plugin.name == "Upper Case Plugin":
            text = plugin.plugin_object.process(text)
            print("After processing:", text)


if __name__ == "__main__":
    main()  # Invoke the main function when this script is run as a standalone program.
