#!/usr/bin/env python

def generate_podspec(fbs_in, fbs_out):
    with open('pod.yaml.template', 'r') as f:
        y = f.read()
        y = y.replace('__FBS_IN__', fbs_in)
        y = y.replace('__FBS_OUT__', fbs_out)
    return y


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} <fbs_in> <fbs_out>'.format(sys.argv[0]))
        print('Got: {}'.format(sys.argv))
        sys.exit(1)
    print(generate_podspec(sys.argv[1], sys.argv[2]))
