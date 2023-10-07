from geopy.geocoders import Nominatim
import geopy

def get_current_location_address(latitude,longitude):
    # 創建一個地理位置解析器
    geolocator = Nominatim(user_agent="my_app")

    # 使用geopy來獲取地址
    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    if location:
        custom_info = [
            location.raw.get('address', {}).get('country', ''),
            location.raw.get('address', {}).get('city', ''),
            location.raw.get('address', {}).get('suburb', ''),
            location.raw.get('address', {}).get('road', ''),
            location.raw.get('address', {}).get('house_number', '')
        ]
        return custom_info
    else:
        return None

if __name__ == '__main__':
    current_address = get_current_location_address()
    if current_address:
        print(type(current_address))
        print(f'當前位置：{current_address}')
    else:
        print('無法獲取當前位置信息')
