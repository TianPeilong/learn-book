class Evaluate:
    # different
    def solution(self, expression):
        # to post
        opstrs = set(['+', '-', '*', '/'])
        priorities = {'(':1, '+':1, '-':1, '*':2, '/':2}
        post_exp = []
        ops = []
        for exp in expression:
            if exp == '(':
                ops.append(exp)
            elif exp in opstrs:
                while ops and ops[-1] != '(' and priorities[ops[-1]] > priorities[exp]:
                    post_exp.append(ops.pop())
                ops.append(exp)
            elif exp == ')':
                while ops[-1] != '(':
                    post_exp.append(ops.pop())
                ops.pop()
            else:
                post_exp.append(exp)
        while ops:
            post_exp.append(ops.pop())
        # cal post
        cal_stack = []
        for exp in post_exp:
            if exp == '+':
                op2 = cal_stack.pop()
                op1 = cal_stack.pop()
                cal_stack.append(op1 + op2)
            elif exp == '-':
                op2 = cal_stack.pop()
                op1 = cal_stack.pop()
                cal_stack.append(op1 - op2)
            elif exp == '*':
                op2 = cal_stack.pop()
                op1 = cal_stack.pop()
                cal_stack.append(op1 * op2)
            elif exp == '/':
                op2 = cal_stack.pop()
                op1 = cal_stack.pop()
                cal_stack.append(op1 / op2)
            else:
                cal_stack.append(float(exp))
        return cal_stack.pop()

    
expressions = ['(', '1', '+', '2', '-', '1', ')', '/', '2', '+', '(', '19', '*', '3', '/', '5', ')']
s = Evaluate()
print(s.solution(expressions))