import pandas as pd
from datetime import *
df = pd.read_csv('Final_correct_data.csv')
df.drop_duplicates(inplace=True)

flights = []
airport_connection = {}
flightid = {}
max_flow = 0
arrival_time = datetime.strptime('12:00 AM', '%I:%M %p')

for trip in df.values:
    departure = datetime.strptime(trip[0],"%I:%M %p")
    arrival = datetime.strptime(trip[3], "%I:%M %p")
    if trip[1] in airport_connection:
        airport_connection[trip[1]].append([trip[4],departure,arrival,trip[8]])
    else:
        airport_connection[trip[1]] = [[trip[4],departure,arrival,trip[8]]]
    flightid[trip[8]] = trip[9]  

def max_flight_capacity(connection,current_airport,AT):
    if current_airport == 'John F. Kennedy International Airport JFK':
        flights.append(connection)
        return

    for row in airport_connection[current_airport]:
        if AT < row[1]:
            max_flight_capacity(connection + [row[3]],row[0],row[2])
        else:
            pass

max_flight_capacity([],'Los Angeles International Airport LAX',latest_AT)

 
for flight in flights:
    for ride in flight:
        flow = float('inf')
        flow = min(flow, flightid[ride])
    max_flow += flow
    for ride in flight:
        flightid[ride] -= flow
print("The maximum capacity of flights from LAX to JFK on 6th January is %d" %max_flow)
