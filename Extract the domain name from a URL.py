"""
Extract the domain name from a URL
"""

def domain_name(url):

    if str("www") in str(url):
        strips = []
        ops_on = url
        for runs in range(url.count(".")):
            add = ops_on.find(".")
            ops_on = ""
            ops_on = ops_on + url[add+1:]
            strips.append(add)

        return url[strips[0] + 1:strips[0] + strips[1] + 1]

    else:
        strips = []
        strips.append(url.find("//") + 2)
        strips.append(url.find(".com"))
        return url[strips[0]:strips[1]]
