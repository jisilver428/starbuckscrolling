# starbucks crolling project

-map_StarBucks.html
스타벅스 매장(서울,경기)을 마크로 표시한 시각화 파일.

-starbuck_map_geo.dbf
-starbuck_map_geo.hsp.csv
-starbuck_map_geo.shp
주소 데이터를 수정하고 Geocoder를 사용하여 만든 shp파일과 csv파일.

-starbucks.csv
크롤링을 통해 스타벅스 매장의 지점명과 주소를 얻어와서 주소 뒤에 붙어있던 번호를 삭제하고 주소만을 도출한 store_address_final필드를 위해 만든 csv파일.

-starbucks_2.csv
starbucks.csv파일에서 주소만을 얻어낸 필드를 통해, 행정구역 이름을 수정한 주소의 최종 csv파일.

-starbucks.py
webdriver을 사용하여 스타벅스 매장위치 페이지를 크롤링하고, 그 파일을 csv파일로 저장하는 python파일.
