import json


class Preset:
    """
    Preset object for each commodity/item
    """
    def __init__(self, commodity):
        """
        Constructor for Preset class to create object
        :param commodity: (str) commodity/item
        """
        self.commodity = commodity
        self.weigher_list = []
        self.total_weight = 0

    def __eq__(self, other):
        """
        Check if 2 objects of type Preset are equal
        :param other: (Preset) preset object
        :return: (bool) True if 2 objects are same else False
        """
        return type(other) is Preset and self.commodity == other.commodity

    def __str__(self):
        """
        To print the object
        :return: (str) object as string
        """
        string = "Preset: {}".format(self.commodity)
        string += "\nWeighers: {}".format(', '.join("Weigher {}".format(weigher) for weigher in self.weigher_list))
        string += "\nTotal KG Per Hour: {}\n".format(self.total_weight)
        return string

    def add_weigher(self, weigher):
        """
        Add the weigher to the list
        :param weigher: (str) weigher of the preset
        :return: void
        """
        self.weigher_list.append(weigher)

    def add_weight(self, weight):
        """
        Add the weight weighed by the weigher to the total weight of the commodity
        :param weight: (float) weight
        :return: void
        """
        self.total_weight += weight


# preset mapping the commodities with id number
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
    """
    Parse the preset json file
    :param file_name: (str) json file name which is in same directory as this file
    :return: (dict) mapping of the commodity with preset object
    """
    try:
        with open(file_name) as json_file:
            data = json_file.read()
            # store the data of json to dictionary
            response_dict = json.loads(data)

            # dict for mapping commodity to preset object
            output_dict = {}

            for weigher, weight in response_dict.items():
                weigher_details = weigher.split('_')
                # getting the value of the preset from the preset_dict using the id
                preset_value = preset_dict[weigher_details[4]]

                if preset_value not in output_dict:
                    # create a preset object if the commodity/item is not present in the output dict
                    output_dict[preset_value] = Preset(preset_value)
                # add the weigher to the preset object
                output_dict[preset_value].add_weigher(weigher_details[2])
                # add the weight with the total weight for the preset object
                output_dict[preset_value].add_weight(weight)
            return output_dict
    except Exception as e:
        # should be used log for debug purpose, instead of using print method
        print(e)
        # return empty dict if any exceptions occur
        return {}


# driver code
if __name__ == '__main__':
    preset_details = parse_preset_json('sample_response.json')
    # to check if any items are there in the returned dict
    if preset_details:
        for preset in preset_details:
            print(preset_details[preset])
