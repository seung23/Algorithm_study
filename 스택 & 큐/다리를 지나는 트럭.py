from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    
    time = 0
    on_bridge_weight = 0
    
    while bridge:
        time += 1
        on_bridge_weight -= bridge.popleft()
        
        if truck_weights:
            if on_bridge_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
                on_bridge_weight += next_truck
            else:
                bridge.append(0)
    
    return time