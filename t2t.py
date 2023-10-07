from geopy.geocoders import Nominatim

def get_current_location_address(latitude, longitude):
    # 创建一个地理位置解析器
    geolocator = Nominatim(user_agent="my_app")

    # 使用geopy获取地址
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    if location:
        address = location.raw.get('address', {})
        custom_info = [
            address.get('country', ''),
            address.get('city', ''),
            address.get('suburb', ''),
            address.get('road', ''),
            address.get('house_number', '')
        ]
        return custom_info
    else:
        return None

if __name__ == '__main__':
    latitude = 40.7128  # 替换为实际的纬度
    longitude = -74.0060  # 替换为实际的经度
    current_address = get_current_location_address(latitude, longitude)
    if current_address:
        print(type(current_address))
        print(f'当前位置：{current_address}')
    else:
        print('无法获取当前位置信息')
