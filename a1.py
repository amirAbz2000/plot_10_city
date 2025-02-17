# pip install kaleido



import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go



cities = [
    {"name": "تهران", "lat": 35.6892, "lon": 51.3890, "population": 9000000},
    {"name": "مشهد", "lat": 36.2605, "lon": 59.6168, "population": 3600000},
    {"name": "اصفهان", "lat": 32.6546, "lon": 51.6679, "population": 2200000},
    {"name": "شیراز", "lat": 29.5918, "lon": 52.5837, "population": 2000000},
    {"name": "تبریز", "lat": 38.0800, "lon": 46.2919, "population": 1850000},
    {"name": "کرج", "lat": 35.8400, "lon": 50.9391, "population": 1840000},
    {"name": "اهواز", "lat": 31.3183, "lon": 48.6692, "population": 1400000},
    {"name": "قم", "lat": 34.6399, "lon": 50.8759, "population": 1350000},
    {"name": "کرمانشاه", "lat": 34.3142, "lon": 47.0650, "population": 1150000},
    {"name": "ارومیه", "lat": 37.5520, "lon": 45.0761, "population": 1100000}
]


fig = go.Figure()


# تعریف مرزهای ایران در قالب GeoJSON
iran_geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {},
            "geometry": {
                "coordinates": [
                    [
                        [
                            42.85829482766377, 39.96191255432703
                        ],
                        [
                            42.85829482766377, 23.43075153081307
                        ],
                        [
                            63.86099644983949, 23.43075153081307
                        ],
                        [
                            63.86099644983949, 39.96191255432703
                        ],
                        [
                            42.85829482766377, 39.96191255432703
                        ]
                    ]
                ],
                "type": "Polygon"
            }
        }
    ]
}

fig.add_trace(go.Choroplethmapbox(
    geojson=iran_geojson,
    locations=[0],
    featureidkey="properties",
    z=[1],  
    colorscale="Viridis",
    showscale=True
))


fig.add_trace(go.Scattermapbox(
    lat=[city["lat"] for city in cities],
    lon=[city["lon"] for city in cities],
    mode='markers+text',
    marker=dict(size=[city["population"] / 350000 for city in cities], color="red", opacity=0.7),
    text=[f"{city['name']} ({city['population']:,})" for city in cities],
    textposition="top center"
))


fig.update_layout(
    mapbox_style="open-street-map"  ,
    mapbox_zoom=4 ,
    mapbox_center={"lat": 32.4279, "lon": 53.6880},
    title=" شهر پر جمعیت ایران ۱۰",
    width=900  ,
    height=600  ,
)


fig.write_image("plot.png")  


fig.show()
