
import prepare_data
d = prepare_data.build_all_data()
for i, a in enumerate(d['agenda']):
    print(i, a['time'], a['activity'], a.get('phase'), a.get('category'))
