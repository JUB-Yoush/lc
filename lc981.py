class TimeMap:

	def __init__(self):
		self.store = {}
		

	def set(self, key: str, value: str, timestamp: int) -> None:
		if key not in self.store:
			self.store[key] = []
		self.store[key].append([timestamp,value]) 
		

	def get(self, key: str, timestamp: int) -> str:
		# get value that is the most <=timestamp
		res = ''
		values = self.store.get(key,[])
  
		l = 0
		r = len(values) -1
		while l <= r:
			m = (l+r)//2
			if values[m][0] <= timestamp:
				res = values[m][1]
				l = m + 1
			else:
				r = m -1
			
		return res


test = TimeMap()
test.set("foo","bar",1)
test.get("foo",1)
test.get("foo",3)
test.set("foo","bar2",4)
test.get("foo",4)
test.get("foo",5)