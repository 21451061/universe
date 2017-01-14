#!/usr/bin/env python

def generate_podspec(env_id, cpu_quota, recorder_logdir, disable_hyperthreads="true"):
    with open('pod.yaml.template', 'r') as f:
        y = f.read()
        y = y.replace('__ENV_ID__', env_id)
        y = y.replace('__CPU_QUOTA__', cpu_quota)
        y = y.replace('__RECORDER_LOGDIR__', recorder_logdir)
        y = y.replace('__DISABLE_HYPERTHREADS__', str(disable_hyperthreads).lower())
    return y


if __name__ == '__main__':
    import sys
    if len(sys.argv) not in (4, 5):
        print('Usage: {} <env_id> <cpu_quota> <recorder_logdir> [disable_hyperthreads]'.format(sys.argv[0]))
        print('Got: {}'.format(' '.join(sys.argv)))
        sys.exit(1)
    print(generate_podspec(*sys.argv[1:]))
