from dragonfly import Config, Section, Item, MappingRule, Grammar, Text, Key, Dictation

config = Config("my commands")
config.cmd = Section("helpers")
config.cmd.map = Item(
    {
        "cd (mogo test|mogotest)": Text("cd ~/dev/workspaces/mogotest") + Key("enter"),
        "cd (mogo test|mogotest) remote": Text("cd ~/dev/workspaces/mogotest-helix") + Key("enter"),
        "cd ping4": Text("cd ~/dev/workspaces/ping4app") + Key("enter"),
        "cd ping4 remote": Text("cd ~/ping4-helix") + Key("enter"),
        "cd workspaces": Text("cd ~/dev/workspaces") + Key("enter"),
        "cd home": Text("cd ~") + Key("enter"),
        "cd downloads": Text("cd ~/Downloads") + Key("enter"),
        "cd drop box": Text("cd ~/Dropbox") + Key("enter"),
        #"cd NatLink": Text("cd C:\NatLink\NatLink\MacroSystem") + Key("enter"),
        "cd NatLink": Text("cd /c/NatLink/NatLink/MacroSystem") + Key("enter"),

        "(open|start) rails console": Text("./script/rails c") + Key("enter"),
        "fix line endings": Text("find . -type f -exec dos2unix {} \; && chmod +x script/*") + Key("enter"),
        "fix (date|time)": Text("ntpd -qg") + Key("enter"),
        "stop torquebox": Text("service monit stop && service torquebox stop") + Key("enter"),
        "start torquebox": Text("service torquebox start") + Key("enter"),
        "grep torquebox": Text("ps aux | grep torque") + Key("enter"),


        "find URL group": Text("g = UrlGroup.where(uid: '').first") + Key("left:8"),

        "ssh Q A gateway": Text("ssh qa-gw.ping4inc.com") + Key("enter"),
        "ssh Q A mets": Text("ssh qa-mets.ping4inc.com") + Key("enter"),
        "ssh load test gateway": Text("ssh loadtest-gw.ping4inc.com") + Key("enter"),
        "ssh load test mets": Text("ssh loadtest-mets.ping4inc.com") + Key("enter"),
        "ssh melchior": Text("ssh nirvdrum@melchior") + Key("enter"),
        "ssh ping4 (development|V M)": Text("ssh development.ping4inc.com") + Key("enter"),
        "ssh Kevin dot mogotest dot com": Text("ssh kevin.mogotest.com") + Key("enter"),
        "ssh melchior": Text("ssh melchior") + Key("enter"),

        "ssh Cassandra 1": Text("ssh cas1.ping4central.com") + Key("enter"),
        "ssh Cassandra 2": Text("ssh cas2.ping4central.com") + Key("enter"),
        "ssh Cassandra 3": Text("ssh cas3.ping4central.com") + Key("enter"),
        "ssh Cassandra 4": Text("ssh cas4.ping4central.com") + Key("enter"),
        "ssh Cassandra 5": Text("ssh cas5.ping4central.com") + Key("enter"),
        "ssh Cassandra 6": Text("ssh cas6.ping4central.com") + Key("enter"),
        "ssh Cassandra 7": Text("ssh cas7.ping4central.com") + Key("enter"),
        "ssh Cassandra 8": Text("ssh cas8.ping4central.com") + Key("enter"),

        "tail app logs": Text("cd ~") + Key("enter") + Text("current") + Key("enter") + Text("tail -f log/*.log") + Key("enter"),
        "tail (torquebox|torque box) log": Text("tail -f /var/log/torquebox/torquebox.log") + Key("enter"),
        "tail development logs": Text("tail -f log.log/development.log") + Key("enter"),

        "edit ssh config": Text("vim ~/.ssh/config") + Key("enter"),

        "(open|start) program": Key("a-space"),

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
        "change ruby (jay ruby|jruby)": Text("rbenv shell jruby-1.7.10") + Key("enter"),

        "(torque box|TorqueBox) run": Text("torquebox run -b 0.0.0.0") + Key("enter"),
        "(torque box|TorqueBox) deploy": Text("torquebox deploy") + Key("enter"),
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
