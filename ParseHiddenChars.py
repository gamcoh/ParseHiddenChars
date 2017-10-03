import sublime
import sublime_plugin

from string import printable

class ParseHiddenChars(sublime_plugin.TextCommand):
	def run(self, edit):
		html = self.view.substr(sublime.Region(0, self.view.size()))
		new_html = ''.join(char for char in html if char in printable)

		self.view.replace(edit, sublime.Region(0, self.view.size()), new_html)


