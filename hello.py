a,b=10,20

print("# 교환 전 값")
print("a : {}, b : {}".format(a,b))
print("# 교환 전 id a's id:{}, b's id:{}".format(id(a),id(b)))
print()
a,b=b,a

print("# 교환 후 id a's id:{}, b's id:{}".format(id(a),id(b)))
