fd = open("day11/in.txt")
fd2 = open("day11/table.txt")
import math
import re


table = {}
loop = 0
while (True):
    line = fd2.readline()
    m = re.match(r"== .*\s(\d+) ==",line)
    assert m
    loop = int(m.group(1))
    table[loop] = {}
    for _ in range(4):
        line = fd2.readline()
        m = re.match(r"Monkey (\d) inspected items (\d+) times.",line)
        assert m
        table[loop][int(m.group(1))] = int(m.group(2))
    
    if loop == 10000:
        break
    fd2.readline()



#items = {}
div_by= 3

def rules(val):
 return math.floor(val/div_by)

def multold(current,par):
    return current*current

def multpar(current,par):
    return current*par

def addpar(current,par):
    return current + par

class Monkey:

    def __init__(self):
        self.my_items = []

    def parse(self,fd):
        line = fd.readline()
        m = re.match(r"Monkey (\d+):", line)
        if not m:
            return None
        assert m
        self.name = m.group(1)
        self.handled = 0
        line = fd.readline()
        m = re.match(r".*:\s(\d.*\d)", line)
        assert m
        for i in m.group(1).split(','):
            val = int(i.strip())
            it = {"level" : val, "name" : val, "op" :0}
            # items[val] = it
            self.my_items += [it]
        line = fd.readline()
        self.operation = None
        
        m = re.match(r".*=\sold\s\*\sold.*", line)
        if m:
            self.operation = multold
            self.operation_value = None
        m = re.match(r".*=\sold\s\*\s(\d+)", line)
        if m:
            self.operation = multpar
            self.operation_value = int(m.group(1))
        m = re.match(r".*=\sold\s\+\s(\d+)", line)
        if m:
            self.operation = addpar
            self.operation_value = int(m.group(1))
        assert self.operation
        
        line = fd.readline()
        m = re.match(r".*Test: divisible by (\d+)", line)
        assert m
        self.test_operation = m.group(1)
        
        line = fd.readline()
        m = re.match(r".*monkey (\d+)", line)
        assert m
        self.throw_true = int(m.group(1))

        line = fd.readline()
        m = re.match(r".*monkey (\d+)", line)
        assert m
        self.throw_false = int(m.group(1))

        return self

    def catch(self,item):
        self.my_items += [item]

    def p(self):
        return [(i["level"])  for i in self.my_items]

    def oper(self):
        return [(i["op"])  for i in self.my_items]
    def do(self):
        for count in range(len(self.my_items)):
            self.handled += 1
            item = self.my_items[0]
            del(self.my_items[0])
            item["op"] += 1
            item["level"] = (self.operation)(item["level"],self.operation_value)
            item["level"] = rules("level")

            if  item["level"] % int(self.test_operation) == 0:
                monkeys[self.throw_true].catch(item)
            else:
                monkeys[self.throw_false].catch(item)

monkeys = []
while (fd.readable()):
    m = Monkey().parse(fd)
    if not m:
        break
    monkeys.append(m)
    fd.readline()

for i in range(10):
    for monkey in monkeys:
        monkey.do()
    if i in table:
        is_ok = True
        for m in table[i]:
            oo = table[i][m]
            if oo != monkeys[m].handled:
                print(f"Monkey {m} exp{oo} got {monkeys[m].handled}")
                is_ok = False
        if not is_ok:
            break

[print(f"Monkey {m.name}: {m.p()}") for m in monkeys]
a= sorted([m.handled for m in monkeys])
print(a)
print(a[-1]*a[-2])
pass




