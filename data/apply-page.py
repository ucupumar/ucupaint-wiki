
content = '''
# Contributors
{contributors}
# Wiki's Contributors
{wiki_contributors}
# Sponsors
{sponsors}
'''


contributors = ''
wiki_contributors = ''
sponsors = ''

with open('contributors.csv', 'r') as f:
	lines = f.readlines()
	skip_first = True
	for line in lines:
		if skip_first:
			skip_first = False
			continue
		parts = line.strip().split(',')
		if len(parts) >= 3:
			login, display, url, pic = parts
			name = display.strip()
			if name == '':
				name = login.strip()
			contributors += f'* [{name}]({url.strip()})\n'

with open('contributors-wiki.csv', 'r') as f:
	lines = f.readlines()
	skip_first = True
	for line in lines:
		if skip_first:
			skip_first = False
			continue
		parts = line.strip().split(',')
		if len(parts) >= 3:
			login, display, url, pic = parts
			name = display.strip()
			if name == '':
				name = login.strip()
			wiki_contributors += f'* [{name}]({url.strip()})\n'

with open('sponsors.csv', 'r') as f:
	lines = f.readlines()
	for line in lines:
		parts = line.strip().split(',')
		if len(parts) >= 6:
			login, name, url, pic, since, price_usd, is_one_time, index_tier, public = parts
			is_public:bool = public.strip().lower() == 'true'
			if is_public:
				name = name.strip()
				if name == '':
					name = login.strip()
				sponsors += f'* [{name}]({url.strip()})\n'

content = content.format(contributors=contributors, wiki_contributors=wiki_contributors, sponsors=sponsors)

with open('../docs/01.12.contributors.md', 'w') as f:
	f.write(content)