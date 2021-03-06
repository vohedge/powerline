# -*- coding: utf-8 -*-
# vim:fenc=utf-8:noet

from powerline import Powerline
from powerline.lib import mergedicts


class IpythonPowerline(Powerline):
	def __init__(self):
		super(IpythonPowerline, self).__init__('ipython')

	def get_config_paths(self):
		if self.path:
			return [self.path]
		else:
			return super(IpythonPowerline, self).get_config_paths()

	def load_main_config(self):
		r = super(IpythonPowerline, self).load_main_config()
		if self.config_overrides:
			mergedicts(r, self.config_overrides)
		return r

	def load_theme_config(self, name):
		r = super(IpythonPowerline, self).load_theme_config(name)
		if name in self.theme_overrides:
			mergedicts(r, self.theme_overrides[name])
		return r
