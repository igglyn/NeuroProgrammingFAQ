import re
import os

if __name__ == "__main__":
    html = (file := open("FAQ.html")).read().replace("\n", " ")
    file.close()
    
    attribute_regex = re.compile(r"(\w+)=['\"](.+?)['\"]");

    # find all opening tags
    for element in re.findall(r"<\w+ (.+?)/?>", html):
        # matches all `(name)="(value)"`
        attrs = dict(re.findall(attribute_regex, element))
        # check if we have the right element with the size in its `style` attr
        if "id" in attrs and attrs["id"] == "content":
            style = attrs["style"]
            widths = re.findall(r"width: ?(\d+)px", style)
            heights = re.findall(r"height: ?(\d+)px", style)
            if len(widths) == 0 or len(heights) == 0:
                os._exit(1)
                
            print(f"{widths[-1]},{heights[-1]}")