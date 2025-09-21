from bs4 import BeautifulSoup
from markdown import markdown
import numpy as np

class TableArray2:
    def convert_table_headers(html:str):
        scope = html.find("table").find("thead").find("tr")
        return np.array(scope, dtype=object)
    def convert_table_body(html:str):
        scope = html.find("table").find("tbody")
        grid = [[i for i in row.find_all("td")] for row in scope.find_all("tr")]
        array = np.array(grid, dtype=object)
        return array




# I could not think of a better method
class HTMLObject:
    def __init__(self, tag:str, content:str):
        self.tag = tag
        self.content = content
        self.kclass = []

    def add_class(self, *args):
        self.kclass.extend(args)

    def __str__(self):
        if len(self.kclass) > 0:
            return "<" + self.tag + " class='" + " ".join(self.kclass)+ "'" + ">" + self.content + "</" + self.tag + ">"
        else:
            return "<" + self.tag + ">" + self.content + "</" + self.tag + ">"

    __repr__ = __str__




def reformat_table(html:str, special_classes:dict=None):

    # convert html to arrays
    # we are assuming that there is one table in here
    headers = TableArray2.convert_table_headers(html)
    other_rows = TableArray2.convert_table_body(html)


    #print(other_rows)


    subject_offsets = []
    for idx, subject in np.ndenumerate(other_rows[:, 0]):
        if not len(tuple(subject.children)):
            subject_offsets.append(idx[0])
    else:
        subject_offsets.append(idx[0] + 1)


    for idx, section in np.ndenumerate(other_rows[:, 0:]):
        # Converting from <td></td> to <p></p>
        # lack of hidden internals moment
        section.name = "p"


    exit()


    # Pack into Array

    table_array = np.empty(shape=(len(subject_offsets) ,len(headers)), dtype=object)

    for idx, offset in enumerate(subject_offsets):
        if idx == len(subject_offsets) - 1: break
        table_array[idx+1, 0] = HTMLObject("th", str(other_rows[offset, 0]))

        for col in range(1,len(headers)):
            table_array[idx+1, col] = HTMLObject("td", "".join(other_rows[offset:subject_offsets[idx+1], col]))

    for idx, header in enumerate(headers):
        table_array[0, idx] = HTMLObject("th", "<p>" + header + "</p>")



    # Add Classes to Elements

    for idx, section in np.ndenumerate(table_array[0, :]):
        table_array[0, idx][0] = section.add_class("top")
    for idx, section in np.ndenumerate(table_array[-1, :]):
        table_array[-1, idx][0] = section.add_class("bottom")
    for idx, section in np.ndenumerate(table_array[:, 0]):
        table_array[idx, 0][0] = section.add_class("left")

    if not special_classes is None:
        for key, val in enumerate(special_classes):
            table_array[key][0] = table_array[key][0].add_class(val)

    # Convert array into table
    rows = []
    for idx, section in np.ndenumerate(table_array[:, 0]):
        rows.append("<tr>" + "".join([str(item) for item in table_array[idx]]) + "</tr>")

    table = "<table><thead>" + rows[0] + "</thead><tbody>" + "".join(rows[1:]) + "</tbody></table>"

    return table


if __name__ == "__main__":
    # convert md to html

    md = (file := open("../FAQ.md")).read()
    file.close()
    table_html = markdown(md, extensions=["markdown.extensions.tables"])
    table = reformat_table(table_html)
    print(table)
