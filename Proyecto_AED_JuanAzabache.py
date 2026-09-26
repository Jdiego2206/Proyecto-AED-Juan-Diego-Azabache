from manim import *
import numpy as np

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.pos = np.array([0, 0, 0])

class BSTAnimation(Scene):
    def construct(self):
        # Título
        title = Text("Binary Search Tree", font_size=50, color=BLUE)
        subtitle = Text("Algoritmo y Estructura de Datos", font_size=30, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        self.wait(0.3)
        
        # Crear el BST
        bst = BSTNode(50)
        values_to_insert = [30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
        
        tree_mobjects = {}
        
        # Sección 1: INSERCIÓN
        section1 = Text("Fase 1: Inserción de Nodos", font_size=36, color=BLUE)
        section1.to_corner(UP + LEFT)
        self.play(Write(section1))
        self.wait(0.5)
        
        # Mostrar raíz
        root_circle = Circle(radius=0.35, color=BLUE, fill_opacity=0.8)
        root_circle.move_to([0, 2, 0])
        root_text = Text("50", font_size=24, color=WHITE)
        root_text.move_to([0, 2, 0])
        
        self.play(Create(root_circle), Write(root_text))
        tree_mobjects[50] = (root_circle, root_text)
        bst.pos = np.array([0, 2, 0])
        bst.mobject_circle = root_circle
        bst.mobject_text = root_text
        
        self.wait(0.5)
        
        # Insertar valores
        for i, value in enumerate(values_to_insert):
            self.insert_to_tree(bst, value, tree_mobjects)
            self.wait(0.25)
        
        self.wait(0.5)
        self.play(FadeOut(section1))
        self.wait(0.3)
        
        # Sección 2: BÚSQUEDA EXITOSA
        section2 = Text("Fase 2: Búsqueda Exitosa", font_size=36, color=GREEN)
        section2.to_corner(UP + LEFT)
        self.play(Write(section2))
        self.wait(0.3)
        
        search_label = Text("Buscando: 25", font_size=28, color=YELLOW)
        search_label.to_corner(UP + RIGHT)
        self.play(Write(search_label))
        self.wait(0.3)
        
        self.search_value(bst, 25, tree_mobjects)
        self.wait(0.5)
        
        self.play(FadeOut(search_label), FadeOut(section2))
        self.wait(0.3)
        
        # Sección 3: BÚSQUEDA FALLIDA
        section3 = Text("Fase 3: Búsqueda No Exitosa", font_size=36, color=RED)
        section3.to_corner(UP + LEFT)
        self.play(Write(section3))
        self.wait(0.3)
        
        search_label2 = Text("Buscando: 15", font_size=28, color=ORANGE)
        search_label2.to_corner(UP + RIGHT)
        self.play(Write(search_label2))
        self.wait(0.3)
        
        self.search_value(bst, 15, tree_mobjects)
        self.wait(0.5)
        
        self.play(FadeOut(search_label2), FadeOut(section3))
        self.wait(0.3)
        
        # Sección 4: OTRA BÚSQUEDA EXITOSA
        section4 = Text("Fase 4: Búsqueda Adicional", font_size=36, color=BLUE_C)
        section4.to_corner(UP + LEFT)
        self.play(Write(section4))
        self.wait(0.3)
        
        search_label3 = Text("Buscando: 70", font_size=28, color=YELLOW)
        search_label3.to_corner(UP + RIGHT)
        self.play(Write(search_label3))
        self.wait(0.3)
        
        self.search_value(bst, 70, tree_mobjects)
        self.wait(0.5)
        
        self.play(FadeOut(search_label3), FadeOut(section4))
        self.wait(0.3)
        
        # Sección 5: ELIMINACIÓN
        section5 = Text("Fase 5: Eliminación de Nodo", font_size=36, color=RED)
        section5.to_corner(UP + LEFT)
        self.play(Write(section5))
        self.wait(0.3)
        
        delete_label = Text("Eliminando: 25", font_size=28, color=RED)
        delete_label.to_corner(UP + RIGHT)
        self.play(Write(delete_label))
        self.wait(0.3)
        
        # Resaltar el nodo a eliminar
        if 25 in tree_mobjects:
            circle_to_delete, text_to_delete = tree_mobjects[25]
            self.play(circle_to_delete.animate.set_fill(RED, opacity=1), run_time=0.4)
            self.wait(0.3)
            self.play(FadeOut(circle_to_delete), FadeOut(text_to_delete), run_time=0.5)
            self.wait(0.3)
        
        self.play(FadeOut(delete_label), FadeOut(section5))
        self.wait(0.3)
        
        # Sección 6: BÚSQUEDA DESPUÉS DE ELIMINAR
        section6 = Text("Fase 6: Verificación Post-Eliminación", font_size=36, color=PURPLE)
        section6.to_corner(UP + LEFT)
        self.play(Write(section6))
        self.wait(0.3)
        
        search_label4 = Text("Buscando: 25 (eliminado)", font_size=28, color=ORANGE)
        search_label4.to_corner(UP + RIGHT)
        self.play(Write(search_label4))
        self.wait(0.3)
        
        # Esta búsqueda fallará ahora
        self.search_value(bst, 25, tree_mobjects, deleted=True)
        self.wait(0.5)
        
        self.play(FadeOut(search_label4), FadeOut(section6))
        self.wait(0.5)
        
        # Propiedades del BST
        properties = Text("Propiedades del BST", font_size=32, color=BLUE)
        prop1 = Text("• Hijo izq < Padre < Hijo der", font_size=20)
        prop2 = Text("• Búsqueda: O(log n) en promedio", font_size=20)
        prop3 = Text("• Inserción: O(log n) en promedio", font_size=20)
        
        props_group = VGroup(properties, prop1, prop2, prop3)
        props_group.arrange(DOWN, buff=0.3)
        props_group.move_to(ORIGIN)
        
        self.play(FadeOut(*[mob for mob in self.mobjects if mob not in self.mobjects[:10]]))
        self.play(Write(props_group))
        self.wait(1.5)
        
        self.play(FadeOut(props_group))
        self.wait(0.5)
        
        # Créditos
        credits_title = Text("Proyecto: Binary Search Tree", font_size=36, color=BLUE)
        credits_author = Text("Juan Diego Azabache Liñan", font_size=32, color=GRAY)
        credits_course = Text("CS2023 - Algoritmos y Estructuras de Datos", font_size=24, color=LIGHT_GRAY)
        
        credits_group = VGroup(credits_title, credits_author, credits_course)
        credits_group.arrange(DOWN, buff=0.3)
        credits_group.move_to(ORIGIN)
        
        self.play(FadeIn(credits_group))
        self.wait(2)
    
    def get_tree_position(self, node, parent_pos, is_left, depth):
        """Calcula posición del nodo en el árbol"""
        x_offset = 2.5 / (2 ** (depth + 1))
        if is_left:
            node_x = parent_pos[0] - x_offset
        else:
            node_x = parent_pos[0] + x_offset
        node_y = parent_pos[1] - 1.0
        return np.array([node_x, node_y, 0])
    
    def insert_to_tree(self, node, value, tree_mobjects, parent=None, is_left=True, depth=0):
        """Inserta un valor en el BST y anima el proceso"""
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
                pos = self.get_tree_position(node.left, node.pos, True, depth)
                node.left.pos = pos
                self.animate_node_creation(node, node.left, tree_mobjects, pos)
            else:
                self.insert_to_tree(node.left, value, tree_mobjects, node, True, depth + 1)
        else:
            if node.right is None:
                node.right = BSTNode(value)
                pos = self.get_tree_position(node.right, node.pos, False, depth)
                node.right.pos = pos
                self.animate_node_creation(node, node.right, tree_mobjects, pos)
            else:
                self.insert_to_tree(node.right, value, tree_mobjects, node, False, depth + 1)
    
    def animate_node_creation(self, parent, new_node, tree_mobjects, pos):
        """Anima la creación de un nuevo nodo"""
        circle = Circle(radius=0.35, color=GREEN, fill_opacity=0.7)
        circle.move_to(pos)
        text = Text(str(new_node.value), font_size=20, color=WHITE)
        text.move_to(pos)
        
        parent_pos = parent.pos
        line = Line(parent_pos, pos, color=GRAY, stroke_width=2)
        
        self.play(Create(line), run_time=0.2)
        self.play(Create(circle), Write(text), run_time=0.2)
        
        new_node.mobject_circle = circle
        new_node.mobject_text = text
        tree_mobjects[new_node.value] = (circle, text)
    
    def search_value(self, node, target, tree_mobjects, path_nodes=None, deleted=False):
        """Busca un valor y anima el camino de búsqueda"""
        if path_nodes is None:
            path_nodes = []
        
        if node.value not in tree_mobjects:
            # Nodo fue eliminado
            if not deleted:
                found_text = Text("No existe", font_size=24, color=RED)
                found_text.to_corner(DOWN + RIGHT)
                self.play(Write(found_text))
                self.wait(0.5)
                self.play(FadeOut(found_text))
            return
        
        circle, text = tree_mobjects[node.value]
        path_nodes.append((circle, text))
        
        # Resaltar nodo actual
        original_color = circle.fill_color
        self.play(circle.animate.set_fill(YELLOW, opacity=1), run_time=0.2)
        self.wait(0.3)
        
        if node.value == target:
            # Encontrado
            self.play(circle.animate.set_fill(GREEN, opacity=1))
            found_text = Text("¡Encontrado!", font_size=24, color=GREEN)
            found_text.to_corner(DOWN + RIGHT)
            self.play(Write(found_text))
            self.wait(0.5)
            self.play(FadeOut(found_text))
            
            # Restaurar color
            for c, t in path_nodes:
                self.play(c.animate.set_fill(BLUE if c == tree_mobjects[50][0] else GREEN, opacity=0.8), run_time=0.1)
        elif target < node.value:
            if node.left:
                self.play(circle.animate.set_fill(original_color, opacity=0.8), run_time=0.2)
                self.search_value(node.left, target, tree_mobjects, path_nodes, deleted)
            else:
                # No encontrado
                self.play(circle.animate.set_fill(RED, opacity=1))
                not_found = Text("No existe", font_size=24, color=RED)
                not_found.to_corner(DOWN + RIGHT)
                self.play(Write(not_found))
                self.wait(0.5)
                self.play(FadeOut(not_found))
                self.play(circle.animate.set_fill(original_color, opacity=0.8), run_time=0.2)
        else:
            if node.right:
                self.play(circle.animate.set_fill(original_color, opacity=0.8), run_time=0.2)
                self.search_value(node.right, target, tree_mobjects, path_nodes, deleted)
            else:
                # No encontrado
                self.play(circle.animate.set_fill(RED, opacity=1))
                not_found = Text("No existe", font_size=24, color=RED)
                not_found.to_corner(DOWN + RIGHT)
                self.play(Write(not_found))
                self.wait(0.5)
                self.play(FadeOut(not_found))
                self.play(circle.animate.set_fill(original_color, opacity=0.8), run_time=0.2)
