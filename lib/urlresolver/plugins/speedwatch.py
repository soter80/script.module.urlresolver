'''
SpeedWatch.io urlresolver plugin
Copyright (C) 2019 gujal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

from __generic_resolver__ import GenericResolver

class SpeedWatchResolver(GenericResolver):
    name = "speedwatch"
    domains = ["speedwatch.io"]
    pattern = r'(?://|\.)(speedwatch\.io)/plyr/([0-9a-zA-Z]+)'

    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://www.{host}/plyr/{media_id}.html')
