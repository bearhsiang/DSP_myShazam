# myShazam

## How to build data set?
1. Put all the songs in ```./song_source```
2. ```make build```

You could also download ```musics``` and ```corresponding files``` at [here](https://drive.google.com/open?id=1n3FMoOwPJrbQlWyF1pF1WiOHc18GDVfE ).

## How to record?
```
make record TARGET=[target]
```
This would create recording file```target.wav```

## How to test a recording?
```
make test SOUR=[source file] TARGET=[target]
```
Which take ```source file``` as input, create 
* ```./usr/target_data``` 
* ```./usr/target.center``` 
* ```./usr/target.hash``` 
* ```./usr/target.sort``` 
* ```./rec/target.result```
