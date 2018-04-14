import json


class Preset:
    def __init__(self, commodity):
        self.commodity = commodity
        self.weigher_list = []
        self.total_weight = 0

    def __eq__(self, other):
        return type(other) is Preset and self.commodity == other.commodity

    def __str__(self):
        string = "Preset: {}".format(self.commodity)
        string += "\nWeighers: {}".format(', '.join("Weigher {}".format(weigher) for weigher in self.weigher_list))
        string += "\nTotal KG Per Hour: {}\n".format(self.total_weight)
        return string

    def add_weigher(self, weigher):
        self.weigher_list.append(weigher)

    def add_weight(self, weight):
        self.total_weight += weight


preset_dict = {
    '1': 'Gold',
    '2': 'Silver',
    '3': 'Diamond',
    '4': 'Platinum',
    '7': 'Titanium',
    '8': 'Steel',
    '9': 'Zinc',
    '10': 'Uranium',
    '11': 'Mercury',
    '14': 'Phosphorous',
    '17': 'Sodium'
}


def parse_preset_json(file_name):
    try:
        with open(file_name) as json_file:
            data = json_file.read()
            response_dict = json.loads(data)
            output_dict = {}
            for weigher, weight in response_dict.items():
                weigher_details = weigher.split('_')
                preset_value = preset_dict[weigher_details[4]]
                if preset_value not in output_dict:
                    output_dict[preset_value] = Preset(preset_value)
                output_dict[preset_value].add_weigher(weigher_details[2])
                output_dict[preset_value].add_weight(weight)
            return output_dict
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    preset_details = parse_preset_json('sample_response.json')
    if preset_details:
        for preset in preset_details:
            print(preset_details[preset])
