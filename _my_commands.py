from dragonfly import Config, Section, Item, MappingRule, Grammar, Text, Key, Dictation

config = Config("my commands")
config.cmd = Section("helpers")
config.cmd.map = Item(
    {
        "cd (mogo test|mogotest)": Text("cd ~/dev/workspaces/mogotest") + Key("enter"),
        "cd workspaces": Text("cd ~/dev/workspaces") + Key("enter"),
        "cd home": Text("cd ~") + Key("enter"),
        "cd downloads": Text("cd ~/Downloads") + Key("enter"),
        "cd drop box": Text("cd ~/Dropbox") + Key("enter"),

        "(open|start) rails console": Text("./script/rails c") + Key("enter"),

        "find URL group": Text("g = UrlGroup.where(uid: '').first") + Key("left:8"),

        # Custom vocabulary.
        "nerve drum": Text("nirvdrum"),
        "J ruby": Text("jruby"),
        "you tills": Text("utils"),
        "firefox you tills": Text("FirefoxUtils"),
        "IE 601": Text("ie601"),
        "IE 602": Text("ie602"),
        "IE 701": Text("ie701"),
        "IE 702": Text("ie702"),
        "IE 801": Text("ie801"),
        "IE 802": Text("ie802"),
        "IE 901": Text("ie901"),
        "IE 902": Text("ie902"),
        "IE 1001": Text("ie1001"),
        "IE 1002": Text("ie1002"),

        "ruby version": Text("ruby --version") + Key("enter"),
        "change ruby M R I": Text("rbenv shell 2.1.0") + Key("enter"),
        "change (jay ruby|jruby) 1.7.10": Text("rbenv shell jruby-1.7.10") + Key("enter"),
    }
)

class MyCommandsRule(MappingRule):
    mapping = config.cmd.map

    extras = [
        Dictation("text"),
    ]

global_context = None  # Context is None, so grammar will be globally active.
grammar = Grammar("My commands", context=global_context)  # Create this module's grammar.
grammar.add_rule(MyCommandsRule())  # Add the top-level rule.
grammar.load()  # Load the grammar.


def unload():
    """Unload function which will be called at unload time."""
    global grammar
    if grammar:
        grammar.unload()
    grammar = None