
def create_description(license):

    descr = "The " + license['name'] + " license is a "

    if license['copyleft']:
        descr += "copyleft"
    else:
        descr += "permissive"

    descr += ", "

    if license['status']['dfsg']:
        descr += "DFSG free"
    else:
        descr += "DFSG non-free"

    descr += ", and GPL "

    if license['status']['gpl-compat']:
        descr += "compatable"
    else:
        descr += "incomptable"

    descr += " license, "

    if license['packages'] != []:
        descr += "with"
    else:
        descr += "without"

    descr += " packages in the archive."

    return descr
