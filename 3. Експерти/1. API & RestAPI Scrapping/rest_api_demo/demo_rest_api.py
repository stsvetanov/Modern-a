import requests

def _url(path):
    return 'https://todo.example.com' + path

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
        })


resp = add_task("Take out trash")
if resp.status_code != 201:
    raise ApiError('Cannot create task: {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))

resp = get_tasks()
if resp.status_code != 200:
    raise ApiError('Cannot fetch all tasks: {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['id'], todo_item['summary']))