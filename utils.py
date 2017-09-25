import os
from urlparse import urlparse

def is_string_valid(p_string):
    """
    Method to validate whether the input string is a valid string or not
    :param p_string: Input string which needs to be validated
    :return: true if string is valid else false
    """
    if p_string == '':
        return False
    elif p_string is None:
        return False
    elif p_string.strip() == '':
        return False
    else:
        return True


def create_directory(p_Directory):
    """
    Method to create directory for each site for storing files
    :param p_Directory: Directory path which needs to be created
    :return: nothing
    """
    if not os.path.exists(p_Directory):
        print('creating directory: ' + p_Directory)
        os.makedirs(p_Directory)


def create_file(p_filename, p_filepath):
    """
    Method to create a file with the given name
    :param p_filename: Filename with which the file is to be created
    :param p_filepath: Path at which the file is to be created
    :return: nothing
    """

    if is_string_valid(p_filepath):
        p_filename += p_filepath

    if not os.path.isfile(p_filename):
        write_to_file(p_filename, '')

def write_to_file(p_filepath, p_data):
    """
    Method to write input data to file
    :param p_filepath: Path at which the file is to be created
    :param p_data: Data which needs to be written to the file
    :return: nothing
    """
    with open(p_filepath, 'w') as lfile:
        lfile.write(p_data)


def append_to_file(p_FilePath, p_Data):
    """
    Method to append data to file
    :param p_FilePath: File's complete path at which the file is there in which the data needs to be appended
    :param p_Data: Data to be appended to the file
    :return: Nothing
    """
    with open(p_FilePath, 'a') as LFile:
        LFile.write(p_Data + '\n')


def delete_contents_of_file(p_FilePath):
    """
    Method to delete contents of a file
    :param p_FilePath: File whose contents need to be deleted
    :return: Nothing
    """
    open(p_FilePath, 'w').close()


def convert_data_from_file_to_collection(p_FileName):
    """
    Method to get data from a file into a set
    :param p_FileName: Location of the file to read the contents from
    :return: Set containing the entries in the file
    """
    result = []
    # open the file in read mode
    with open(p_FileName, 'rt') as lfile:
        # iterate over each line in the file and add it to the set
        for line in lfile:
            # replace the newline character in line
            result.append(line.replace('\n', ''))
    # return the set after adding all the links from the file
    return result


def convert_data_from_collection_to_file(p_filename, p_data):
    """
    Method to convert data from a set to file
    :param p_filename: File in which the data from the set needs to be written
    :param p_data: Dataset from which the data needs to be written to a file
    :return: Nothing
    """
    # open the file in write mode
    with open(p_filename, "w") as lfile:
        # iterate over each item in set and add it to file
        for litem in p_data:
            litem = litem.encode('utf-8')
            lfile.write(str(litem) + "\n")


def get_domain_name_from_url(p_Url):
    """
    Method to return domain name from url
    :param p_Url: Url from which the domain name is to be retrieved
    :return: Domain name from the url
    """
    try:
        lresult = urlparse(p_Url).netloc
    except:
        lresult = ''

    try:
        lresult = lresult.split('.')
        lresult = lresult[-2] + '.' + lresult[-1]
    except:
        lresult = ''

    print lresult
    return lresult


def can_add_link(p_linkhref):

    """
    Method to check whether a link can be crawled by the crawler or not
    :param p_linkhref: href url from an anchor tag
    :return: True if the link can be crawled else False
    """

    if not is_string_valid(p_linkhref):
        return False

    # get the lowercase for href
    llinkhref = p_linkhref.lower()

    if ":" in llinkhref:
        return False

    if "#" in llinkhref:
        return False

    if "/wiki/" not in llinkhref:
        return False

    if (".jpeg" in llinkhref)or (".jpg" in llinkhref) or (".png" in llinkhref) \
            or (".gif" in llinkhref) or (".svg" in llinkhref):
        return False

    #if "main_page" in llinkhref:
    #    return False

    if "wikimediafoundation.org" in llinkhref:
        return False

    return True


def get_complete_url(p_domain, p_url):
    """
    Method to return the complete url with domain name
    :param p_domain: Domain name to be added to url
    :param p_url: Url
    :return: Url with domain name if it is not already there, else the same url
    """

    lresult = p_url

    if p_domain not in p_url:
        lresult = p_domain + p_url

    return lresult

def contains_keyword(p_keyword, p_anchortag):

    """
    Method used to check whether the keyword occurs in the anchor tag text or href
    :param p_keyword: Keyword to be searched for
    :param p_anchortag: Anchor tag in which the keyword is to be searched
    :return: Nothing
    """

    if not is_string_valid(p_keyword):
        return False

    llinkhref = p_anchortag.get("href")
    llinkstring = p_anchortag.string

    p_keyword = p_keyword.lower()

    if ( is_string_valid(llinkhref) and p_keyword not in llinkhref.lower() ) and \
            (is_string_valid(llinkstring) and p_keyword not in llinkstring.lower()):
        return False

    return True