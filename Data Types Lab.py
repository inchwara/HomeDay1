def data_type(s):
	s_type = type(s)
	if s_type == str:
		return len(s)

	elif s_type ==bool:
		return s

	elif s_type ==int:
		if s == 100:
			return 'equal to 100'
		elif s < 100:
			return 'less than 100'

		else:
			return 'more than 100'

	elif s_type == list:
		try:
			if s[2]:
				return s[2]
		except Exception as e:
			return None
	else:
		return 'no value'