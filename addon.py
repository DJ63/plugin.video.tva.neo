# -*- coding: utf-8 -*-

'''*
	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
*'''
from commoncore import core
from commoncore import kodi
from commoncore.constants import DEFAULT_VIEWS

@kodi.register('main')
def main():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'tv_menu'}, {'title': "Shows"}, menu=menu, icon='shows.png')
	kodi.add_menu_item({'mode': 'movie_menu'}, {'title': "Movies"}, menu=menu, icon='movies.png')
	kodi.add_menu_item({'mode': 'settings_menu'}, {'title': "Settings and Tools"}, menu=menu, icon='settings.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('tv_menu')
def tv_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'my_calendar'}, {'title': "My Calendar"}, icon='calendar.png')
	kodi.add_menu_item({'mode': 'custom_list_menu', 'media': 'shows'}, {'title': "My Show Lists"}, icon='lists.png')
	kodi.add_menu_item({'mode': 'shows_watchlist', "api": {"name": "trakt", "method": "get_my_watchlist_shows"}}, {'title': "My Watchlist"}, icon='watchlist.png')
	kodi.add_menu_item({'mode': 'shows_collection', "api": {"name": "trakt", "method": "get_my_collection_shows"}}, {'title': "My Collection"}, icon='collection.png')
	kodi.add_menu_item({'mode': 'shows_standard_menu'}, {'title': "Trakt Lists"}, icon='trakt_lists.png')
	kodi.add_menu_item({'mode': 'shows_inprogress', "api": {"name": "trakt", "method": "get_inprogress_shows"}}, {'title': "In Progress"}, icon='in_progress.png')
	kodi.add_menu_item({'mode': 'search_menu', 'media': 'show'}, {'title': "Search"}, icon='search.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('shows_standard_menu')
def shows_standard_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'shows_trending', "api": {"name": "trakt", "method": "get_trending_shows"}}, {'title': "Trending Shows"}, icon='trending.png')
	kodi.add_menu_item({'mode': 'shows_popular', "api": {"name": "trakt", "method": "get_popular_shows"}}, {'title': "Popular Shows"}, icon='popular.png')
	kodi.add_menu_item({'mode': 'shows_recommended', "api": {"name": "trakt", "method": "get_recommended_shows"}}, {'title': "Recommended Shows"}, icon='recommended.png')
	kodi.add_menu_item({'mode': 'shows_anticipated', "api": {"name": "trakt", "method": "get_anticipated_shows"}}, {'title': "Anticipated Shows"}, icon='anticipated.png')
	kodi.add_menu_item({'mode': 'shows_genres', "media": "shows", "api": {"name": "trakt", "method": "get_genres", "args": ("shows", )}}, {'title': "Genres"}, icon='genres.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('movie_menu')
def movie_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'movies_watchlist', "api": {"name": "trakt", "method": "get_my_watchlist_movies"}}, {'title': "My Watchlist"},icon='watchlist.png')
	kodi.add_menu_item({'mode': 'custom_list_menu', "media": "movies"}, {'title': "My Movie Lists"}, icon='lists.png')
	kodi.add_menu_item({'mode': 'movies_collection', "api": {"name": "trakt", "method": "get_my_collection_movies"}}, {'title': "My Collection"}, icon='collection.png')
	kodi.add_menu_item({'mode': 'movies_standard_menu'}, {'title': "Trakt Lists"}, icon='lists.png')
	kodi.add_menu_item({'mode': 'movies_inprogress', "api": {"name": "trakt", "method": "get_inprogress_movies"}}, {'title': "In Progress"}, icon='in_progress.png')
	kodi.add_menu_item({'mode': 'search_menu', 'media': 'movie'}, {'title': "Search"}, icon='search.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('movies_standard_menu')
def movies_standard_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'movies_trending', "api": {"name": "trakt", "method": "get_trending_movies"}}, {'title': "Trending Movies"}, icon='trending.png')
	kodi.add_menu_item({'mode': 'movies_popular', "api": {"name": "trakt", "method": "get_popular_movies"}}, {'title': "Popular Movies"}, icon='popular.png')
	kodi.add_menu_item({'mode': 'movies_recommended', "api": {"name": "trakt", "method": "get_recommended_movies"}}, {'title': "Recommended Movies"}, icon='recommended.png')
	kodi.add_menu_item({'mode': 'movies_anticipated', "api": {"name": "trakt", "method": "get_anticipated_movies"}}, {'title': "Anticipated Movies"}, icon='anticipated.png')
	kodi.add_menu_item({'mode': 'movies_genres', 'media': 'movies', "api": {"name": "trakt", "method": "get_genres", "args": ("movies", )}}, {'title': "Genres"}, icon='genres.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('settings_menu')
def settings_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'auth_realdebrid'}, {'title': "Authorize RealDebrid"}, icon='authorize.png')
	kodi.add_menu_item({'mode': 'premiumize_menu'}, {'title': "Premiumize Cloud"}, icon='premiumize.png')
	kodi.add_menu_item({'mode': 'scrapecore_settings', "api": {"name": "kodi", "method": "open_settings", "args": ("script.module.scrapecore", )}}, {'title': "ScrapeCore Settings"}, icon='settings.png')
	kodi.add_menu_item({'mode': 'open_settings', 'addon_id': 'service.fanart.proxy'}, {'title': "Fanart Proxy Settings"}, icon='settings.png')
	kodi.add_menu_item({'mode': 'commoncore_settings'}, {'title': "Dillinger Common Settings"}, icon='settings.png')
	kodi.add_menu_item({'mode': 'addon_settings'}, {'title': "Addon Settings"}, icon='settings.png')
	kodi.eod(DEFAULT_VIEWS.LIST)
	
@kodi.register('premiumize_menu')
def premiumize_menu():
	menu = kodi.ContextMenu()
	menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("list",)}})
	kodi.add_menu_item({'mode': 'premiumize_transfers'}, {'title': "Transfer List"}, icon='transfer.png')
	kodi.add_menu_item({'mode': 'premiumize_folders'}, {'title': "Browse Folders"}, icon='premiumize.png')
	kodi.eod(DEFAULT_VIEWS.LIST)
	
@kodi.register('search_menu')
def search_menu():
	from commoncore import trakt
	kodi.add_menu_item({'mode': '%s_search_results' % kodi.args['media'], "api": {"name": "trakt", "method": "search", "args": ('',)}}, {'title': "*** New Search ***"}, icon='search.png')
	history = trakt.get_search_history(kodi.args['media'])
	for h in history:
		kodi.add_menu_item({'mode': '%s_search_results' % kodi.args['media'], "api": {"name": "trakt", "method": "search", "args": h}}, {'title': h[0]}, icon='search.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register('custom_list_menu')
def custom_list_menu():
	from commoncore import trakt
	lists = trakt.get_custom_lists()
	for l in lists['items']:
		kodi.add_menu_item({'mode': '%s_custom_list' % kodi.arg('media'), "api": {"name": "trakt", "method": "get_custom_list", "args": (l['ids']['slug'], kodi.arg('media'), )}}, {'title': l['name']}, icon='custom_list.png')
	kodi.eod(DEFAULT_VIEWS.LIST)
	
@kodi.register(['shows_genres', 'movies_genres'])
def sub_menu():
	if kodi.mode == 'shows_genres':
		from commoncore.trakt import SHOW_GENRES as GENRES
	else:
		from commoncore.trakt import MOVIE_GENRES as GENRES
	method = "get_trending_%s" % kodi.arg('media')
	mode = "%s_genre_list" % kodi.arg('media')
	for genre, slug in GENRES:
		kodi.add_menu_item({'mode': mode, "api": {"name": "trakt", "method": method, "args": ('genres', slug)}}, {'title': genre}, icon='genre.png')
	kodi.eod(DEFAULT_VIEWS.LIST)

@kodi.register(['shows_inprogress', 'movies_inprogress'])
def in_progress():
	import json
	from commoncore import trakt
	api = kodi.arg('api', decode='json')
	results = core.execute_api(locals(), api)
	if not results: 
		kodi.handel_error(kodi.get_name(), 'Not results found')
		return
	def make_show_directory(record):
		ids = json.loads(record[0])
		metadata = json.loads(record[1])
		episode = metadata['episode']
		show = metadata['show']['items']
		infoLabel =  metadata['episode']
		infoLabel['display'] = "%sx%s. %s - %s" % (infoLabel['season'], infoLabel['episode'], show['title'], infoLabel['title'])
		menu = kodi.ContextMenu()
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("show",)}})
		menu.add('Add to List', {"mode": "execute_api", "api": {"name": "trakt", "method": "add_to_list", "args": ("show", infoLabel['trakt_id'])}})
		kodi.add_menu_item({"mode": "search_streams", "media": "episode", "trakt_id": infoLabel['trakt_id'], "title": show['title'], "year": show['year'], "season": infoLabel['season'], "episode": infoLabel['episode'], "ids": ids}, infoLabel, menu=menu, in_progress=True, image=infoLabel['poster'])

	def make_movie_directory(record):
		ids = json.loads(record[0])
		infoLabel = json.loads(record[1])
		infoLabel['display'] = "%s (%s)" % (infoLabel['title'], infoLabel['year'])
		menu = kodi.ContextMenu()
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("movie",)}})
		menu.add('Add to List', {"mode": "execute_api", "api": {"name": "trakt", "method": "add_to_list", "args": ("movie", infoLabel['trakt_id'])}})
		kodi.add_menu_item({"mode": "search_streams", "media": "movie", "trakt_id": infoLabel['trakt_id'], "title": infoLabel['title'], "year": infoLabel['year'], "ids": ids}, infoLabel, menu=menu, in_progress=True, image=infoLabel['poster'])

	if kodi.mode == 'shows_inprogress':
		map(make_show_directory, results)
	else:
		map(make_movie_directory, results)
	kodi.eod(DEFAULT_VIEWS.SHOWS)	
	
@kodi.register(['shows_watchlist', 'shows_custom_list', 'shows_collection', 'shows_trending', 'shows_popular', 'shows_recommended', 'shows_anticipated', 'show_search_results', 'shows_genre_list'])
def tv_list():
	from commoncore import trakt
	api = kodi.arg('api', decode='json')
	if api['method'] == "search":
		query = kodi.get_property('search.query.refesh') if kodi.get_property('search.query.refesh') else api['args'][0]
		if query:
			kodi.clear_property('search.query')
			kodi.clear_property('search.query.refesh')
		else:
			query = kodi.dialog_input("Search for TV Shows")
		if query is None or query is False: 
			kodi.clear_property("search.query")
			return
		kodi.set_property('search.query', query)
		api['args'] = (query, 'show')
	results = core.execute_api(locals(), api)
	if not results: 
		kodi.handel_error(kodi.get_name(), 'Not results found')
	def make_show_directory(record):
		infoLabel = core.make_infolabel('show', record)
		ids = record['show']['ids'] if 'show' in record else record['ids']
		infoLabel['display'] = "%s (%s)" % (infoLabel['title'], infoLabel['year'])
		menu = kodi.ContextMenu()
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("show",)}})
		if kodi.mode in ['shows_watchlist', 'shows_custom_list']:
			menu.add('Remove From List', {"mode": "execute_api", "api": {"name": "trakt", "method": "remove_from_list", "args": ("show", api['args'][0], infoLabel['trakt_id']), "refresh": True, "confirm": "Confirm Remove from List?", "message": api['args'][0]}})
		else:
			menu.add('Add to List', {"mode": "execute_api", "api": {"name": "trakt", "method": "add_to_list", "args": ("show", infoLabel['trakt_id'])}})
		kodi.add_menu_item({"mode": "list_seasons", "trakt_id": infoLabel['trakt_id'], "ids": ids}, infoLabel, menu=menu, image=infoLabel['poster'])
	map(make_show_directory, results['items'])
	if 'total_pages' in results and results['total_pages'] > 1 and results['current_page'] < results['total_pages']:
		kodi.add_menu_item({"mode": kodi.mode, "api": api, "page": results['current_page'] + 1}, {"title": core.format_color("Next Page >>", 'green')}, icon="next_page.png")
	kodi.eod(DEFAULT_VIEWS.SHOWS)	

@kodi.register('list_seasons')
def list_seasons():
	from commoncore import trakt
	ids = kodi.arg('ids', decode='json')
	seasons = trakt.get_show_seasons(kodi.arg('trakt_id'))
	watched = trakt.get_season_watched(kodi.arg('trakt_id'))
	
	for season in seasons['items']:
		infoLabel = core.make_season_infolabel(season, ids)
		if not infoLabel: continue
		if 'aired_episodes' in season and infoLabel['season'] in watched and season['aired_episodes'] == len(watched[infoLabel['season']]):
			infoLabel['overlay'] = 7
			infoLabel['playcount'] = 1
		menu = kodi.ContextMenu()
		menu.add('Toggle Watched', {"mode": "toggle_watched", "api": {"name": "trakt", "method": "set_watched_state", "args": ("season", kodi.arg('trakt_id'), season, True), "refresh": True}})
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("season",)}})
		menu.add('Toggle Watched', {"mode": "toggle_watched", "api": {"name": "trakt", "method": "set_watched_state", "args": ("season", kodi.arg('trakt_id'), True, infoLabel['season']), "refresh": True}})
		kodi.add_menu_item({"mode": "list_episodes", "trakt_id": ids['trakt'], "season": infoLabel['season'], "ids": ids}, infoLabel, menu=menu, image=infoLabel['poster'])
	kodi.eod(DEFAULT_VIEWS.SEASONS)

@kodi.register('list_episodes')
def list_episodes():
	from commoncore import trakt
	ids = kodi.arg('ids', decode='json')
	show = trakt.get_show_info(ids['trakt'])
	episodes = trakt.get_season_info(kodi.arg('trakt_id'), kodi.arg('season'))
	watched = trakt.get_watched_history('shows')
	for episode in episodes['items']:
		infoLabel = core.make_infolabel('episode', episode, show=show, ids=ids, watched=watched)
		if not infoLabel: continue
		infoLabel['display'] = "%sx%s. %s" % (infoLabel['season'], infoLabel['episode'], infoLabel['title'])
		menu = kodi.ContextMenu()
		menu.add('Toggle Watched', {"mode": "toggle_watched", "api": {"name": "trakt", "method": "set_watched_state", "args": ("episode", infoLabel['trakt_id'], infoLabel['playcount'] == 0), "refresh": True}})
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("episode",)}})
		kodi.add_menu_item({"mode": "search_streams", "media": "episode", "trakt_id": infoLabel['trakt_id'], "title": infoLabel['showtitle'], "year": infoLabel['year'], "season": infoLabel['season'], "episode": infoLabel['episode'], "ids": ids}, infoLabel, menu=menu, image=infoLabel['poster'])
	kodi.eod(DEFAULT_VIEWS.EPISODES)

@kodi.register('my_calendar')
def calendars():
	from commoncore import trakt
	records = trakt.get_my_calendar()
	watched = trakt.get_watched_history('shows')
	for record in records['items']:
		show = record['show']
		ids = show['ids']
		episode = record['episode']
		infoLabel = core.make_infolabel('episode', episode, ids=ids, watched=watched)
		if infoLabel['season'] == 0 or infoLabel['season'] == 0: continue
		infoLabel['display'] = "%sx%s. %s - %s" % (infoLabel['season'], infoLabel['episode'], show['title'], infoLabel['title'])
		if not infoLabel: continue
		menu = kodi.ContextMenu()
		in_progress = trakt.is_inprogress('episode', infoLabel['trakt_id'])
		ids['episode_ids'] = episode['ids']
		menu.add('Toggle Watched', {"mode": "toggle_watched", "api": {"name": "trakt", "method": "set_watched_state", "args": ("episode", infoLabel['trakt_id'], infoLabel['playcount'] == 0), "refresh": True}})
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("episode",)}})		
		kodi.add_menu_item({"mode": "search_streams", "media": "episode", "trakt_id": infoLabel['trakt_id'], "title": show['title'], "year": show['year'], "season": infoLabel['season'], "episode": infoLabel['episode'], "ids": ids}, infoLabel, in_progress=in_progress, menu=menu, image=infoLabel['poster'])
	kodi.eod(DEFAULT_VIEWS.EPISODES)

@kodi.register(['movies_watchlist', 'movies_custom_list', 'moives_collection', 'movies_trending', 'movies_popular', 'movies_recommended', 'movies_anticipated', 'movie_search_results', 'movies_genre_list'])
def movie_list():
	from commoncore import trakt
	api = kodi.arg('api', decode='json')
	if api['method'] == "search":
		query = kodi.get_property('search.query.refesh') if kodi.get_property('search.query.refesh') else api['args'][0]
		if query:
			kodi.clear_property('search.query')
			kodi.clear_property('search.query.refesh')
		else:
			query = kodi.dialog_input("Search for Movies")
		if query is None or query is False: 
			kodi.clear_property("search.query")
			return
		kodi.set_property('search.query', query)
		api['args'] = (query, 'movie')
	results = core.execute_api(locals(), api)
	if not results: 
		kodi.handel_error(kodi.get_name(), 'Not results found')
	watched = trakt.get_watched_history('movies')
	def make_movie_directory(record):
		ids = record['movie']['ids'] if 'movie' in record else record['ids']
		infoLabel = core.make_infolabel('movie', record, watched=watched)
		infoLabel['display'] = "%s (%s)" % (infoLabel['title'], infoLabel['year'])
		menu = kodi.ContextMenu()
		menu.add('Toggle Watched', {"mode": "toggle_watched", "api": {"name": "trakt", "method": "set_watched_state", "args": ("movie", infoLabel['trakt_id'], infoLabel['playcount'] == 0), "refresh": True}})
		if kodi.mode in ['shows_watchlist', 'shows_custom_list']:
			menu.add('Remove From List', {"mode": "execute_api", "api": {"name": "trakt", "method": "remove_from_list", "args": ("movie", api['args'][0], infoLabel['trakt_id']), "refresh": True, "confirm": "Confirm Remove from List?", "message": api['args'][0]}})
		else:
			menu.add('Add to List', {"mode": "execute_api", "api": {"name": "trakt", "method": "add_to_list", "args": ("movie", infoLabel['trakt_id'])}})
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("movie",)}})
		kodi.add_menu_item({"mode": "search_streams", "media": "movie", "trakt_id": infoLabel['trakt_id'], "title": infoLabel['title'], "year": infoLabel["year"], "ids": ids}, infoLabel, menu=menu, image=infoLabel['poster'])
	map(make_movie_directory, results['items'])
	if 'total_pages' in results and results['total_pages'] > 1 and results['current_page'] < results['total_pages']:
		kodi.add_menu_item({"mode": kodi.mode, "api": api, "page": results['current_page'] + 1}, {"title": core.format_color("Next Page >>", 'green')}, icon="next_page.png")
	kodi.eod(DEFAULT_VIEWS.MOVIES)

@kodi.register('premiumize_folders')
def premiumize_folders():
	import re
	from commoncore import premiumize
	from scrapecore.scrapers.common import BaseScraper, QUALITY
	id = kodi.arg('id', '')
	folders = premiumize.list_folder(id)
	kodi.add_menu_item({"mode": "execute_api", "api": {"name": "premiumize", "method": "delete_folder", "refresh": True, "confirm": "Confirm Delete Folder(s)?", "message": "Delete all", "args": ('', )}}, {'title': "*** Delete All Files and Folders ***"}, icon="delete_all_files.png")
	for f in folders['content']:
		menu = kodi.ContextMenu()
		if f['type'] == 'folder':
			menu.add('Delete Folder', {"mode": "execute_api", "api": {"name": "premiumize", "method": "delete_folder", "args": (f['id'],), "refresh": True, "confirm": "Confirm Delete Folder(s)?", "message": f['name']}})
			kodi.add_menu_item({'mode': 'premiumize_folders', "id": f['id']}, {'title': f['name']}, menu=menu, icon="definition/folder.png")
		elif f['type'] == 'file':
			kodi.log(f)
			menu.add('Delete Item', {"mode": "execute_api", "api": {"name": "premiumize", "method": "delete_item", "args": (f['id'],), "refresh": True, "confirm": "Confirm Delete Folder(s)?", "message": f['name']}})
			display  = "PREMIUMIZE | %s | %s" % (core.format_color(core.format_size(f['size']), 'blue'), f['name'])
			if re.search("\.(txt|text|htm|html|info|ifo)$", f['name'], re.IGNORECASE):
				kodi.add_menu_item({"mode": "premiumize_direct", "name": f['name'], "type": "txt", "url": f['link']}, {"title": f['name'], "display": display}, menu=menu, icon='void.png')
			else:
				if re.search("\.(avi|mpg|mpeg|vob|mkv|mp4)$", f['name'], re.IGNORECASE):
					quality = QUALITY.r_map[BaseScraper().test_quality(f['name'])]
					icon="definition/%s.png" % quality.lower()
				else:
					icon=''
				kodi.add_video_item({"mode": "premiumize_direct", "name": f['name'], "type": "stream", "url": f['link']}, {"title": f['name'], "display": display}, icon=icon, menu=menu)
	kodi.eod(DEFAULT_VIEWS.STREAMS)

@kodi.register('premiumize_transfers')
def premiumize_transfers():
	import re
	from commoncore import premiumize
	from scrapecore.scrapers.common import BaseScraper, QUALITY
	id = kodi.arg('id', '')
	transfers = premiumize.list_transfers()
	kodi.add_menu_item({"mode": "execute_api", "api": {"name": "premiumize", "method": "clear_transfers", "refresh": True, "confirm": "Confirm Clear Transfers(s)?", "message": "Delete all transfers"}}, {'title': "*** Clear Finished Transfered ***"}, icon="clear_transfers.png")
	for t in transfers['transfers']:
		menu = kodi.ContextMenu()
		kodi.add_menu_item({'mode': 'void', "id": t['id']}, {'title': t['name']}, menu=menu, icon="definition/folder.png")
	kodi.eod(DEFAULT_VIEWS.STREAMS)

@kodi.register('premiumize_direct')
def premiumize_direct():
	if kodi.args['type'] == 'txt':
		import requests
		text = requests.get(kodi.args['url']).text
		kodi.dialog_textbox(kodi.args['name'], text)
	else:
		kodi.play_url(kodi.args['url'])

@kodi.register(['execute_api', 'set_default_view', 'toggle_watched', 'scrapecore_settings', 'commoncore_settings'])
def execute_api():
	api = kodi.arg('api', decode='json')
	if 'confirm' in api and api['confirm']:
		message = api['message'] if 'message' in api else ''
		if not kodi.dialog_confirm("Click Yes to proceed.", api['confirm'], message): return
	response = core.execute_api(globals(), api)
	if 'notify' in api and api['notify']:
		kodi.notify('API Response', response)
	if 'refresh' in api and api['refresh']:
		kodi.refresh()
		
@kodi.register('execute_command')
def execute_command():
	cmd = kodi.arg('xbmc', decode='json')
	cmd = "%s(%s)" % (cmd['command'], cmd['args'])
	kodi.run_command(cmd)

@kodi.register('auth_realdebrid')
def auth_realdebrid():
	from commoncore import realdebrid
	realdebrid.authorize()

@kodi.register('master_control')
def master_control():
	options = ["Send to Master Control", "Stream with Master Control", "Master Control Queue"]
	c = kodi.dialog_select("Master Control Menu", options)
	if c is False: return
	if c == 2:
		kodi.execute_url("plugin://master.control?mode=queue")
	elif c == 1:
		from scrapecore import scrapers
		resolved_url = scrapers.get_scraper_by_name(kodi.args['service']).resolve_url(kodi.args['raw_url'])
		if not resolved_url: return
		from mastercontrol import api as master_control
		stream_url = master_control.get_streaming_url(resolved_url)
		kodi.play_url(stream_url)
	elif c == 0:
		ids = kodi.arg('ids', decode='json')
		from commoncore import trakt
		from mastercontrol import api as master_control
		if kodi.args['media'] == 'movie':
			media='movie'
			title = "%s (%s)" % (kodi.args['title'], kodi.args['year'])
			filename = kodi.vfs.clean_file_name(title)
			destination = ''
		else:
			media='tvshow'
			destination = kodi.vfs.join(kodi.args['title'], "Season %s" % kodi.args['season'])
			title = "%s - S%02dE%02d" % (kodi.args['title'], int(kodi.args['season']), int(kodi.args['episode']))
			filename = kodi.vfs.clean_file_name(title)
			
		from scrapecore import scrapers
		resolved_url = scrapers.get_scraper_by_name(kodi.args['service']).resolve_url(kodi.args['raw_url'])
		if not resolved_url: return
		video = {
				"type": media,
				"filename": filename,
				"url": resolved_url,
				"title": title,
				"addon": kodi.get_id(),
				"destination": destination,
				"trakt_id": kodi.args['trakt_id']
		}
		kodi.log(video)
		response = master_control.enqueue(video)
		kodi.log(response)
		message = 'Failed Adding to Queue %s.' % (title)
		try:
			if response['status'] == 200:
				message = 'Added to Queue %s.' % (title)
		except:
			pass
		kodi.notify(kodi.get_name(), message)

@kodi.register("open_settings")
def addon_settings():
	kodi.open_settings(kodi.arg('addon_id'))
	
@kodi.register('search_streams')
def search_streams():
	from scrapecore import scrapers
	from scrapecore.scrapers.common import QUALITY
	results = scrapers.search(kodi.args['media'], kodi.args['title'], year=kodi.arg('year'), season=kodi.arg('season'), episode=kodi.arg('episode'), trakt_id=kodi.arg('trakt_id'))
	results = {v['raw_url']:v for v in results}.values()
	if len(results) == 0 :
		kodi.handel_error(kodi.get_name(), 'Not results found')
		return
	results.sort(reverse=True, key=lambda k: k['quality'])
	ids = kodi.arg('ids', decode='json')
	ids['season'] = kodi.arg('season')
	ids['episode'] = kodi.arg('episode')
	for r in results:
		menu = kodi.ContextMenu()
		menu.add('Set Default View', {"mode": "set_default_view", "api": {"name": "kodi", "method": "set_default_view", "args": ("stream",)}})
		quality = QUALITY.r_map[r['quality']]
		infoLabel = {"title": r['title'], "display": r['display']}
		menu.add('Master Control', {"mode": "master_control", "media": kodi.args['media'], "raw_url": r['raw_url'], "service": r['service'], "title": kodi.args['title'], "year": kodi.arg('year'), "season": kodi.arg('season'), "episode": kodi.arg('episode'), "trakt_id": kodi.arg('trakt_id')})
		if r['torrent']:
			menu.add('Add to Cloud', {"mode": "execute_api", "api": {"name": "premiumize", "method": "create_transfer", "args": (r['raw_url'],), "notify": True, "confirm": "Add to Premiumize Cloud?", "message": r['title']}})
		kodi.add_video_item({"mode": "play_stream", "raw_url": r['raw_url'], "title": kodi.args['title'],  "service": r['service'], "ids": ids, "media": kodi.args['media'], "trakt_id": kodi.args['trakt_id']}, infoLabel, menu=menu, icon="definition/%s.png" % quality.lower())
	kodi.eod(DEFAULT_VIEWS.STREAMS)
	
@kodi.register('play_stream')
def play_stream():
	from commoncore import trakt
	ids = kodi.arg('ids', decode='json')
	if kodi.args['media'] == 'episode':
		response = trakt.get_episode_info(ids['trakt'], ids['season'], ids['episode'])
		infoLabel = core.make_infolabel('episode', response['items'], ids=ids)
		infoLabel['title'] = "%s-S%02dE%02d-%s" % (kodi.args['title'], int(ids['season']), int(ids['episode']), infoLabel['title'])
	else:
		response = trakt.get_movie_info(ids['trakt'])
		infoLabel = core.make_infolabel('movie', response['items'])
	kodi.set_trakt_ids(ids)

	resume_point = trakt.trakt.query("SELECT current FROM playback_states WHERE media=? AND trakt_id=?", [kodi.args['media'], kodi.args['trakt_id']])
	if resume_point:
		infoLabel['resume_point'] = resume_point[0][0]
	from scrapecore import scrapers
	resolved_url = scrapers.get_scraper_by_name(kodi.args['service']).resolve_url(kodi.args['raw_url'])
	kodi.play_stream(resolved_url, metadata=infoLabel)
	
def on_play_back_stop():
	import json
	from commoncore import trakt
	try:
		percent = int(kodi.get_property('percent', 'service.fanart.proxy'))
		current_time = kodi.get_property('current_time', 'service.fanart.proxy')
		total_time = kodi.get_property('total_time', 'service.fanart.proxy')
	except:
		percent = 0		
		current_time = 0
		total_time = 0

	ids = kodi.arg('ids', decode='json')
	if kodi.args['media'] == 'episode':
		response = trakt.get_episode_info(ids['trakt'], ids['season'], ids['episode'])
		episode = core.make_infolabel('episode', response['items'], ids=ids)
		show = trakt.get_show_info(ids['trakt'])
		metadata = {"show": show, "episode": episode}
	else:
		response = trakt.get_movie_info(ids['trakt'])
		metadata = core.make_infolabel('movie', response['items'])
	if percent > 94:
		trakt.trakt.execute("UPDATE playback_states SET watched=1, total='', current='' WHERE media=? AND trakt_id=?", [kodi.args['media'], kodi.args['trakt_id']])
		trakt.trakt.commit()
	else:
		trakt.trakt.execute("REPLACE INTO playback_states(media, trakt_id, current, total, ids, metadata) VALUES(?,?,?,?,?,?)", [kodi.args['media'], kodi.args['trakt_id'], current_time, total_time, json.dumps(ids), json.dumps(metadata)])
		trakt.trakt.commit()
	kodi.unset_trakt_ids()
	#kodi.refresh()

kodi.on_playback_stop = on_play_back_stop
	
if __name__ == '__main__': kodi.run()


