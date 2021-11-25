import requests
import json



def get_board_id_by_external_link(link):
    board = requests.get(link + '.json')
    id_board = json.loads(board.text)['id']
    return id_board

def get_lists_id_by_border_id(id_board):
    lists = requests.get('https://api.trello.com/1/boards/' + id_board + '/lists?')
    json_lists = json.loads(lists.text)
    id_lists = [list['id'] for list in json_lists]
    return id_lists

def get_tasks_id_by_list_id(id_list):
    tasks = requests.get('https://api.trello.com/1/lists/' + id_list +'/cards?')
    json_tasks = json.loads(tasks.text)
    id_tasks = [task['id'] for task in json_tasks]
    return id_tasks

def get_task_by_id(id_task):
    task = requests.get('https://api.trello.com/1/cards/' + id_task)
    task_json = json.loads(task.text)
    return task_json