from clinic_manager.models import Order
from warehouse.models import ProcessQueue
from dispatcher.models import DispatchQueue
from ha.models import LocationData
from tsp_solver.greedy import solve_tsp
import json


def update_process_queue():
    orders = Order.objects.filter(order_status='Queued for Processing').order_by('priority_level', 'date_ordered')
    ProcessQueue.objects.all().delete()

    queue_no =0

    for order in orders:
        p = ProcessQueue()
        p.order_id = order.id
        p.queue_no = queue_no
        queue_no += 1
        p.save()

    print('Process queue updated')


def update_dispatch_queue():
    orders = Order.objects.filter(order_status='Queued for Dispatch').order_by('priority_level', 'date_ordered')
    DispatchQueue.objects.all().delete()

    queue_no = 0

    for order in orders:
        q = DispatchQueue()
        q.order_id = order.id
        q.queue_number = queue_no
        queue_no += 1
        q.save()

    print('Dispatch queue updated')


def generate_distance_matrix(locations):

    distance_matrix = []
    for location in LocationData.objects.all():
        distance_matrix.append(json.loads(location.distances)['distances'])

    print(distance_matrix)
    result_matrix = [[]]
    for i in range(1, len(locations)):
        result_matrix_element = []
        for j in range(i):
            id_j = locations[j][0]
            id_i = locations[i][0]
            if id_j == id_i:
                distance = 0
            else:
                distance = distance_matrix[max(id_i - 1, id_j - 1)][min(id_j - 1, id_i - 1)]
            result_matrix_element.append(distance)

        result_matrix.append(result_matrix_element)

    return result_matrix


def route_plan(orders):

    all_locations = [(8, "Queen Mary Hospital Drone Port")]
    for locations in orders:
        if (LocationData.objects.get(name=locations.order_clinic).id, locations.order_clinic) not in all_locations:
            all_locations.append((LocationData.objects.get(name=locations.order_clinic).id, locations.order_clinic))
    # Add last location to be Queen Mary Hospital
    all_locations.append((8, "Queen Mary Hospital Drone Port"))

    distance_matrix = generate_distance_matrix(all_locations)

    result = solve_tsp(distance_matrix, endpoints=(0, len(distance_matrix)-1))

    result_names = []
    for c in result:
        result_names.append(all_locations[c][1])

    print(result_names)
    return result_names[1:]
