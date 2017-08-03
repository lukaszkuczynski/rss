# ES image

## Troubleshooting

In case of having error during ES image startup (boostrap checks)
```bash
max virtual memory areas vm.max_map_count [65530] likely too low, increase to at least [262144]
```
You need to increase your mem in you docker-engine host
```bash
sudo sysctl -w vm.max_map_count=262144
```