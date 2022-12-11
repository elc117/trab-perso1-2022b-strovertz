import geocoder
import folium

f = geocoder.ip("2804:7f6:8087:6301::1")

myAddress = f.latlng

print(myAddress)

my_map1 = folium.Map(location=myAddress,
                    zoom_start=12)


folium.CircleMarker(location=myAddress,
                    radius=50, popup="numsie").add_to(my_map1)

folium.Marker(myAddress, 
              popup="yok").add_to(my_map1)

my_map1.save("my_map.html")
