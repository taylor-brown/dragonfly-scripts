from dragonfly import (
    Function,
    MappingRule,
    IntegerRef,
    Grammar,
    Dictation
)

from lib.dynamic_aenea import (
    GlobalDynamicContext,
    Key,
    Text,
)


import lib.format

DYN_MODULE_NAME = "bash"
INCOMPATIBLE_MODULES = []


def directory_up(n):
    repeat = ['..' for i in range(n)]  # @UnusedVariable
    txt = "cd %s\n" % ("/".join(repeat))
    Text(txt).execute()


rules = MappingRule(
    mapping={
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
        "directory up <n> [times]": Function(directory_up),
        "(D P K G|D package)": Text("dpkg "),
        "(D P K G|D package) list": Text("dpkg -l "),
        "exit": Text("exit"),
        "foreground": Text("fg "),
        "find process": Text("ps aux | grep -i "),
        "find process <text>": Text("ps aux | grep -i ") + Function(lib.format.snake_case_text),
        "find": Text("find . -name "),
        "find <text>": Text("find . -name %(text)s"),
        "[go to] end of line": Key("c-e"),
        "[go to] start of line": Key("c-a"),
        "grep": Text("grep "),
        "grep invert": Text("grep -v "),
        "grep <text>": Text("grep %(text)s"),
        "grep invert <text>": Text("grep -v %(text)s"),
        "grep recursive": Text("grep -rn ") +  Key("dquote/3, dquote/3") + Text(" *") + Key("left/3:3"),  # @IgnorePep8
        "grep recursive <text>": Text("grep -rn ") + Key("dquote/3") + Text("%(text)s") + Key("dquote/3") + Text(" *") + Key("left/3:3"),  # @IgnorePep8
        "history": Text("history "),
        "ifconfig": Text("ifconfig "),
        "(iptables|I P tables) list": Text("iptables -L"),
        "(iptables|I P tables) flush": Text("iptables -F"),
        "jobs": Text("jobs "),
        "kill": Text("kill "),
        "kill (hard|[dash]9)": Text("kill -9 "),
        "kill line": Key("c-k"),
        "(link|L N)": Text("ln "),
        "list files": Text("ls -la") + Key("enter"),
        "list files <text>": Text("ls -la %(text)s"),
        "list files time sort": Text("ls -lat") + Key("enter"),
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
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

terminator_grammar = Grammar("Python grammar", context=GlobalDynamicContext())
terminator_grammar.add_rule(rules)
terminator_grammar.load()
terminator_grammar.disable()


def dynamic_enable():
    global terminator_grammar
    if terminator_grammar.enabled:
        return False
    else:
        terminator_grammar.enable()
        return True


def dynamic_disable():
    global terminator_grammar
    if terminator_grammar.enabled:
        terminator_grammar.disable()
        return True
    else:
        return False


def is_enabled():
    global terminator_grammar
    if terminator_grammar.enabled:
        return True
    else:
        return False


# Unload function which will be called at unload time.
def unload():
    global terminator_grammar
    if terminator_grammar:
        terminator_grammar.unload()
    terminator_grammar = None
