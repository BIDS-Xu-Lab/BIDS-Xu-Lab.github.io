import re
import markdown
from pelican import signals

REGEX_YEAR = r"\b(\d{4})\b"

###########################################################
# Filters
###########################################################
def filter_person2html(person, template):
    '''
    Convert a person information to HTML by using a template

    Person is defined in the `people.json` file
    '''
    return template.render(p=person)


def filter_sort_mycates(categories, desc=True):
    '''
    Sort categories 
    '''
    return sorted(categories, key=lambda v: v[0], reverse=True)


def filter_md2html(s):
    '''
    Convert a Markdown string to HTML
    '''
    return markdown.markdown(s)


def filter_get_year(date_str):
    '''
    Get the year in a string
    '''
    ms = re.findall(REGEX_YEAR, date_str)

    if len(ms) == 0:
        return ''
    else:
        return ms[0]


def filter_pg2path(page_name):
    '''
    Get the path according to page_name
    '''
    if page_name == 'index':
        # ok it's the homepage
        return '.'
    else:
        return '..'


def filter_pg2act_nav(output_file, target):
    '''
    Get the active nav item
    '''
    if output_file == target:
        return 'active'

    return ''


def filter_astitle(s):
    '''
    Convert a string to title
    '''
    return s.title()


def filter_fmtdate(date_str, fmt='%Y-%m-%d'):
    '''
    Format a date string
    '''
    return date_str.strftime(fmt)


def add_all_filters(pelican):
    """Add (register) all filters to Pelican."""
    pelican.env.filters.update({"pg2path": filter_pg2path})
    pelican.env.filters.update({"person2html": filter_person2html})
    pelican.env.filters.update({"pg2act_nav": filter_pg2act_nav})
    pelican.env.filters.update({"md2html": filter_md2html})
    pelican.env.filters.update({"get_year": filter_get_year})
    pelican.env.filters.update({"sort_mycates": filter_sort_mycates})
    pelican.env.filters.update({"astitle": filter_astitle})
    pelican.env.filters.update({"fmtdate": filter_fmtdate})


###########################################################
# Plugin for make special pages
###########################################################


def register():
    """Plugin registration."""
    signals.generator_init.connect(add_all_filters)