
import heartbeat as hb 
dataset = hb.get_data("data.csv")
hb.process(dataset, 0.75, 100)
bpm = hb.measures['bpm']
print (hb.measures.keys())

