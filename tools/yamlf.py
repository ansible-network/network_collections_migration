import os
from ruamel.yaml import YAML


def sequence_indent_four(s):
    # this will fail on direclty nested lists: {1; [[2, 3], 4]}
    levels = []
    ret_val = ''
    loop = 0
    linebreak = ''
    for line in s.splitlines(True):
        ls = line.lstrip()
        indent = len(line) - len(ls)
        if ls.startswith('- '):
            if loop > 1:
               linebreak = '\n'
            if not levels or indent > levels[-1]:
                levels.append(indent)
            elif levels:
                if indent < levels[-1]:
                    levels = levels[:-1]
            # same -> do nothing
        else:
            if levels:
                if indent <= levels[-1]:
                    while levels and indent <= levels[-1]:
                        levels = levels[:-1]

        if indent == 0:
            ret_val += linebreak + '' * len(levels) + line
        else:
            ret_val += '  ' * (len(levels) - 1) + line
        loop += 1

    return ret_val

def read_yaml_file(filename):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True

    data = None
    with open(filename, 'r') as stream:
        data = yaml.load(stream)

    with open(filename, 'w') as f:
        yaml.dump(data, f, transform=sequence_indent_four)


def read_meta_file(filename):
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.explicit_start = True
    yaml.indent(sequence=4, offset=2)

    data = None
    with open(filename, 'r') as stream:
        data = yaml.load(stream)

    with open(filename, 'w') as f:
        yaml.dump(data, f)

files = []
meta_files = []

for dirpath, dirname, filenames in os.walk('.'):
    for f in filenames:
        if '.yml' in f or '.yaml' in f:
            if 'meta' in dirpath:
                meta_files.append(os.path.join(dirpath, f))
                continue

            files.append(os.path.join(dirpath, f))

for f in files:
    read_yaml_file(f)

for f in meta_files:
    read_meta_file(f)
