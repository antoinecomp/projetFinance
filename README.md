# projetFinance

## Requirements

Python3
Elastic search must have been downloaded, it can be done here :https://www.elastic.co/guide/en/elasticsearch/guide/current/running-elasticsearch.html

You may have things to donwload with pip3 install according to the error logs on your terminal while running Main.py

## Run

 To start it up in the foreground:

cd elasticsearch-<version>
./bin/elasticsearch

Then in your prefered web browser go to : http://localhost:9200/finance/crypto (don't work)

## TO-DO list

- Verify why the ema array of calculateAllEMA function which calculate the exponential arithmetic mean of the stocks is empty. Maybe we should add conditions on it.
- create an actionDecision function which verify SMA and EMA gives the same output or not to create an array of decision by stocks : buy or sell
- modulate the stocks we can have with different API with as much stocks we can.

## Files


### analyseValeurs.py

Is a draft file to show what we would like.

### ValueAnalyse.py 

Is a file that contains the financial method we need to take the actions.

exponential moving average is calculated from http://www.iexplain.org/ema-how-to-calculate/

### Main.py

### Util.py

### Message.py

### Elastic.py
