def create_empty_block():
	from datetime import datetime
	
	dic = {
		"subject": "",
		"creation_time": datetime.now().strftime("%Y%m%d%H%M%S"),
		"due_date": "00000000000000",
		"tags": [],
		"level": "Easy",
		"status": "Not Started Yet",
		"completeness": "0",
		"comment": "",
		"number": -1
	}

	empty_block = EventBlock(dic)
	return empty_block

class EventBlock():
	def __init__(self, kwarg):
		self.subject = kwarg["subject"]
		self.number = kwarg["number"]
		self.creation_time = kwarg["creation_time"]
		self.due_date = kwarg["due_date"]
		self.tags = kwarg["tags"]
		self.level = kwarg["level"]
		self.status = kwarg["status"]
		self.completeness = kwarg["completeness"]
		self.comment = kwarg["comment"]

	def __str__(self):
		_str = ""

		_str += f"EventBlock:\n"
		_str += f"        subject = {self.subject}\n"
		_str += f"         number = {self.number}\n"
		_str += f"  creation_time = {self.creation_time}\n"
		_str += f"       due_date = {self.due_date}\n"
		_str += f"           tags = {self.tags}\n"
		_str += f"          level = {self.level}\n"
		_str += f"         status = {self.status}\n"
		_str += f"   completeness = {self.completeness}\n"
		_str += f"        comment = {self.comment}\n"
		_str += f"\n"

		return _str


	def set_block(self, subject, creation_time, due_date, tags, level, status, completeness, comment):
		self.subject = subject
		self.creation_time = creation_time
		self.due_date = due_date
		self.tags = tags
		self.level = level
		self.status = status
		self.completeness = completeness
		self.comment = comment

class MainData():
	def __init__(self, data):
		tags = set()
		blocks = []
		for i, d in enumerate(data):
			if d["status"] != "deleted":
				for tag in d["tags"]:
					tags.add(tag)
			d["number"] = i
			blocks.append(EventBlock(d))

		self.tags = tags
		self.blocks = blocks

	def save(self):
		lst = []
		for d in self.blocks:
			dic = {}
			dic["subject"] = d.subject
			dic["creation_time"] = d.creation_time
			dic["due_date"] = d.due_date
			dic["tags"] = d.tags
			dic["level"] = d.level
			dic["status"] = d.status
			dic["completeness"] = d.completeness
			dic["comment"] = d.comment

			lst.append(dic)
		import json
		with open("maindata.json", 'w') as f:
			json.dump(lst, f)

'''
def Sort(blocks, tag = 'ALL', sort_by = "default", status = "dafault"):
	lst = []

	for block in blocks:
		if (tag in block.tags or tag == 'ALL') and (status == block.status or status == "default"):
			lst.append(block)
	if sort_by == "default":
		lst.sort(key = lambda d: d.creation_time)
	elif sort_by == "due_date":
		lst.sort(key = lambda d: d.due_date)
	elif sort_by == "completion":
		lst.sort(key = lambda d: d.completeness)
	return lst
'''