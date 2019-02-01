import sys

la, lb, list_operator = sys.argv, [], ""
la.pop(0)

# function for check if li is sort
def is_sort(li) :
	if (len(li) == 0) :
		return False
	i = 1
	tmp = li[0]
	while (i < len(li) and tmp <= li[i]) :
		tmp = li[i]
		i += 1
	if (i == len(li)):
		return True
	else :
		return False

# parse list to int
def parse() :
	i = 0
	while i < len(la) :
		la[i] = int(la[i])
		i += 1

# function for assigned task into la
def sort () :
	mini = min(la)
	if (len(lb) > 0 and is_sort(la)) :
		return pa()
	if (len(la) == 1 and len(lb) > 0) :
		return pa()
	elif (len(la) > 1 and la[0] != mini) :
		return ra()
	elif (len(la) > 1 and la[0] == mini) :
		return pb()
	else  :
		return 'rien'

# swap la[0] la[1]
def sa() :
	la[0], la[1] = la[1], la[0]
	return "sa"

# swap lb[0] lb[1]
def sb () :
	lb[0], lb[1] = lb[1], lb[0]
	return "sb"

# sa + sb
def sc ():
	la[0], la[1] = la[1], la[0]
	lb[0], lb[1] = lb[1], lb[0]
	return "sc"

# push lb[0] in la[0]
def pa () :
	la.insert(0, lb[0])
	lb.pop(0)
	return "pa"

# push la[0] in lb[0]
def pb () :
	lb.insert(0, la[0])
	la.pop(0)
	return "pb"

# rot la[0] -> end la
def ra () :
	la.insert(len(la), la[0])
	la.pop(0)
	return "ra"

# rot lb[0] -> end lb
def rb () :
	lb.insert(len(lb), lb[0])
	lb.pop(0)
	return "rb"

# ra + rb
def rr () :
	ra()
	rb()
	return "rr"

# revese ra
def rra () :
	la.insert(0, la[len(la)-1])
	la.pop(len(la)-1)
	return "rra"

# revese rb
def rrb () :
	lb.insert(0, lb[len(lb)-1])
	lb.pop(len(lb)-1)
	return "rrb"

# rra + rrb
def rrr () :
	rra()
	rrb()
	return "rrr"

# main function
def push_swap() :
	global la, lb, list_operator
	parse()
	ii = 0
	while (is_sort(la) == False or len(lb) > 0) :
		state = sort()
		# print "{{",state, "}}\nla", la," \nlb", lb, "\n"
		list_operator += state + " "
	print list_operator[0:len(list_operator)-1]
push_swap()
