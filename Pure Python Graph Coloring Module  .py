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
    'آذربایجان شرقی': ['آذربایجان غربی', 'اردبیل', 'زنجان'], #1
    'آذربایجان غربی': ['آذربایجان شرقی', 'اردبیل', 'کردستان', 'کرمانشاه'], #2
    'اردبیل': ['آذربایجان شرقی', 'آذربایجان غربی', 'زنجان', 'گیلان'], #3
    'اصفهان': ['تهران', 'یزد', 'فارس', 'مرکزی', 'سمنان', 'خراسان رضوی'], #4
    'البرز': ['تهران', 'قزوین', 'مرکزی', 'سمنان'], #5
    'ایلام': ['کرمانشاه', 'لرستان', 'خوزستان'], #6
    'بوشهر': ['فارس', 'هرمزگان'], #7
    'تهران': ['البرز', 'سمنان', 'مرکزی', 'قم', 'اصفهان'], #8
    'چهارمحال و بختیاری': ['فارس', 'اصفهان', 'خوزستان', 'لرستان'], #9
    'خراسان جنوبی': ['خراسان رضوی', 'سیستان و بلوچستان', 'کرمان', 'یزد'], #10
    'خراسان رضوی': ['خراسان شمالی', 'خراسان جنوبی', 'سمنان', 'اصفهان', 'یزد'], #11
    'خراسان شمالی': ['گلستان', 'خراسان رضوی', 'سمنان'], #12
    'خوزستان': ['چهارمحال و بختیاری', 'لرستان', 'ایلام', 'کهگیلویه و بویراحمد'], #13
    'زنجان': ['آذربایجان شرقی', 'اردبیل', 'قزوین', 'همدان'], #14
    'سمنان': ['تهران', 'البرز', 'مرکزی', 'اصفهان', 'خراسان رضوی', 'خراسان شمالی', 'گلستان'], #15
    'سیستان و بلوچستان': ['کرمان', 'هرمزگان', 'خراسان جنوبی'], #16
    'فارس': ['هرمزگان', 'کرمان', 'اصفهان', 'چهارمحال و بختیاری', 'بوشهر'], #17
    'قزوین': ['گیلان', 'زنجان', 'همدان', 'مرکزی', 'البرز'], #18
    'قم': ['تهران', 'مرکزی', 'اصفهان'], #19
    'کردستان': ['آذربایجان غربی', 'کرمانشاه', 'همدان'], #20
    'کرمان': ['یزد', 'هرمزگان', 'سیستان و بلوچستان', 'فارس'], #21
    'کرمانشاه': ['همدان', 'کردستان', 'آذربایجان غربی', 'ایلام'], #22
    'کهگیلویه و بویراحمد': ['خوزستان', 'فارس'], #23
    'گلستان': ['مازندران', 'سمنان', 'خراسان شمالی'], #24
    'گیلان': ['مازندران', 'اردبیل', 'قزوین'], #25
    'لرستان': ['همدان', 'مرکزی', 'خوزستان', 'چهارمحال و بختیاری'], #26
    'مازندران': ['گیلان', 'گلستان'], #27
    'مرکزی': ['قم', 'تهران', 'البرز', 'سمنان', 'اصفهان', 'همدان', 'لرستان'], #28
    'هرمزگان': ['کرمان', 'سیستان و بلوچستان', 'فارس', 'بوشهر'], #29
    'همدان': ['کردستان', 'کرمانشاه', 'زنجان', 'قزوین', 'مرکزی', 'لرستان'], #30
    'یزد': ['اصفهان', 'کرمان', 'خراسان جنوبی', 'خراسان رضوی'] #31
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