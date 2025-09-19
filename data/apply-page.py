
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
	for line in lines:
		parts = line.strip().split(', ')
		if len(parts) >= 3:
			login, url, pic = parts
			contributors += f'* [{login}]({url})\n'

with open('contributors-wiki.csv', 'r') as f:
	lines = f.readlines()
	for line in lines:
		parts = line.strip().split(', ')
		if len(parts) >= 3:
			login, url, pic = parts
			wiki_contributors += f'* [{login}]({url})\n'

with open('sponsors.csv', 'r') as f:
	lines = f.readlines()
	for line in lines:
		parts = line.strip().split(', ')
		if len(parts) >= 6:
			login, url, pic, since, price_usd, is_one_time = parts
			sponsors += f'* [{login}]({url})\n'

content = content.format(contributors=contributors, wiki_contributors=wiki_contributors, sponsors=sponsors)

with open('../docs/01.12.contributors.md', 'w') as f:
	f.write(content)