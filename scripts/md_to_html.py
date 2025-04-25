from bs4 import BeautifulSoup
from markdown import markdown
import numpy as np

class TableArray:
    # TODO descriptions for each of these

    @staticmethod
    def __shorthand(html:str, search_type:str) -> list:
        return list(getattr(BeautifulSoup(str(html), "html.parser"), search_type).children)

    @staticmethod
    def __process(html:str, *levels:tuple[str]) -> list:
        # "python match cases are not meant for this"
        if len(levels) == 1:
            output = []
            for item in filter(lambda x: x != '\n', html):
                i = TableArray.__shorthand(item, levels[0])
                if len(i) > 1: output.append(i)
                elif len(i) == 1: output.append(str(i[0]))
                else: output.append("")
            return output
        elif len(levels) == 2:
            search = TableArray.__shorthand(html, levels[0])
            return TableArray.__process(search, levels[1])
        elif len(levels) == 3:
            output = []
            search = TableArray.__process(html, *levels[0:2])
            for item in search:
                output.append(TableArray.__process(item, levels[2]))
            return output

    @staticmethod
    def convert(html:str, *args:tuple[str], **kwargs) -> np.ndarray:
        if len(args) < 2+1 or len(args) > 3+1:
            raise ValueError(f"{len(args)-1} levels of nesting defined, the function only supports 2-3 levels of nesting")
        # object is required, it'll clip when editing later on
        return np.array(TableArray.__process(html, *args, **kwargs), dtype=object)

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




def reformat_table(html, special_classes:dict=None):

    # convert html to arrays
    headers = TableArray.convert(html, "tr", "th")
    other_rows = TableArray.convert(html, "tbody", "tr", "td")

    subject_offsets = []
    for idx, subject in np.ndenumerate(other_rows[:, 0]):
        if not subject == "":
            subject_offsets.append(idx[0])
    else:
        subject_offsets.append(idx[0] + 1)

    for idx, section in np.ndenumerate(other_rows[:, 0:]):
        if section == "": continue
        if type(section) is list: section = [str(item) for item in section]
        other_rows[idx] = "<p>" + "".join(section) + "</p>"




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
