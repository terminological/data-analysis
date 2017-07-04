import yaml
import pprint

def main():
    file = open("static/data/table.yaml")
    tmp = yaml.load(file)
    pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(tmp)
    file.close()
    rows = tmp["rows"]
    for col in tmp["columns"]:
        pp.pprint(col)
        key = list(col.keys())[0]
        pp.pprint(key)
        row_instance = col.get(key)
        i = 0
        tmp2 = {}
        for row in row_instance:
            if type(row) is dict:
                tmp2.update(row)
            else:
                tmp2[rows[i]] = row
            i += 1
        col[key] = tmp2   
    pp.pprint(tmp)

main()   