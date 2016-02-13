from urllib.parse import urlparse


# input_file = input()
input_file = 'takovata-access.log'
input_line = 'dt="2016-02-11T12:26:50+00:00" ip="158.58.208.97" m="GET" p="http" url="/student/lecture/assignment/56a4ab616e8efb456bd29b06/" req_b="651" ref="http://python3.softuni.bg/student/lecture/56801633131b1642fba7379c/" ua="Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36" code="200" resp_t="0.126" resp_b="9220"'


def get_url_from_line(line):
    '''
        return url from string
    '''
    prefix = 'url="'
    start_of_url = line.find(prefix)
    end_of_url = line.find('"', start_of_url + len(prefix))
    return line[start_of_url + len(prefix):end_of_url].strip()


def get_resp_t_from_line(line):
    '''
        return resp_t from line
    '''
    prefix = 'resp_t="'
    start_of_resp_t = line.find(prefix)
    end_of_resp_t = line.find('"', start_of_resp_t + len(prefix))
    # print(start_of_resp_t)
    # print(end_of_resp_t)
    return line[start_of_resp_t + len(prefix):end_of_resp_t]


def get_url_withowth_get_param(url):
    url_parsed = urlparse(url)
    return url_parsed.path

# print(get_url_from_line(input_line))
# print(get_resp_t_from_line(input_line))


def main():
    urls_dict = dict()
    with open(input_file, encoding='utf-8') as f:
        for line in f:
            temp_url = get_url_from_line(line)
            # print(get_url_withowth_get_param(temp_url))
            # print(get_resp_t_from_line(line))
            url = get_url_withowth_get_param(temp_url)
            resp_t = get_url_from_line(line)
            urls_dict[url] = resp_t

if __name__ == '__main__':
    main()













'''
    ignore all url which end with /ws/
    check python csv reader
    python yield

'''
