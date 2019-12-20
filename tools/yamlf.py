import os
from ruamel.yaml import YAML


def sequence_indent_four(s):
    ret_val = ''
    first = False
    for line in s.splitlines(True):
        line_break = ''
        ls = line.lstrip()
        indent = len(line) - len(ls)
        if indent > 0:
            line = line[2:]
        if ls.startswith('- ') and (': ' in ls or ls.rstrip().endswith(':')):
            if first:
                line_break += '\n'
            first = True

        ret_val += line_break + line

    return ret_val

def read_yaml_file(filename):
    yaml = YAML()
    yaml.explicit_start = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.allow_unicode = True

    data = None
    with open(filename, 'r') as stream:
        data = yaml.load(stream)

    with open(filename, 'w') as f:
        yaml.dump(data, f, transform=sequence_indent_four)


def read_meta_file(filename):
    yaml = YAML()
    yaml.explicit_start = True
    yaml.indent(mapping=2, sequence=4, offset=2)

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
            if 'meta' in dirpath or 'vars' in dirpath:
                meta_files.append(os.path.join(dirpath, f))
                continue

            files.append(os.path.join(dirpath, f))

for f in files:
    read_yaml_file(f)

for f in meta_files:
    read_meta_file(f)
