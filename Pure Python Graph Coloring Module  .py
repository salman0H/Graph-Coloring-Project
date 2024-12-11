class GraphColoring:
    def __init__(self, provinces):
        """
        Initialize the graph coloring problem

        :param provinces: Dictionary of provinces and their neighboring provinces
        """
        self.graph = provinces
        self.colors = ['Green', 'Red', 'Blue', 'White']

    def is_safe(self, node, color, coloring):
        """
        Check if it's safe to color a node with a given color

        :param node: Node to color
        :param color: Color to assign
        :param coloring: Current coloring assignment
        :return: Boolean indicating if coloring is safe
        """
        # Check neighbors of the current node
        for neighbor in self.graph.get(node, []):
            if neighbor in coloring and coloring[neighbor] == color:
                return False
        return True

    def graph_coloring_util(self, coloring, nodes):
        """
        Recursive utility function for graph coloring

        :param coloring: Current coloring assignment
        :param nodes: Remaining nodes to color
        :return: Completed coloring or None
        """
        # If all nodes are colored, we're done
        if not nodes:
            return coloring

        # Select the first uncolored node
        node = nodes[0]

        # Try each color
        for color in self.colors:
            if self.is_safe(node, color, coloring):
                # Create a copy of current coloring and add this node's color
                new_coloring = coloring.copy()
                new_coloring[node] = color

                # Recursively color remaining nodes
                result = self.graph_coloring_util(new_coloring, nodes[1:])
                if result:
                    return result

        # No valid coloring found
        return None

    def solve(self):
        """
        Solve the graph coloring problem

        :return: A valid coloring or None
        """
        nodes = list(self.graph.keys())
        return self.graph_coloring_util({}, nodes)

    def print_coloring(self, coloring):
        """
        Print the coloring results

        :param coloring: Color assignment for provinces
        """
        for province, color in coloring.items():
            print(f"{province}: {color}")


# Provinces of Iran with their neighbors
iran_provinces = {
    'آذربایجان شرقی': ['آذربایجان غربی', 'اردبیل', 'زنجان'],
    'آذربایجان غربی': ['آذربایجان شرقی', 'اردبیل', 'کردستان', 'کرمانشاه'],
    'اردبیل': ['آذربایجان شرقی', 'آذربایجان غربی', 'زنجان', 'گیلان'],
    'اصفهان': ['تهران', 'یزد', 'فارس', 'مرکزی', 'سمنان', 'خراسان رضوی'],
    'البرز': ['تهران', 'قزوین', 'مرکزی', 'سمنان'],
    'ایلام': ['کرمانشاه', 'لرستان', 'خوزستان'],
    'بوشهر': ['فارس', 'هرمزگان'],
    'تهران': ['البرز', 'سمنان', 'مرکزی', 'قم', 'اصفهان'],
    'چهارمحال و بختیاری': ['فارس', 'اصفهان', 'خوزستان', 'لرستان'],
    'خراسان جنوبی': ['خراسان رضوی', 'سیستان و بلوچستان', 'کرمان', 'یزد'],
    'خراسان رضوی': ['خراسان شمالی', 'خراسان جنوبی', 'سمنان', 'اصفهان', 'یزد'],
    'خراسان شمالی': ['گلستان', 'خراسان رضوی', 'سمنان'],
    'خوزستان': ['چهارمحال و بختیاری', 'لرستان', 'ایلام', 'کهگیلویه و بویراحمد'],
    'زنجان': ['آذربایجان شرقی', 'اردبیل', 'قزوین', 'همدان'],
    'سمنان': ['تهران', 'البرز', 'مرکزی', 'اصفهان', 'خراسان رضوی', 'خراسان شمالی', 'گلستان'],
    'سیستان و بلوچستان': ['کرمان', 'هرمزگان', 'خراسان جنوبی'],
    'فارس': ['هرمزگان', 'کرمان', 'اصفهان', 'چهارمحال و بختیاری', 'بوشهر'],
    'قزوین': ['گیلان', 'زنجان', 'همدان', 'مرکزی', 'البرز'],
    'قم': ['تهران', 'مرکزی', 'اصفهان'],
    'کردستان': ['آذربایجان غربی', 'کرمانشاه', 'همدان'],
    'کرمان': ['یزد', 'هرمزگان', 'سیستان و بلوچستان', 'فارس'],
    'کرمانشاه': ['همدان', 'کردستان', 'آذربایجان غربی', 'ایلام'],
    'کهگیلویه و بویراحمد': ['خوزستان', 'فارس'],
    'گلستان': ['مازندران', 'سمنان', 'خراسان شمالی'],
    'گیلان': ['مازندران', 'اردبیل', 'قزوین'],
    'لرستان': ['همدان', 'مرکزی', 'خوزستان', 'چهارمحال و بختیاری'],
    'مازندران': ['گیلان', 'گلستان'],
    'مرکزی': ['قم', 'تهران', 'البرز', 'سمنان', 'اصفهان', 'همدان', 'لرستان'],
    'هرمزگان': ['کرمان', 'سیستان و بلوچستان', 'فارس', 'بوشهر'],
    'همدان': ['کردستان', 'کرمانشاه', 'زنجان', 'قزوین', 'مرکزی', 'لرستان'],
    'یزد': ['اصفهان', 'کرمان', 'خراسان جنوبی', 'خراسان رضوی']
}

# Khorasan Provinces with their neighbors
khorasan_provinces = {
    'قائن': ['نهبندان', 'طبس', 'سرایان'],
    'نهبندان': ['قائن', 'سربیشه', 'طبس'],
    'طبس': ['قائن', 'نهبندان', 'سرایان', 'درمیان'],
    'سرایان': ['قائن', 'طبس', 'فردوس', 'درمیان'],
    'درمیان': ['طبس', 'سرایان', 'بیرجند', 'خوسف'],
    'سربیشه': ['نهبندان', 'زیرکوه', 'خوسف'],
    'خوسف': ['درمیان', 'سربیشه', 'زیرکوه', 'بیرجند'],
    'زیرکوه': ['سربیشه', 'خوسف', 'فردوس'],
    'فردوس': ['سرایان', 'زیرکوه', 'آرینشهر', 'گزیک']
}


def main():
    # Solve Iran provinces coloring
    iran_graph = GraphColoring(iran_provinces)
    iran_coloring = iran_graph.solve()

    if iran_coloring:
        print("Iran Provinces Coloring:")
        iran_graph.print_coloring(iran_coloring)
    else:
        print("No valid coloring found for Iran provinces")

    # Solve Khorasan provinces coloring
    khorasan_graph = GraphColoring(khorasan_provinces)
    khorasan_coloring = khorasan_graph.solve()

    if khorasan_coloring:
        print("\nKhorasan Provinces Coloring:")
        khorasan_graph.print_coloring(khorasan_coloring)
    else:
        print("No valid coloring found for Khorasan provinces")


if __name__ == "__main__":
    main()