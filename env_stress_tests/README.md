## Background

A shortage of CPU resources can cause environment dynamics to slow down (i.e.
in every minute of real time, less than 60 seconds elapse on the game clock,
and the environment appears to run in slow motion). This can drastically affect
the rate at which an agent accumulates reward, which is particularly worriesome
for racing envs, where OpenAI agents are ranked according to their average
reward per second.

This directory contains some utilites for testing the performance of an
environment given different CPU resource quotas.


## Run

`run/pod.yaml.template` defines a pod with an agent and environment containers,
configured so that the agent connects to the environment, spams "up arrow"
until one episode is complete, and then disconnects and causes both containers
to exit successfully. System diagnostics and the complete VNC and rewarder
traffic dumps are saved to disk for analysis.

`run/make-podspec.py` converts the template to a valid podspec by substituting
three variables:

- `__ENV_ID__`: the env id to test
- `__CPU_QUOTA__`: number of CPU cores to allocate for the env container (can be non-integer)
- `__RECORDER_LOGDIR__`: output directory for system diagnostics and protocol dumps

`run/run [env_id ...]` launches pods for each env id and each CPU_QUOTAS

## Transcode

VNC protocol dumps are tight-encoded, but tools (e.g.
`universe/example/readers/*`) expect RAW-encoded `.fbs` files.

[transcode](https://github.com/openai/go-vncdriver/tree/master/cmd/transcode),
dockerized as `docker.openai.com/transcode` is used to convert to RAW.

`transcode/run [base_dir ...]` finds all `server.fbs` files under `base_dir`
and creates sibling `server.raw.fbs` files (one transcode pod per file).
Transcoding is skipped if `server.raw.fbs` already exists (so this operation is
idempotent and not terribly slow).

## Screenshot

`universe/example/readers/screenshots.py` reads `server.raw.fbs` and saves
screenshots at 30 second intervals (according to the FBS timestamps). These can
be examined manually to measure the elapsed game time and calculate time
dilation.

# Conclusion

No time dilation is observed for the eight racing envs in `run/envs.txt` when
given one physical core of a `c4.8xlarge` (i.e. 1 CPU with hyperthreading
disabled).

