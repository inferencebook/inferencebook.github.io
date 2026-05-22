import sys, json
sys.stdout.reconfigure(encoding='utf-8')
path = 'c:/Users/james/Documents/GitHub/inferencebook.github.io/notebooks/chapter_07_frequentist_linear_regression.ipynb'
with open(path, encoding='utf-8') as f:
    nb = json.load(f)
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell['source'])
    ctype = cell['cell_type']
    print(f'--- cell {i} ({ctype}) ---')
    print(src[:400])
    print()
