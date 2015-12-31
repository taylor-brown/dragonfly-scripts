import aenea.config
import aenea.configuration
import format

from aenea import (
    AeneaContext,
    AppContext,
    Dictation,
    Grammar,
    IntegerRef,
    Key,
    MappingRule,
    ProxyAppContext,
    Text,
    Pause,
    Function
)


rules = MappingRule(
    mapping={
        # Miscellaneous.
        "[start|exit] full screen": Key("f11"),
        "search": Key("cs-f"),
        "(toggle|show|hide) (scroll|scrollbar)": Key("cs-s"),

        # Window management.
        "new window": Key("cs-i"),
        "close window": Key("cs-q"),

        # Tab management.
        "new tab": Key("cs-t"),
        "close tab": Key("cs-w"),
        "rename tab": Key("c-r"),
        "[switch to] next tab": Key("c-pgdown"),
        "[switch to] previous tab": Key("c-pgup"),
        "move tab left": Key("cs-pgup"),
        "move tab right": Key("cs-pgdown"),

        # View management.
        "split horizontally": Key("cs-o"),
        "split vertically": Key("cs-e"),
        "close view": Key("cs-w"),
        "[switch to] next view": Key("c-tab"),
        "[switch to] previous view": Key("cs-tab"),
        "[switch to] left view": Key("a-left"),
        "[switch to] right view": Key("a-right"),
        "[switch to] top view": Key("a-up"),
        "[switch to] bottom view": Key("a-down"),
        "clear (view|tab|window|terminal)": Key("cs-g"),
        "resize left [<n>]": Key("cs-left:%(n)d"),
        "resize right [<n>]": Key("cs-right:%(n)d"),
        "resize up [<n>]": Key("cs-up:%(n)d"),
        "resize down [<n>]": Key("cs-down:%(n)d"),

        # Zoom.
        "(zoom|focus|unzoom|unfocus) (view|tab|terminal)": Key("cs-z"),
        "zoom (100 percent|reset|normal)": Key("c-0"),
        "zoom in": Key("c-plus"),
        "zoom out": Key("c-minus"),

        # Cursor grouping.
        "group all": Key("w-g"),
        "ungroup all": Key("ws-g"),
        "group tab": Key("w-t"),
        "ungroup tab": Key("ws-t"),

        # Copy & paste.
        "copy [that]": Key("cs-c"),
        "paste [that]": Key("cs-v"),
        # Commands and keywords:
        "apt cache search": Text("apt-cache search "),
        "apt cache search <text>": Text("apt-cache search %(text)s"),
        "apt cache show": Text("apt-cache show "),
        "apt cache show <text>": Text("apt-get show %(text)s"),
        "apt get install": Text("apt-get install "),
        "apt get install <text>": Text("apt-get install %(text)s"),
        "apt get update": Text("apt-get update") + Key("enter"),
        "sudo apt get install": Text("sudo apt-get install "),
        "sudo apt get install <text>": Text("sudo apt-get install %(text)s"),
        "sudo apt get update": Text("sudo apt-get update") + Key("enter"),
        "background": Text("bg "),
        "(cat|C A T)": Text("cat "),
        "(cat|C A T) <text>": Text("cat %(text)s"),
        "(change (directory|dir)|C D)": Text("cd "),
        "(change (directory|dir)|C D) <text>": Text("cd %(text)s"),
        "[press] control break": Key("ctrl:down, c/10, ctrl:up"),
        "(copy|C P)": Text("cp "),
        "(copy|C P) recursive": Text("cp -r "),
        "copy terminal": Key("cs-c/3"),
        "(change mode)|C H mod": Text("chmod "),
        "(cron|cron tab|crontab) edit": Text("crontab -e") + Key("enter"),
        "(cron|cron tab|crontab) list": Text("crontab -l") + Key("enter"),
        "(cron|cron tab|crontab) reset": Text("crontab -r"),
        "diff": Text("diff "),
        "(D P K G|D package)": Text("dpkg "),
        "(D P K G|D package) list": Text("dpkg -l "),
        "exit": Text("exit"),
        "foreground": Text("fg "),
        "find process": Text("ps aux | grep -i "),
        "find process <text>": Text("ps aux | grep -i ") + Function(format.snake_case_text),
        "find": Text("find . -name "),
        "find <text>": Text("find . -name %(text)s"),
        "[go to] end of line": Key("c-e"),
        "[go to] start of line": Key("c-a"),
        "grep": Text("grep "),
        "grep invert": Text("grep -v "),
        "grep <text>": Text("grep %(text)s"),
        "grep invert <text>": Text("grep -v %(text)s"),
        "grep recursive": Text("grep -rn ") + Key("dquote/3, dquote/3") + Text(" *") + Key("left/3:3"),  # @IgnorePep8
        "grep recursive <text>": Text("grep -rn ") + Key("dquote/3") + Text("%(text)s") + Key("dquote/3") + Text(
            " *") + Key("left/3:3"),  # @IgnorePep8
        "history": Text("history "),
        "ifconfig": Text("ifconfig "),
        "(iptables|I P tables) list": Text("iptables -L"),
        "(iptables|I P tables) flush": Text("iptables -F"),
        "jobs": Text("jobs "),
        "kill": Text("kill "),
        "kill (hard|[dash]9)": Text("kill -9 "),
        "kill line": Key("c-k"),
        "(link|L N)": Text("ln "),
        "list files": Text("ls -lah") + Key("enter"),
        "list files <text>": Text("ls -lha %(text)s"),
        "list files time sort": Text("ls -laht") + Key("enter"),
        "make (directory|dir)": Text("mkdir "),
        "make (directory|dir) <text>": Text("mkdir %(text)s"),
        "move": Text("mv "),
        "move <text>": Text("mv %(text)s"),
        "paste terminal": Key("cs-v/3"),
        "pipe": Text(" | "),
        "ping": Text("ping "),
        "(print working directory|P W D)": Text("pwd") + Key("enter"),
        "([list] processes [list]|P S)": Text("ps -ef"),
        "(R M|remove file)": Text("rm "),
        "(R M|remove file) <text>": Text("rm %(text)s"),
        "remove (directory|dir|folder|recursive)": Text("rm -rf "),
        "remove (directory|dir|folder|recursive) <text>": Text("rm -rf %(text)s"),  # @IgnorePep8
        "(sed|S E D)": Text("sed "),
        "(secure copy|S C P)": Text("scp "),
        "(secure copy|S C P) <text>": Text("scp %(text)s"),
        "(secure shell|S S H)": Text("ssh "),
        "(secure shell|S S H) <text>": Text("ssh %(text)s"),
        "soft link": Text("ln -s "),
        "soft link <text>": Text("ln -s %(text)s"),
        "sudo": Text("sudo "),
        "(switch user|S U)": Text("su "),
        "(switch user|S U) login": Text("su - "),
        "tail": Text("tail "),
        "tail <text>": Text("tail %(text)s"),
        "tail (F|follow)": Text("tail -f "),
        "tail (F|follow) <text>": Text("tail -f %(text)s"),
        "telnet": Text("telnet "),
        "touch": Text("touch "),
        "touch <text>": Text("touch %(text)s"),
        "vim": Text("vim "),
        "vim <text>": Text("vim %(text)s"),
        "(W C|word count)": Text("wc "),
        "(W C|word count) lines": Text("wc -l "),
        "W get ": Text("wget "),
        "X args": Text("xargs "),
        "X D O tool": Text("xdotool "),
        "X M L lint": Text("xmllint "),
        "X M L lint <text>": Text("xmllint %(text)s"),
        "X M L lint format": Text("xmllint -format "),
        "X M L lint format <text>": Text("xmllint -format %(text)s"),
        "X M L lint schema": Text("xmllint -schema "),
        "X M L lint schema <text>": Text("xmllint -schema %(text)s"),
        "X prop": Text("xprop "),
        "X win info": Text("xwininfo "),
    },


    extras=[IntegerRef('n', 1, 10), Dictation('text')]

)

context = aenea.AeneaContext(
    ProxyAppContext(match='regex', title='fish'),
    (AppContext(executable='python'))
)

terminator_grammar = Grammar("Terminator general", context=context)
terminator_grammar.add_rule(rules)
terminator_grammar.load()


def unload():
    global terminator_grammar
    if terminator_grammar:
        terminator_grammar.unload()
    grammar = None