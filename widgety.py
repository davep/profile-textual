from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widgets import Checkbox
from textual.widgets import ContentSwitcher
from textual.widgets import DataTable
from textual.widgets import Digits
from textual.widgets import DirectoryTree
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Input
from textual.widgets import Label
from textual.widgets import ListItem
from textual.widgets import ListView
from textual.widgets import LoadingIndicator
from textual.widgets import Log
from textual.widgets import MarkdownViewer
from textual.widgets import OptionList
from textual.widgets import Placeholder
from textual.widgets import Pretty
from textual.widgets import ProgressBar
from textual.widgets import RadioButton
from textual.widgets import RadioSet
from textual.widgets import RichLog
from textual.widgets import Select
from textual.widgets import SelectionList
from textual.widgets import Sparkline
from textual.widgets import Static
from textual.widgets import Switch
from textual.widgets import TabbedContent, TabPane
from textual.widgets import Tooltip
from textual.widgets import Tree
from textual.widgets import Welcome

class ManyWidgetsApp(App[None]):

    def compose(self) -> ComposeResult:
        yield Button()
        yield Checkbox()
        yield ContentSwitcher()
        yield DataTable()
        yield Digits()
        yield DirectoryTree(".")
        yield Footer()
        yield Header()
        yield Input()
        yield Label()
        yield ListItem()
        yield ListView()
        yield LoadingIndicator()
        yield Log()
        yield MarkdownViewer("README.md")
        yield OptionList()
        yield Placeholder()
        yield Pretty("Vacant")
        yield ProgressBar()
        yield RadioButton()
        yield RadioSet()
        yield RichLog()
        yield Select([("1", "1")])
        yield SelectionList()
        yield Sparkline()
        yield Static()
        yield Switch()
        with TabbedContent():
            with TabPane("Hello"):
                yield Label("Hello")
        yield Tooltip()
        yield Tree("Foo")
        yield Welcome()

    def on_ready(self) -> None:
        self.exit()

if __name__ == "__main__":
    ManyWidgetsApp().run()

### widgety.py ends here
