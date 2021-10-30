import requests
import pygal
from operator import itemgetter

# Make and API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
status_code = ['']
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    if submission_r.status_code == 200:
        status_code[0] = submission_r.status_code
    else:
        status_code.append(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'label': response_dict['title'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'value': response_dict.get('descendants', 0),
        }
    submission_dicts.append(submission_dict)

if len(status_code) == 1:
    print("Loop status code: 200")
else:
    print("Loop status: ERROR")
submission_dicts = sorted(submission_dicts, key=itemgetter('value'),
                            reverse=True)
titles = []
for submission_dict in submission_dicts:
    titles.append(submission_dict['label'])

# Plot a bar chart showing most active discussions.
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config)
chart.title = 'Most-Active Discussions on Hacker News'
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('hn_submissions.svg')
