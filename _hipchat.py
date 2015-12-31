from dragonfly import Config, Section, Item, AppContext, Grammar, MappingRule, IntegerRef, Dictation, Choice, Key, Text

config = Config("HipChat")
config.usernames = Section("Username Mappings")
config.usernames.map = Item(
  {
    "All": "all",
    "Here": "here"
  }
)

config.load()

class NavigationRule(MappingRule):
  mapping = {
    "move up [<n>]":                                    Key("ctrl:down, shift:down, tab:%(n)d, shift:up, ctrl:up"),
    "move down [<n>]":                                  Key("ctrl:down, tab:%(n)d, ctrl:up"),
    "close tab":                                        Key("ctrl:down, f4, ctrl:up"),
    "(join room | private message) <room>":             Key("c-j/25") + Text("%(room)s") + Key("enter"),
    }

  extras = [
    IntegerRef("n", 1, 10),
    Dictation("room"),
    ]

  defaults = {
    "n": 1,
    }

class ChatRule(MappingRule):
  mapping = {
    "at <user>":     Text("@%(user)s "),
    "send":          Key("enter"),
  }

  extras = [
    Choice("user", config.usernames.map),
  ]


context = AppContext(executable="hipchat")
terminator_grammar = Grammar("hipchat_general", context=context)
terminator_grammar.add_rule(NavigationRule())
terminator_grammar.add_rule(ChatRule())
terminator_grammar.load()

# Unload function which will be called by natlink at unload time.
def unload():
  global terminator_grammar
  if grammar: grammar.unload()
  grammar = None