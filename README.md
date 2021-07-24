# rasprophet - prophet rest service

## usage

```
docker run -it --rm -v "$PWD":/app -p 5000:5000 peterpeerdeman/docker-prophet-arm venv/bin/python3 -m flask run --host=0.0.0.0
curl -X POST --header "Content-Type: application/json" --data '{"ds":["2016-01-20","2016-01-21"],"y":[8.8999,9.9999],"p":2}' localhost:5000 | jq
```

## credits

inspired by https://github.com/thedataincubator/k8s-prophet
