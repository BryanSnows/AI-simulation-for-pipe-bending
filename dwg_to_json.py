import argparse
import ezdxf
import json

import json

data = {
    "tb": "weqrqwerqwefqwef",
    "ang": 30,
    "descripction": "brrrd brbdhj bshjdskks"
}

json_string = json.dumps(data, indent=2)
print(json_string)


def dwg_to_json(input_dwg_path, output_json_path):
    doc = ezdxf.readfile(input_dwg_path)
    entities = []

    for entity in doc.modelspace().query('*'):
        data = {
            'type': entity.dxftype(),
            'handle': entity.dxf.handle,
            'layer': entity.dxf.layer,
            'color': entity.dxf.color,
            'start_point': (entity.dxf.start.x, entity.dxf.start.y),
            'end_point': (entity.dxf.end.x, entity.dxf.end.y) if hasattr(entity.dxf, 'end') else None
        }
        entities.append(data)

    with open(output_json_path, 'w') as json_file:
        json.dump(entities, json_file, indent=2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert DWG to JSON')
    parser.add_argument('input_dwg', help='Path to the input DWG file')
    parser.add_argument('output_json', help='Path to the output JSON file')
    args = parser.parse_args()

    dwg_to_json(args.input_dwg, args.output_json)