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

- generate a message to a given number.
- install it on a RaspberryPi
- modulate the stocks we can have with different API with as much stocks as we can.
- are microdeals profitable ? Shouldn't we create a margin ?

### Machine Learning project :

Sometimes the prediction will be wrong. How can the program learn it was wrong ?
- each time we predict it will go up or down and the reverse appears, we should store a boolean value saying True/False...
And ..?

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
