import re

# v1.0.0.20220616
def jsonIndentLimit(jsonString, indent, limit):
	regexPattern = re.compile(f'\n({indent}){{{limit}}}(({indent})+|(?=(}}|])))')
	return regexPattern.sub('', jsonString)

if __name__ == '__main__':
	jsonString = '''{
	"layer1": {
		"layer2": {
			"layer3_1": [
				{
					"x": 1,
					"y": 7
				},
				{
					"x": 0,
					"y": 4
				},
				{
					"x": 5,
					"y": 3
				},
				{
					"x": 6,
					"y": 9
				}
			],
			"layer3_2": "string"
		}
	}
}'''
	print(jsonIndentLimit(jsonString, '\t', 3))
