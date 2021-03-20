

import ast

a="print('hello world')"
code=ast.parse(a,mode='exec')
exec(compile(code,filename='',mode='exec'))

print(ast.dump(code))

b='1+2'
c=ast.parse(b,mode='eval')
print(eval(compile(c,'',mode='eval')))

class NodeVisitor(ast.NodeVisitor):
    def visit_Str(self,tree):
        print('{}'.format(tree.s))

class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self,tree):
        return ast.Str("String: " + tree.s)

NodeTransformer().visit(code)
NodeVisitor().visit(code)
