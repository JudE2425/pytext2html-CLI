# Set source file from command line argument
from sys import argv

script, source_file_path, to_file = argv
#source_file_path = '/home/mage/Downloads/c0.txt' # Not needed d/t argv

template = '''<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>{{title}}</title>
	</head>
	<body class='bodyStyle'>{{body}}</body>
	<style>{{style}}</style>
</html>'''

br = '<br>'
#I like 'p' tags better d/t spacing.
p = '<p>'

title = ''

style = '''
.bodyStyle {
	background: white;
	color:	black;
	margin-left: 20%;
	margin-right: 20%;
	font-size: medium;
}
'''

src_file_string = None
with open(source_file_path) as source_file:
	src_file_string = source_file.read()

src_file_string = src_file_string.replace('\r', '')

body = src_file_string.replace('\n', p)
body = src_file_string.replace('\n\n', p)
body = body.replace('\t', p + '&emsp;'*3)


html = template.replace('{{body}}', body)
html = html.replace('{{title}}', title)
html = html.replace('{{style}}', style)

#dest_file_path = source_file_path + '.html' #dest file now set by argv

with open(to_file, 'tw') as dest_file:
	dest_file.write(html)
