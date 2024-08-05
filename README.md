

```
sudo ln -s /usr/share/alsa /usr/local/share/alsa
```

```
ALSA lib conf.c:4004:(snd_config_hooks_call) Cannot open shared library libasound_module_conf_pulse.so (/usr/local/lib/alsa-lib/libasound_module_conf_pulse.so: cannot open shared object file: No such file or directory)
```
```
sudo ln -s /usr/lib/x86_64-linux-gnu/alsa-lib /usr/local/lib/alsa-lib
```