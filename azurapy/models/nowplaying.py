

# def wrapper(func):
#     def wrap(*args, **kwargs):
#         print('mm')
#         result = func(*args, **kwargs)
#         print('ugu')
#         print(result)
#     return wrap


# @wrapper
def get():
    return '/nowplaying', 'GET'


def get_by_station(station_id: int):
    return f'/nowplaying/{station_id}'
