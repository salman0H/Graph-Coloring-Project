import tkinter as tk
from tkinter import ttk, messagebox

class GraphColoring:
    def __init__(self, provinces):
        self.graph = provinces
        self.colors = ['Green', 'Red', 'Blue', 'White']

    def is_safe(self, node, color, coloring):
        for neighbor in self.graph.get(node, []):
            if neighbor in coloring and coloring[neighbor] == color:
                return False
        return True

    def graph_coloring_util(self, coloring, nodes):
        if not nodes:
            return coloring

        node = nodes[0]

        for color in self.colors:
            if self.is_safe(node, color, coloring):
                new_coloring = coloring.copy()
                new_coloring[node] = color

                result = self.graph_coloring_util(new_coloring, nodes[1:])
                if result:
                    return result

        return None

    def solve(self):
        nodes = list(self.graph.keys())
        return self.graph_coloring_util({}, nodes)

# Data for provinces
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

def display_coloring(result, title):
    result_window = tk.Toplevel()
    result_window.title(title)

    tree = ttk.Treeview(result_window, columns=("Province", "Color"), show='headings', height=20)
    tree.heading("Province", text="Province")
    tree.heading("Color", text="Color")
    tree.column("Province", width=200)
    tree.column("Color", width=100)

    # Add provinces and their colors to the treeview
    for province, color in result.items():
        tree.insert("", tk.END, values=(province, color), tags=(color,))

    # Define tag styles for colors
    style = ttk.Style()
    style.configure("Green.Treeview", foreground="green")
    style.configure("Red.Treeview", foreground="red")
    style.configure("Blue.Treeview", foreground="blue")
    style.configure("White.Treeview", foreground="gray")

    for color in ["Green", "Red", "Blue", "White"]:
        tree.tag_configure(color, foreground=color.lower())

    tree.pack(fill=tk.BOTH, expand=True)

def solve_coloring(graph, title):
    solver = GraphColoring(graph)
    result = solver.solve()

    if result:
        display_coloring(result, title)
    else:
        messagebox.showerror("Error", "No valid coloring found")

def main():
    def start_coloring():
        if selected_map.get() == 1:
            solve_coloring(iran_provinces, "Iran Provinces Coloring")
        elif selected_map.get() == 2:
            solve_coloring(khorasan_provinces, "Khorasan Provinces Coloring")

    root = tk.Tk()
    root.title("Graph Coloring")

    selected_map = tk.IntVar()

    tk.Label(root, text="Choose a map to color:", font=('Helvetica', 14)).pack(pady=10)
    tk.Radiobutton(root, text="Iran Provinces", variable=selected_map, value=1).pack()
    tk.Radiobutton(root, text="Khorasan Provinces", variable=selected_map, value=2).pack()

    tk.Button(root, text="Start Coloring", command=start_coloring).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
