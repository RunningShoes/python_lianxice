#!/usr/local/bin/python3
#-*-coding:utf-8-*-



import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS



# '''C'''
# url='https://api.github.com/search/repositories?q=language:C&sort=stars'
# data=requests.get(url)
# print("status_code:",data.status_code)
# dict_data=data.json()
# print(dict_data['total_count'])
# print(dict_data.keys())
# '''C++'''
# url='https://api.github.com/search/repositories?q=language:C++&sort=stars'
# data=requests.get(url)
# print("status_code:",data.status_code)
# dict_data=data.json()
# print(dict_data['total_count'])
# print(dict_data.keys())
'''PYTHON'''
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
data=requests.get(url)
print("status_code:",data.status_code)
dict_data=data.json()
print(dict_data['total_count'])
repository=dict_data['items']
print("Information in repository:\n")
for repo_dict in repository:
    print('name:',repo_dict['name'])
    print('Owner',repo_dict['owner']['login'])
    print('Stars',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    print('Description',repo_dict['description'])


'''pygal配置设置'''
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.truncate_label=15
my_config.width=1000
#
#

names,plot_dicts=[],[]
for i in repository[:25]:
    names.append(i['name'])
    plot_dict={
        'value': i['stargazers_count'],
        'label': str(i['description']),
        'xlink': i['html_url']
    }
    plot_dicts.append(plot_dict)
chart=pygal.Bar(my_config)
chart.add(' ',plot_dicts)
chart.title='Python Repository on Github'
chart.x_labels=names

# chart.render()
chart.render_to_file('python_repos.svg')

