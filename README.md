# An Explanatory Analysis of COVID-19 Focusing on the City of Chicago

## Overview
This project aims to analyze COVID-19's affect on the City of Chicago through different categories of citizens, such as age groups, gender (if-applicable), and race/ethnicity.  A project of this type can be used to study how a global pandemic affects the groups of citizens of a city like Chicago and if something similar were to happen, we can be better prepared to combat the deadly virus against our most at risk citizens.

Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.

Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.

The best way to prevent and slow down transmission is to be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face.

The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).

## Data Collection

* The two datasets were collected from the [Chicago Data Portal](https://data.cityofchicago.org/)
* The two datasets can be found here:
    * [Daily](https://data.cityofchicago.org/Health-Human-Services/Daily-Chicago-COVID-19-Cases-Deaths-and-Hospitaliz/kxzd-kd6a)
    * [Weekly by ZIP Code](https://data.cityofchicago.org/Health-Human-Services/COVID-19-Cases-Tests-and-Deaths-by-ZIP-Code/yhhz-zm2v/data)

## Methods of Analyzation

* Various graphs were constructed using matplotlib.pyplot, seaborn, and folium.  The most interesting visualization (linked below) highlights each ZIP Code of Chicago and what the total amount of cases were in that area as of December 23rd, 2020.

* Additionally the data required some minor cleaning such as extracting the coordinates of each ZIP Code from a single column.
* Feature Engineering was performed to highlight the Death Rate of Positive COVID cases (# of Deaths over # of Cases in a single day)
    * The average case-fatality ratio according to John Hopkins University is 1.8% for the United States, which is fairly close to our calculated value of about 2.8%
    * This new feature plotted against the Date column to see the rise and eventual fall of the COVID19 Mortality Rate in Chicago.

## Conclusion & Insights
* From this project, one can learn the drastic effects a disease like this will have on different groups of citizens of a city.  As you can below, the Bedford Park neighborhood of Chicago (ZIP: 60629) has the highest number of COVID cases as of 12/23/2020, with 13166 cases, however a much more centralized area of the city (ZIP: 60603) has the smallest number of COVID cases with only 46 cases.  I attribute this to the fact the former has a much less dense population and fewer amount of livable space (homes) in the area.
* Additionally, please feel free to look through the below visualizations I created and draw your own insights!







## Extra
As a test of my visualization ability, I also contracted the below Choropleth map that shows the Global Case Count of COVID19

<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.6.0/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_e680a2db117244adaac00b9aef042b84 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
</head>
<body>    
    
            <div class="folium-map" id="map_e680a2db117244adaac00b9aef042b84" ></div>
        
</body>
<script>    
    
            var map_e680a2db117244adaac00b9aef042b84 = L.map(
                "map_e680a2db117244adaac00b9aef042b84",
                {
                    center: [41.8781, -87.6298],
                    crs: L.CRS.EPSG3857,
                    zoom: 13,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );

            

        
    
            var tile_layer_ca6c121f39c940e4bc7212e6e5591e6c = L.tileLayer(
                "https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png",
                {"attribution": "\u0026copy; \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors \u0026copy; \u003ca href=\"http://cartodb.com/attributions\"\u003eCartoDB\u003c/a\u003e, CartoDB \u003ca href =\"http://cartodb.com/attributions\"\u003eattributions\u003c/a\u003e", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
            var circle_marker_7a1e7a51c7704f7098c8a19474e5df87 = L.circleMarker(
                [41.653147, -87.556037],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_7fa0af2fa5e64fe09c00517e34039fa3 = L.popup({"maxWidth": "100%"});

        
            var html_51e884a4ef914c69a0a11282c11c3dec = $(`<div id="html_51e884a4ef914c69a0a11282c11c3dec" style="width: 100.0%; height: 100.0%;">ZIP Code: 60633<br>Cases: 1036.0<br>Lat: -87.556037<br>Long: 41.653147<br></div>`)[0];
            popup_7fa0af2fa5e64fe09c00517e34039fa3.setContent(html_51e884a4ef914c69a0a11282c11c3dec);
        

        circle_marker_7a1e7a51c7704f7098c8a19474e5df87.bindPopup(popup_7fa0af2fa5e64fe09c00517e34039fa3)
        ;

        
    
    
            var circle_marker_e00177bb98684dbbb00b04ac8ed6091c = L.circleMarker(
                [41.721257, -87.556897],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_6a3dde66a0b244179683d0adf89856c8 = L.popup({"maxWidth": "100%"});

        
            var html_d1f7756f415c40328c53d3b272fffdc6 = $(`<div id="html_d1f7756f415c40328c53d3b272fffdc6" style="width: 100.0%; height: 100.0%;">ZIP Code: 60617<br>Cases: 5630.0<br>Lat: -87.556897<br>Long: 41.721257<br></div>`)[0];
            popup_6a3dde66a0b244179683d0adf89856c8.setContent(html_d1f7756f415c40328c53d3b272fffdc6);
        

        circle_marker_e00177bb98684dbbb00b04ac8ed6091c.bindPopup(popup_6a3dde66a0b244179683d0adf89856c8)
        ;

        
    
    
            var circle_marker_0780e72af135455ea57e68fdb1535b81 = L.circleMarker(
                [41.762202, -87.571522],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_caeddc1971d3400f8ff19cc0953053b3 = L.popup({"maxWidth": "100%"});

        
            var html_d938577c8fcc4280b5e0bcf8a6c47075 = $(`<div id="html_d938577c8fcc4280b5e0bcf8a6c47075" style="width: 100.0%; height: 100.0%;">ZIP Code: 60649<br>Cases: 2275.0<br>Lat: -87.571522<br>Long: 41.762202<br></div>`)[0];
            popup_caeddc1971d3400f8ff19cc0953053b3.setContent(html_d938577c8fcc4280b5e0bcf8a6c47075);
        

        circle_marker_0780e72af135455ea57e68fdb1535b81.bindPopup(popup_caeddc1971d3400f8ff19cc0953053b3)
        ;

        
    
    
            var circle_marker_35fd55c33d3046d8b24ae4ac310ea00c = L.circleMarker(
                [41.801993, -87.602725],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_580379a68b4f4441b93f7af7ac3b971a = L.popup({"maxWidth": "100%"});

        
            var html_7e97aa72265e4d68885109a98efae323 = $(`<div id="html_7e97aa72265e4d68885109a98efae323" style="width: 100.0%; height: 100.0%;">ZIP Code: 60615<br>Cases: 1537.0<br>Lat: -87.602725<br>Long: 41.801993<br></div>`)[0];
            popup_580379a68b4f4441b93f7af7ac3b971a.setContent(html_7e97aa72265e4d68885109a98efae323);
        

        circle_marker_35fd55c33d3046d8b24ae4ac310ea00c.bindPopup(popup_580379a68b4f4441b93f7af7ac3b971a)
        ;

        
    
    
            var circle_marker_322314784ef045e9982469e49d830ab6 = L.circleMarker(
                [41.780991, -87.604053],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_262b1906bde746389357b5828c707ac2 = L.popup({"maxWidth": "100%"});

        
            var html_66942640e23b4e6ca16b704fb95b0387 = $(`<div id="html_66942640e23b4e6ca16b704fb95b0387" style="width: 100.0%; height: 100.0%;">ZIP Code: 60637<br>Cases: 2267.0<br>Lat: -87.604053<br>Long: 41.780991<br></div>`)[0];
            popup_262b1906bde746389357b5828c707ac2.setContent(html_66942640e23b4e6ca16b704fb95b0387);
        

        circle_marker_322314784ef045e9982469e49d830ab6.bindPopup(popup_262b1906bde746389357b5828c707ac2)
        ;

        
    
    
            var circle_marker_6a1b5f39c99245829c5f72b5e36229d2 = L.circleMarker(
                [41.744737, -87.60569],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_c9729a2fc7fb4759acde7f573b1b0fe3 = L.popup({"maxWidth": "100%"});

        
            var html_bb67fdc1f094432a8cace442604610ad = $(`<div id="html_bb67fdc1f094432a8cace442604610ad" style="width: 100.0%; height: 100.0%;">ZIP Code: 60619<br>Cases: 3015.0<br>Lat: -87.60569<br>Long: 41.744737<br></div>`)[0];
            popup_c9729a2fc7fb4759acde7f573b1b0fe3.setContent(html_bb67fdc1f094432a8cace442604610ad);
        

        circle_marker_6a1b5f39c99245829c5f72b5e36229d2.bindPopup(popup_c9729a2fc7fb4759acde7f573b1b0fe3)
        ;

        
    
    
            var circle_marker_2756fbd2416a4e6882db15576d7421cd = L.circleMarker(
                [41.819261, -87.611244],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_994329b107b04584a17bfa830990b2ac = L.popup({"maxWidth": "100%"});

        
            var html_ae397151cf32463187022632bb1b38af = $(`<div id="html_ae397151cf32463187022632bb1b38af" style="width: 100.0%; height: 100.0%;">ZIP Code: 60653<br>Cases: 1765.0<br>Lat: -87.611244<br>Long: 41.819261<br></div>`)[0];
            popup_994329b107b04584a17bfa830990b2ac.setContent(html_ae397151cf32463187022632bb1b38af);
        

        circle_marker_2756fbd2416a4e6882db15576d7421cd.bindPopup(popup_994329b107b04584a17bfa830990b2ac)
        ;

        
    
    
            var circle_marker_752314aaef1447e0819a201086c07d5a = L.circleMarker(
                [41.894734, -87.620291],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_1bebb7ebd4fb452f99c22ec967498609 = L.popup({"maxWidth": "100%"});

        
            var html_74f57e23c7f743279a30bebe6a33bf96 = $(`<div id="html_74f57e23c7f743279a30bebe6a33bf96" style="width: 100.0%; height: 100.0%;">ZIP Code: 60611<br>Cases: 1456.0<br>Lat: -87.620291<br>Long: 41.894734<br></div>`)[0];
            popup_1bebb7ebd4fb452f99c22ec967498609.setContent(html_74f57e23c7f743279a30bebe6a33bf96);
        

        circle_marker_752314aaef1447e0819a201086c07d5a.bindPopup(popup_1bebb7ebd4fb452f99c22ec967498609)
        ;

        
    
    
            var circle_marker_0008f6b47b7a402ab0acd518ac83cc7b = L.circleMarker(
                [41.694192, -87.621537],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_7e4d26e47fe540409a3b5fb72b8646ba = L.popup({"maxWidth": "100%"});

        
            var html_5dbc63b0e12c4e22a210b08ef8f60ab9 = $(`<div id="html_5dbc63b0e12c4e22a210b08ef8f60ab9" style="width: 100.0%; height: 100.0%;">ZIP Code: 60628<br>Cases: 3520.0<br>Lat: -87.621537<br>Long: 41.694192<br></div>`)[0];
            popup_7e4d26e47fe540409a3b5fb72b8646ba.setContent(html_5dbc63b0e12c4e22a210b08ef8f60ab9);
        

        circle_marker_0008f6b47b7a402ab0acd518ac83cc7b.bindPopup(popup_7e4d26e47fe540409a3b5fb72b8646ba)
        ;

        
    
    
            var circle_marker_fc569694ee394629a5831df044f7a447 = L.circleMarker(
                [41.886262, -87.622844],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_6cc3e85cfe714008a1034da201d3214d = L.popup({"maxWidth": "100%"});

        
            var html_9e0904751b6f46568635f3f83ca5904c = $(`<div id="html_9e0904751b6f46568635f3f83ca5904c" style="width: 100.0%; height: 100.0%;">ZIP Code: 60601<br>Cases: 683.0<br>Lat: -87.622844<br>Long: 41.886262<br></div>`)[0];
            popup_6cc3e85cfe714008a1034da201d3214d.setContent(html_9e0904751b6f46568635f3f83ca5904c);
        

        circle_marker_fc569694ee394629a5831df044f7a447.bindPopup(popup_6cc3e85cfe714008a1034da201d3214d)
        ;

        
    
    
            var circle_marker_00560c1ccad3413aac5fb98b4ec11c09 = L.circleMarker(
                [41.867824, -87.623449],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_6683517e1b144d7c961efce8dd56096c = L.popup({"maxWidth": "100%"});

        
            var html_5eebb432526e414aafdf8703c0c44857 = $(`<div id="html_5eebb432526e414aafdf8703c0c44857" style="width: 100.0%; height: 100.0%;">ZIP Code: 60605<br>Cases: 1268.0<br>Lat: -87.623449<br>Long: 41.867824<br></div>`)[0];
            popup_6683517e1b144d7c961efce8dd56096c.setContent(html_5eebb432526e414aafdf8703c0c44857);
        

        circle_marker_00560c1ccad3413aac5fb98b4ec11c09.bindPopup(popup_6683517e1b144d7c961efce8dd56096c)
        ;

        
    
    
            var circle_marker_e7ac9f5ebbe1412fa974742c0e1e347d = L.circleMarker(
                [41.880112, -87.625473],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_8d0ee3bbb97047ffb2fec05b426ec227 = L.popup({"maxWidth": "100%"});

        
            var html_4dd28cf9b39a466195bb8627c2cd787d = $(`<div id="html_4dd28cf9b39a466195bb8627c2cd787d" style="width: 100.0%; height: 100.0%;">ZIP Code: 60603<br>Cases: 43.0<br>Lat: -87.625473<br>Long: 41.880112<br></div>`)[0];
            popup_8d0ee3bbb97047ffb2fec05b426ec227.setContent(html_4dd28cf9b39a466195bb8627c2cd787d);
        

        circle_marker_e7ac9f5ebbe1412fa974742c0e1e347d.bindPopup(popup_8d0ee3bbb97047ffb2fec05b426ec227)
        ;

        
    
    
            var circle_marker_73b59866a20047c88685260ffec45edd = L.circleMarker(
                [41.883136, -87.628309],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_a239d0d4e46641d9a9676ad5f2ec899a = L.popup({"maxWidth": "100%"});

        
            var html_cc71e824dc5b44f485e0a563c87f51c9 = $(`<div id="html_cc71e824dc5b44f485e0a563c87f51c9" style="width: 100.0%; height: 100.0%;">ZIP Code: 60602<br>Cases: 63.0<br>Lat: -87.628309<br>Long: 41.883136<br></div>`)[0];
            popup_a239d0d4e46641d9a9676ad5f2ec899a.setContent(html_cc71e824dc5b44f485e0a563c87f51c9);
        

        circle_marker_73b59866a20047c88685260ffec45edd.bindPopup(popup_a239d0d4e46641d9a9676ad5f2ec899a)
        ;

        
    
    
            var circle_marker_23d2802c26fa4006b05303f037321838 = L.circleMarker(
                [41.878153, -87.629029],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_d5b4d68cc010494fa5580fb791f000f3 = L.popup({"maxWidth": "100%"});

        
            var html_b68e2fd97508486eb9e8c6af6f3f71d1 = $(`<div id="html_b68e2fd97508486eb9e8c6af6f3f71d1" style="width: 100.0%; height: 100.0%;">ZIP Code: 60604<br>Cases: 74.0<br>Lat: -87.629029<br>Long: 41.878153<br></div>`)[0];
            popup_d5b4d68cc010494fa5580fb791f000f3.setContent(html_b68e2fd97508486eb9e8c6af6f3f71d1);
        

        circle_marker_23d2802c26fa4006b05303f037321838.bindPopup(popup_d5b4d68cc010494fa5580fb791f000f3)
        ;

        
    
    
            var circle_marker_89cbc301c2734de28d051e35643bab92 = L.circleMarker(
                [41.844869, -87.629531],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_cfeabcedeb434fdb87849eb4fd5dae3d = L.popup({"maxWidth": "100%"});

        
            var html_eba8af7291fe49c58949fd143568c67e = $(`<div id="html_eba8af7291fe49c58949fd143568c67e" style="width: 100.0%; height: 100.0%;">ZIP Code: 60616<br>Cases: 2431.0<br>Lat: -87.629531<br>Long: 41.844869<br></div>`)[0];
            popup_cfeabcedeb434fdb87849eb4fd5dae3d.setContent(html_eba8af7291fe49c58949fd143568c67e);
        

        circle_marker_89cbc301c2734de28d051e35643bab92.bindPopup(popup_cfeabcedeb434fdb87849eb4fd5dae3d)
        ;

        
    
    
            var circle_marker_0cc434043cc04601a73c5c50c1bbe9d9 = L.circleMarker(
                [41.650765, -87.633087],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_e495c6762eae49bea6d258f89e45979c = L.popup({"maxWidth": "100%"});

        
            var html_d2edcc6649324c5f9c1c94483d86e7ee = $(`<div id="html_d2edcc6649324c5f9c1c94483d86e7ee" style="width: 100.0%; height: 100.0%;">ZIP Code: 60827<br>Cases: 223.0<br>Lat: -87.633087<br>Long: 41.650765<br></div>`)[0];
            popup_e495c6762eae49bea6d258f89e45979c.setContent(html_d2edcc6649324c5f9c1c94483d86e7ee);
        

        circle_marker_0cc434043cc04601a73c5c50c1bbe9d9.bindPopup(popup_e495c6762eae49bea6d258f89e45979c)
        ;

        
    
    
            var circle_marker_e65057df6fd9438fa00acf0f27984c3a = L.circleMarker(
                [41.90455, -87.63581],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_ff57e26362d04fd6a55cddce9a6f80ef = L.popup({"maxWidth": "100%"});

        
            var html_af67d516bec64273adcce4e8246eadc9 = $(`<div id="html_af67d516bec64273adcce4e8246eadc9" style="width: 100.0%; height: 100.0%;">ZIP Code: 60610<br>Cases: 2111.0<br>Lat: -87.63581<br>Long: 41.90455<br></div>`)[0];
            popup_ff57e26362d04fd6a55cddce9a6f80ef.setContent(html_af67d516bec64273adcce4e8246eadc9);
        

        circle_marker_e65057df6fd9438fa00acf0f27984c3a.bindPopup(popup_ff57e26362d04fd6a55cddce9a6f80ef)
        ;

        
    
    
            var circle_marker_e19f113fae4641b5be96232acbd29eea = L.circleMarker(
                [41.892485, -87.636354],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_db7960921c2c4cc892ac023edb759287 = L.popup({"maxWidth": "100%"});

        
            var html_979c8a436bc74736be495a500c893912 = $(`<div id="html_979c8a436bc74736be495a500c893912" style="width: 100.0%; height: 100.0%;">ZIP Code: 60654<br>Cases: 1268.0<br>Lat: -87.636354<br>Long: 41.892485<br></div>`)[0];
            popup_db7960921c2c4cc892ac023edb759287.setContent(html_979c8a436bc74736be495a500c893912);
        

        circle_marker_e19f113fae4641b5be96232acbd29eea.bindPopup(popup_db7960921c2c4cc892ac023edb759287)
        ;

        
    
    
            var circle_marker_290be2d726654611b1bbf41a6fc611b8 = L.circleMarker(
                [41.882634, -87.63676],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_d91431ab673f420dbecbd180363402f9 = L.popup({"maxWidth": "100%"});

        
            var html_55f0ee28656e430b825d57679575bb5a = $(`<div id="html_55f0ee28656e430b825d57679575bb5a" style="width: 100.0%; height: 100.0%;">ZIP Code: 60606<br>Cases: 211.0<br>Lat: -87.63676<br>Long: 41.882634<br></div>`)[0];
            popup_d91431ab673f420dbecbd180363402f9.setContent(html_55f0ee28656e430b825d57679575bb5a);
        

        circle_marker_290be2d726654611b1bbf41a6fc611b8.bindPopup(popup_d91431ab673f420dbecbd180363402f9)
        ;

        
    
    
            var circle_marker_db92b0427fed4faeac8b2f0a6bfb7a3f = L.circleMarker(
                [41.776931, -87.638812],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_96c3060a49d64fd5b9a8f75e2f23b6f3 = L.popup({"maxWidth": "100%"});

        
            var html_62662ce62700457f95c5cac633c746ca = $(`<div id="html_62662ce62700457f95c5cac633c746ca" style="width: 100.0%; height: 100.0%;">ZIP Code: 60621<br>Cases: 1582.0<br>Lat: -87.638812<br>Long: 41.776931<br></div>`)[0];
            popup_96c3060a49d64fd5b9a8f75e2f23b6f3.setContent(html_62662ce62700457f95c5cac633c746ca);
        

        circle_marker_db92b0427fed4faeac8b2f0a6bfb7a3f.bindPopup(popup_96c3060a49d64fd5b9a8f75e2f23b6f3)
        ;

        
    
    
            var circle_marker_146858f82a8e4bdf8024be26bedfdc74 = L.circleMarker(
                [41.882786, -87.644283],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_9ce720e0d0ba47bab3dec1484dca5c51 = L.popup({"maxWidth": "100%"});

        
            var html_07aabc7590754854bfa9308c1719e040 = $(`<div id="html_07aabc7590754854bfa9308c1719e040" style="width: 100.0%; height: 100.0%;">ZIP Code: 60661<br>Cases: 505.0<br>Lat: -87.644283<br>Long: 41.882786<br></div>`)[0];
            popup_9ce720e0d0ba47bab3dec1484dca5c51.setContent(html_07aabc7590754854bfa9308c1719e040);
        

        circle_marker_146858f82a8e4bdf8024be26bedfdc74.bindPopup(popup_9ce720e0d0ba47bab3dec1484dca5c51)
        ;

        
    
    
            var circle_marker_d81a47fc53ba406aaab65cbd8a94a912 = L.circleMarker(
                [41.740873, -87.651656],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_0673aa5292184419b84141af510a028e = L.popup({"maxWidth": "100%"});

        
            var html_1a239ef86d1e4e0087f2639ea6f1790f = $(`<div id="html_1a239ef86d1e4e0087f2639ea6f1790f" style="width: 100.0%; height: 100.0%;">ZIP Code: 60620<br>Cases: 3606.0<br>Lat: -87.651656<br>Long: 41.740873<br></div>`)[0];
            popup_0673aa5292184419b84141af510a028e.setContent(html_1a239ef86d1e4e0087f2639ea6f1790f);
        

        circle_marker_d81a47fc53ba406aaab65cbd8a94a912.bindPopup(popup_0673aa5292184419b84141af510a028e)
        ;

        
    
    
            var circle_marker_62ca9ace05a44fc7873a68a49a41a5c0 = L.circleMarker(
                [41.922605, -87.652064],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_ab1eef7bbe7c46ad83081fd776034a21 = L.popup({"maxWidth": "100%"});

        
            var html_ccbce341d1bc45b99f3fb4cf36675e9f = $(`<div id="html_ccbce341d1bc45b99f3fb4cf36675e9f" style="width: 100.0%; height: 100.0%;">ZIP Code: 60614<br>Cases: 3429.0<br>Lat: -87.652064<br>Long: 41.922605<br></div>`)[0];
            popup_ab1eef7bbe7c46ad83081fd776034a21.setContent(html_ccbce341d1bc45b99f3fb4cf36675e9f);
        

        circle_marker_62ca9ace05a44fc7873a68a49a41a5c0.bindPopup(popup_ab1eef7bbe7c46ad83081fd776034a21)
        ;

        
    
    
            var circle_marker_8ca90e9883754aa68e84778faa40b9cb = L.circleMarker(
                [41.876104, -87.652727],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_81e96b239b3e4a7a9b16bf6723238ca5 = L.popup({"maxWidth": "100%"});

        
            var html_6696e3756e084ee4938b4a67f46aeff6 = $(`<div id="html_6696e3756e084ee4938b4a67f46aeff6" style="width: 100.0%; height: 100.0%;">ZIP Code: 60607<br>Cases: 1731.0<br>Lat: -87.652727<br>Long: 41.876104<br></div>`)[0];
            popup_81e96b239b3e4a7a9b16bf6723238ca5.setContent(html_6696e3756e084ee4938b4a67f46aeff6);
        

        circle_marker_8ca90e9883754aa68e84778faa40b9cb.bindPopup(popup_81e96b239b3e4a7a9b16bf6723238ca5)
        ;

        
    
    
            var circle_marker_1c979fbe612e43388fe124dbf61b908a = L.circleMarker(
                [41.812017, -87.653382],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_839080e5831a4c539d616456ecea2f8c = L.popup({"maxWidth": "100%"});

        
            var html_6be613cb3e16462bb5901c451df44ec0 = $(`<div id="html_6be613cb3e16462bb5901c451df44ec0" style="width: 100.0%; height: 100.0%;">ZIP Code: 60609<br>Cases: 5399.0<br>Lat: -87.653382<br>Long: 41.812017<br></div>`)[0];
            popup_839080e5831a4c539d616456ecea2f8c.setContent(html_6be613cb3e16462bb5901c451df44ec0);
        

        circle_marker_1c979fbe612e43388fe124dbf61b908a.bindPopup(popup_839080e5831a4c539d616456ecea2f8c)
        ;

        
    
    
            var circle_marker_fb7c4ed0f9304e5885d844a52210376a = L.circleMarker(
                [41.899935, -87.657821],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_0d76eb0bcad44e53b5edeb6f11bd7409 = L.popup({"maxWidth": "100%"});

        
            var html_791dc1f654b84d63a5c303ee19448859 = $(`<div id="html_791dc1f654b84d63a5c303ee19448859" style="width: 100.0%; height: 100.0%;">ZIP Code: 60642<br>Cases: 1255.0<br>Lat: -87.657821<br>Long: 41.899935<br></div>`)[0];
            popup_0d76eb0bcad44e53b5edeb6f11bd7409.setContent(html_791dc1f654b84d63a5c303ee19448859);
        

        circle_marker_fb7c4ed0f9304e5885d844a52210376a.bindPopup(popup_0d76eb0bcad44e53b5edeb6f11bd7409)
        ;

        
    
    
            var circle_marker_c92dad333e0944d696e0eaa6fc69e28a = L.circleMarker(
                [41.939715, -87.658216],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_1e89bb9816df422c95df08f1efe42419 = L.popup({"maxWidth": "100%"});

        
            var html_5d6a9059ab2847d3a19c92e5fec69bf0 = $(`<div id="html_5d6a9059ab2847d3a19c92e5fec69bf0" style="width: 100.0%; height: 100.0%;">ZIP Code: 60657<br>Cases: 3150.0<br>Lat: -87.658216<br>Long: 41.939715<br></div>`)[0];
            popup_1e89bb9816df422c95df08f1efe42419.setContent(html_5d6a9059ab2847d3a19c92e5fec69bf0);
        

        circle_marker_c92dad333e0944d696e0eaa6fc69e28a.bindPopup(popup_1e89bb9816df422c95df08f1efe42419)
        ;

        
    
    
            var circle_marker_2694f64998b94df28d4823ac0d2f520c = L.circleMarker(
                [41.953742, -87.661343],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_35e277b2f2fc487997e0b666264cdd85 = L.popup({"maxWidth": "100%"});

        
            var html_0ef3213c479545d1bc83e3e49a3d178c = $(`<div id="html_0ef3213c479545d1bc83e3e49a3d178c" style="width: 100.0%; height: 100.0%;">ZIP Code: 60613<br>Cases: 2418.0<br>Lat: -87.661343<br>Long: 41.953742<br></div>`)[0];
            popup_35e277b2f2fc487997e0b666264cdd85.setContent(html_0ef3213c479545d1bc83e3e49a3d178c);
        

        circle_marker_2694f64998b94df28d4823ac0d2f520c.bindPopup(popup_35e277b2f2fc487997e0b666264cdd85)
        ;

        
    
    
            var circle_marker_684256835bef4a11916d46da27241398 = L.circleMarker(
                [41.971888, -87.662232],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_0a482025395c498890456e212b7da644 = L.popup({"maxWidth": "100%"});

        
            var html_e57d5637446c467d9476367b4316c485 = $(`<div id="html_e57d5637446c467d9476367b4316c485" style="width: 100.0%; height: 100.0%;">ZIP Code: 60640<br>Cases: 2951.0<br>Lat: -87.662232<br>Long: 41.971888<br></div>`)[0];
            popup_0a482025395c498890456e212b7da644.setContent(html_e57d5637446c467d9476367b4316c485);
        

        circle_marker_684256835bef4a11916d46da27241398.bindPopup(popup_0a482025395c498890456e212b7da644)
        ;

        
    
    
            var circle_marker_935057e46748434b81e2d28e2ba1c40f = L.circleMarker(
                [41.700445, -87.662381],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_094995669000430591e01bb0a786eb10 = L.popup({"maxWidth": "100%"});

        
            var html_47a140a41c884033a10d5ddd387bd9c0 = $(`<div id="html_47a140a41c884033a10d5ddd387bd9c0" style="width: 100.0%; height: 100.0%;">ZIP Code: 60643<br>Cases: 2929.0<br>Lat: -87.662381<br>Long: 41.700445<br></div>`)[0];
            popup_094995669000430591e01bb0a786eb10.setContent(html_47a140a41c884033a10d5ddd387bd9c0);
        

        circle_marker_935057e46748434b81e2d28e2ba1c40f.bindPopup(popup_094995669000430591e01bb0a786eb10)
        ;

        
    
    
            var circle_marker_767200e7cb774cf7b420acb2d3c6cb9e = L.circleMarker(
                [41.991062, -87.666362],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_a54e5f505ce74ea7bae20ef706316112 = L.popup({"maxWidth": "100%"});

        
            var html_33a1d41ca12b49aa977e6082fa94ada2 = $(`<div id="html_33a1d41ca12b49aa977e6082fa94ada2" style="width: 100.0%; height: 100.0%;">ZIP Code: 60660<br>Cases: 1797.0<br>Lat: -87.666362<br>Long: 41.991062<br></div>`)[0];
            popup_a54e5f505ce74ea7bae20ef706316112.setContent(html_33a1d41ca12b49aa977e6082fa94ada2);
        

        circle_marker_767200e7cb774cf7b420acb2d3c6cb9e.bindPopup(popup_a54e5f505ce74ea7bae20ef706316112)
        ;

        
    
    
            var circle_marker_343e8040e4b94b0381a81ecd06b0de8c = L.circleMarker(
                [41.77599, -87.668597],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_083d3f2923404af4beb89f3a306ab47b = L.popup({"maxWidth": "100%"});

        
            var html_fcc43fc3e77847929a38f18362bc0a1e = $(`<div id="html_fcc43fc3e77847929a38f18362bc0a1e" style="width: 100.0%; height: 100.0%;">ZIP Code: 60636<br>Cases: 2306.0<br>Lat: -87.668597<br>Long: 41.77599<br></div>`)[0];
            popup_083d3f2923404af4beb89f3a306ab47b.setContent(html_fcc43fc3e77847929a38f18362bc0a1e);
        

        circle_marker_343e8040e4b94b0381a81ecd06b0de8c.bindPopup(popup_083d3f2923404af4beb89f3a306ab47b)
        ;

        
    
    
            var circle_marker_e7f3d0348abd48a19a25515aa8306023 = L.circleMarker(
                [42.009469, -87.669834],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_a126cfe34028493c936551e103133ac6 = L.popup({"maxWidth": "100%"});

        
            var html_33b9e8c5e9074d3fa367210ab030c616 = $(`<div id="html_33b9e8c5e9074d3fa367210ab030c616" style="width: 100.0%; height: 100.0%;">ZIP Code: 60626<br>Cases: 2937.0<br>Lat: -87.669834<br>Long: 42.009469<br></div>`)[0];
            popup_a126cfe34028493c936551e103133ac6.setContent(html_33b9e8c5e9074d3fa367210ab030c616);
        

        circle_marker_e7f3d0348abd48a19a25515aa8306023.bindPopup(popup_a126cfe34028493c936551e103133ac6)
        ;

        
    
    
            var circle_marker_1a8d56d0f4d84d0f946a443271077849 = L.circleMarker(
                [41.849879, -87.670366],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_d160d633e41f4c33a44c748edfb8ef5b = L.popup({"maxWidth": "100%"});

        
            var html_6039348be2944505a294ed51252f3555 = $(`<div id="html_6039348be2944505a294ed51252f3555" style="width: 100.0%; height: 100.0%;">ZIP Code: 60608<br>Cases: 6099.0<br>Lat: -87.670366<br>Long: 41.849879<br></div>`)[0];
            popup_d160d633e41f4c33a44c748edfb8ef5b.setContent(html_6039348be2944505a294ed51252f3555);
        

        circle_marker_1a8d56d0f4d84d0f946a443271077849.bindPopup(popup_d160d633e41f4c33a44c748edfb8ef5b)
        ;

        
    
    
            var circle_marker_ab6c76f8f15c4670be73237b1e45cf59 = L.circleMarker(
                [41.902762, -87.681818],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_f60c6d2815e2486e8a28111c02de132b = L.popup({"maxWidth": "100%"});

        
            var html_71a32ade768f49d4b1ba7670ce17af13 = $(`<div id="html_71a32ade768f49d4b1ba7670ce17af13" style="width: 100.0%; height: 100.0%;">ZIP Code: 60622<br>Cases: 3287.0<br>Lat: -87.681818<br>Long: 41.902762<br></div>`)[0];
            popup_f60c6d2815e2486e8a28111c02de132b.setContent(html_71a32ade768f49d4b1ba7670ce17af13);
        

        circle_marker_ab6c76f8f15c4670be73237b1e45cf59.bindPopup(popup_f60c6d2815e2486e8a28111c02de132b)
        ;

        
    
    
            var circle_marker_c069229abfde4aa98025740be7ed3c59 = L.circleMarker(
                [41.88004, -87.687011],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_dc4573b075db4fd7ae6d1ddf9d84b2be = L.popup({"maxWidth": "100%"});

        
            var html_b8aba121c5454da2b0f17b950c46629e = $(`<div id="html_b8aba121c5454da2b0f17b950c46629e" style="width: 100.0%; height: 100.0%;">ZIP Code: 60612<br>Cases: 2534.0<br>Lat: -87.687011<br>Long: 41.88004<br></div>`)[0];
            popup_dc4573b075db4fd7ae6d1ddf9d84b2be.setContent(html_b8aba121c5454da2b0f17b950c46629e);
        

        circle_marker_c069229abfde4aa98025740be7ed3c59.bindPopup(popup_dc4573b075db4fd7ae6d1ddf9d84b2be)
        ;

        
    
    
            var circle_marker_ebdfa409ce31458cb744970a7b71a38b = L.circleMarker(
                [42.008927, -87.695049],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_1dbd9c8262e749bba10ae292df5119fe = L.popup({"maxWidth": "100%"});

        
            var html_49195bf6ff9c481793df4d936125dc35 = $(`<div id="html_49195bf6ff9c481793df4d936125dc35" style="width: 100.0%; height: 100.0%;">ZIP Code: 60645<br>Cases: 3220.0<br>Lat: -87.695049<br>Long: 42.008927<br></div>`)[0];
            popup_1dbd9c8262e749bba10ae292df5119fe.setContent(html_49195bf6ff9c481793df4d936125dc35);
        

        circle_marker_ebdfa409ce31458cb744970a7b71a38b.bindPopup(popup_1dbd9c8262e749bba10ae292df5119fe)
        ;

        
    
    
            var circle_marker_4c68c67c7fcb41559988f2fc639937c9 = L.circleMarker(
                [41.921058, -87.701101],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_704266deb3c74c38ab5437f7c043c3c6 = L.popup({"maxWidth": "100%"});

        
            var html_6891cd4f9151468a965807c6a08583d8 = $(`<div id="html_6891cd4f9151468a965807c6a08583d8" style="width: 100.0%; height: 100.0%;">ZIP Code: 60647<br>Cases: 5944.0<br>Lat: -87.701101<br>Long: 41.921058<br></div>`)[0];
            popup_704266deb3c74c38ab5437f7c043c3c6.setContent(html_6891cd4f9151468a965807c6a08583d8);
        

        circle_marker_4c68c67c7fcb41559988f2fc639937c9.bindPopup(popup_704266deb3c74c38ab5437f7c043c3c6)
        ;

        
    
    
            var circle_marker_6b0c7adb6f2d413ab0585e1c11a15cc1 = L.circleMarker(
                [41.696456, -87.701434],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_2eb823938a4b4f7d964971e7848894c7 = L.popup({"maxWidth": "100%"});

        
            var html_b10e276cbb734c6eb2a85600a8341663 = $(`<div id="html_b10e276cbb734c6eb2a85600a8341663" style="width: 100.0%; height: 100.0%;">ZIP Code: 60655<br>Cases: 2298.0<br>Lat: -87.701434<br>Long: 41.696456<br></div>`)[0];
            popup_2eb823938a4b4f7d964971e7848894c7.setContent(html_b10e276cbb734c6eb2a85600a8341663);
        

        circle_marker_6b0c7adb6f2d413ab0585e1c11a15cc1.bindPopup(popup_2eb823938a4b4f7d964971e7848894c7)
        ;

        
    
    
            var circle_marker_fb291b9deb734afdadf3f1bef2e4e32e = L.circleMarker(
                [41.971155, -87.701816],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_fbe3978e9f9f49038267473f8914ddac = L.popup({"maxWidth": "100%"});

        
            var html_55806d217a294f509dccebcda4a136fb = $(`<div id="html_55806d217a294f509dccebcda4a136fb" style="width: 100.0%; height: 100.0%;">ZIP Code: 60625<br>Cases: 4827.0<br>Lat: -87.701816<br>Long: 41.971155<br></div>`)[0];
            popup_fbe3978e9f9f49038267473f8914ddac.setContent(html_55806d217a294f509dccebcda4a136fb);
        

        circle_marker_fb291b9deb734afdadf3f1bef2e4e32e.bindPopup(popup_fbe3978e9f9f49038267473f8914ddac)
        ;

        
    
    
            var circle_marker_8bd2f77029444a10b9478bde610f7871 = L.circleMarker(
                [41.990803, -87.703266],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_054e2272cb1246bb9ad503f0c9f56828 = L.popup({"maxWidth": "100%"});

        
            var html_d083c07effdc43e6b16c2b591dbfbb7d = $(`<div id="html_d083c07effdc43e6b16c2b591dbfbb7d" style="width: 100.0%; height: 100.0%;">ZIP Code: 60659<br>Cases: 2761.0<br>Lat: -87.703266<br>Long: 41.990803<br></div>`)[0];
            popup_054e2272cb1246bb9ad503f0c9f56828.setContent(html_d083c07effdc43e6b16c2b591dbfbb7d);
        

        circle_marker_8bd2f77029444a10b9478bde610f7871.bindPopup(popup_054e2272cb1246bb9ad503f0c9f56828)
        ;

        
    
    
            var circle_marker_5663a3d4255a4e3ab96abf23742d3490 = L.circleMarker(
                [41.946699, -87.703343],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_ca28aa3c51ca4da9aa3a5176b64d9f3d = L.popup({"maxWidth": "100%"});

        
            var html_c09a125ad85746caa4a75a7470f96261 = $(`<div id="html_c09a125ad85746caa4a75a7470f96261" style="width: 100.0%; height: 100.0%;">ZIP Code: 60618<br>Cases: 5609.0<br>Lat: -87.703343<br>Long: 41.946699<br></div>`)[0];
            popup_ca28aa3c51ca4da9aa3a5176b64d9f3d.setContent(html_c09a125ad85746caa4a75a7470f96261);
        

        circle_marker_5663a3d4255a4e3ab96abf23742d3490.bindPopup(popup_ca28aa3c51ca4da9aa3a5176b64d9f3d)
        ;

        
    
    
            var circle_marker_3247d7214d434fa69ac3246cbc773084 = L.circleMarker(
                [41.810038, -87.711251],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_f47de9ff8c83425d9f7ce2b3344b11a7 = L.popup({"maxWidth": "100%"});

        
            var html_34abfb652a9146fead792948b01c2bd0 = $(`<div id="html_34abfb652a9146fead792948b01c2bd0" style="width: 100.0%; height: 100.0%;">ZIP Code: 60632<br>Cases: 10281.0<br>Lat: -87.711251<br>Long: 41.810038<br></div>`)[0];
            popup_f47de9ff8c83425d9f7ce2b3344b11a7.setContent(html_34abfb652a9146fead792948b01c2bd0);
        

        circle_marker_3247d7214d434fa69ac3246cbc773084.bindPopup(popup_f47de9ff8c83425d9f7ce2b3344b11a7)
        ;

        
    
    
            var circle_marker_f876da119cd54dbfaebcaf27689fffdb = L.circleMarker(
                [41.777061, -87.711565],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_be9c617fe5ae45068909432068441b5f = L.popup({"maxWidth": "100%"});

        
            var html_d225f4d8e6eb490daa975182b15b3f01 = $(`<div id="html_d225f4d8e6eb490daa975182b15b3f01" style="width: 100.0%; height: 100.0%;">ZIP Code: 60629<br>Cases: 13166.0<br>Lat: -87.711565<br>Long: 41.777061<br></div>`)[0];
            popup_be9c617fe5ae45068909432068441b5f.setContent(html_d225f4d8e6eb490daa975182b15b3f01);
        

        circle_marker_f876da119cd54dbfaebcaf27689fffdb.bindPopup(popup_be9c617fe5ae45068909432068441b5f)
        ;

        
    
    
            var circle_marker_d1a0d3985c81474388d7bcf2e722abcb = L.circleMarker(
                [41.745398, -87.714238],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_477de88c7b624bc383c16df0cce88620 = L.popup({"maxWidth": "100%"});

        
            var html_7ffaf5c91d1b4351b9759f39c1c6a020 = $(`<div id="html_7ffaf5c91d1b4351b9759f39c1c6a020" style="width: 100.0%; height: 100.0%;">ZIP Code: 60652<br>Cases: 3825.0<br>Lat: -87.714238<br>Long: 41.745398<br></div>`)[0];
            popup_477de88c7b624bc383c16df0cce88620.setContent(html_7ffaf5c91d1b4351b9759f39c1c6a020);
        

        circle_marker_d1a0d3985c81474388d7bcf2e722abcb.bindPopup(popup_477de88c7b624bc383c16df0cce88620)
        ;

        
    
    
            var circle_marker_0ad38b2912e64b6da9b8670612d1f016 = L.circleMarker(
                [41.850321, -87.717446],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_82aeffc2c4d147669914786d0ef756d2 = L.popup({"maxWidth": "100%"});

        
            var html_8323fe38ed554765b156878c1b1d1453 = $(`<div id="html_8323fe38ed554765b156878c1b1d1453" style="width: 100.0%; height: 100.0%;">ZIP Code: 60623<br>Cases: 8627.0<br>Lat: -87.717446<br>Long: 41.850321<br></div>`)[0];
            popup_82aeffc2c4d147669914786d0ef756d2.setContent(html_8323fe38ed554765b156878c1b1d1453);
        

        circle_marker_0ad38b2912e64b6da9b8670612d1f016.bindPopup(popup_82aeffc2c4d147669914786d0ef756d2)
        ;

        
    
    
            var circle_marker_6ceeeb9738ae4ef2bed8ab2eb7c01508 = L.circleMarker(
                [41.879417, -87.722735],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_5de5b66c9ee24803a4b976b38e0fd458 = L.popup({"maxWidth": "100%"});

        
            var html_cd0465ef670c406aa1868f674c195f09 = $(`<div id="html_cd0465ef670c406aa1868f674c195f09" style="width: 100.0%; height: 100.0%;">ZIP Code: 60624<br>Cases: 2354.0<br>Lat: -87.722735<br>Long: 41.879417<br></div>`)[0];
            popup_5de5b66c9ee24803a4b976b38e0fd458.setContent(html_cd0465ef670c406aa1868f674c195f09);
        

        circle_marker_6ceeeb9738ae4ef2bed8ab2eb7c01508.bindPopup(popup_5de5b66c9ee24803a4b976b38e0fd458)
        ;

        
    
    
            var circle_marker_00d8dd68b5944316bca17a296860ab87 = L.circleMarker(
                [41.901964, -87.741017],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_1b42f89f869447908c4294267310519f = L.popup({"maxWidth": "100%"});

        
            var html_ec019e67c9ed4ddca02d1f7ea30c25e3 = $(`<div id="html_ec019e67c9ed4ddca02d1f7ea30c25e3" style="width: 100.0%; height: 100.0%;">ZIP Code: 60651<br>Cases: 5654.0<br>Lat: -87.741017<br>Long: 41.901964<br></div>`)[0];
            popup_1b42f89f869447908c4294267310519f.setContent(html_ec019e67c9ed4ddca02d1f7ea30c25e3);
        

        circle_marker_00d8dd68b5944316bca17a296860ab87.bindPopup(popup_1b42f89f869447908c4294267310519f)
        ;

        
    
    
            var circle_marker_de79a2119c9f4cafa8ed98b6e86a1c2b = L.circleMarker(
                [41.946682, -87.746791],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_749e1b1adae04c4f8da85fc81c15d766 = L.popup({"maxWidth": "100%"});

        
            var html_8d049de4b7c34b00beec47aa14419419 = $(`<div id="html_8d049de4b7c34b00beec47aa14419419" style="width: 100.0%; height: 100.0%;">ZIP Code: 60641<br>Cases: 6293.0<br>Lat: -87.746791<br>Long: 41.946682<br></div>`)[0];
            popup_749e1b1adae04c4f8da85fc81c15d766.setContent(html_8d049de4b7c34b00beec47aa14419419);
        

        circle_marker_de79a2119c9f4cafa8ed98b6e86a1c2b.bindPopup(popup_749e1b1adae04c4f8da85fc81c15d766)
        ;

        
    
    
            var circle_marker_ac6e5b9f433e4d73ba92d8e8413b77b3 = L.circleMarker(
                [41.920609, -87.75531],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_53637800fb524b7d90a5cf3ba5b2c24d = L.popup({"maxWidth": "100%"});

        
            var html_f5bb50072bcd461b87c39fc7c139d4e8 = $(`<div id="html_f5bb50072bcd461b87c39fc7c139d4e8" style="width: 100.0%; height: 100.0%;">ZIP Code: 60639<br>Cases: 10835.0<br>Lat: -87.75531<br>Long: 41.920609<br></div>`)[0];
            popup_53637800fb524b7d90a5cf3ba5b2c24d.setContent(html_f5bb50072bcd461b87c39fc7c139d4e8);
        

        circle_marker_ac6e5b9f433e4d73ba92d8e8413b77b3.bindPopup(popup_53637800fb524b7d90a5cf3ba5b2c24d)
        ;

        
    
    
            var circle_marker_af9c51d54c35430ca01173054e9c3ed1 = L.circleMarker(
                [41.881113, -87.756863],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_c2b7bec5990e4c708cf76d75f3b6aceb = L.popup({"maxWidth": "100%"});

        
            var html_5febd7ec8f1647a8b1c1397868cfa659 = $(`<div id="html_5febd7ec8f1647a8b1c1397868cfa659" style="width: 100.0%; height: 100.0%;">ZIP Code: 60644<br>Cases: 3009.0<br>Lat: -87.756863<br>Long: 41.881113<br></div>`)[0];
            popup_c2b7bec5990e4c708cf76d75f3b6aceb.setContent(html_5febd7ec8f1647a8b1c1397868cfa659);
        

        circle_marker_af9c51d54c35430ca01173054e9c3ed1.bindPopup(popup_c2b7bec5990e4c708cf76d75f3b6aceb)
        ;

        
    
    
            var circle_marker_73aa51576a62457bbd3100e18fb87d75 = L.circleMarker(
                [41.971261, -87.759611],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_04508f9fdaca48be956b425e0e6a6e39 = L.popup({"maxWidth": "100%"});

        
            var html_28c5834faba54c4690dbe12b317df1c6 = $(`<div id="html_28c5834faba54c4690dbe12b317df1c6" style="width: 100.0%; height: 100.0%;">ZIP Code: 60630<br>Cases: 3700.0<br>Lat: -87.759611<br>Long: 41.971261<br></div>`)[0];
            popup_04508f9fdaca48be956b425e0e6a6e39.setContent(html_28c5834faba54c4690dbe12b317df1c6);
        

        circle_marker_73aa51576a62457bbd3100e18fb87d75.bindPopup(popup_04508f9fdaca48be956b425e0e6a6e39)
        ;

        
    
    
            var circle_marker_882df491ec5d4377bd2dcf5fff4d0137 = L.circleMarker(
                [41.993931, -87.761826],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_329bc571efd648149cdd67fa4c4a6622 = L.popup({"maxWidth": "100%"});

        
            var html_8eb42b7d99a34e90b0a362018077916f = $(`<div id="html_8eb42b7d99a34e90b0a362018077916f" style="width: 100.0%; height: 100.0%;">ZIP Code: 60646<br>Cases: 1666.0<br>Lat: -87.761826<br>Long: 41.993931<br></div>`)[0];
            popup_329bc571efd648149cdd67fa4c4a6622.setContent(html_8eb42b7d99a34e90b0a362018077916f);
        

        circle_marker_882df491ec5d4377bd2dcf5fff4d0137.bindPopup(popup_329bc571efd648149cdd67fa4c4a6622)
        ;

        
    
    
            var circle_marker_d165b8750169496b88f226f143c28587 = L.circleMarker(
                [41.787032, -87.771902],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_04aa2bb8242643f8a7c66e4221e93af9 = L.popup({"maxWidth": "100%"});

        
            var html_ab82c2d3f572445e96aa4fb90ea78a96 = $(`<div id="html_ab82c2d3f572445e96aa4fb90ea78a96" style="width: 100.0%; height: 100.0%;">ZIP Code: 60638<br>Cases: 5678.0<br>Lat: -87.771902<br>Long: 41.787032<br></div>`)[0];
            popup_04aa2bb8242643f8a7c66e4221e93af9.setContent(html_ab82c2d3f572445e96aa4fb90ea78a96);
        

        circle_marker_d165b8750169496b88f226f143c28587.bindPopup(popup_04aa2bb8242643f8a7c66e4221e93af9)
        ;

        
    
    
            var circle_marker_1b78303d90904c69af18367f42efd659 = L.circleMarker(
                [41.944967, -87.797373],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_4a996e0b4d1d4f3cac52b0b10c3c0b6a = L.popup({"maxWidth": "100%"});

        
            var html_08f6ba4290d246d59c3eba8134a06cf0 = $(`<div id="html_08f6ba4290d246d59c3eba8134a06cf0" style="width: 100.0%; height: 100.0%;">ZIP Code: 60634<br>Cases: 7032.0<br>Lat: -87.797373<br>Long: 41.944967<br></div>`)[0];
            popup_4a996e0b4d1d4f3cac52b0b10c3c0b6a.setContent(html_08f6ba4290d246d59c3eba8134a06cf0);
        

        circle_marker_1b78303d90904c69af18367f42efd659.bindPopup(popup_4a996e0b4d1d4f3cac52b0b10c3c0b6a)
        ;

        
    
    
            var circle_marker_b1f26fce00ae4569a63c2388c6c9d54b = L.circleMarker(
                [41.921777, -87.808283],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_a002f8a1ca05443a88e5cb36f263d5ee = L.popup({"maxWidth": "100%"});

        
            var html_a8e5726382464cfcbf67a5a95d4bb168 = $(`<div id="html_a8e5726382464cfcbf67a5a95d4bb168" style="width: 100.0%; height: 100.0%;">ZIP Code: 60707<br>Cases: 1664.0<br>Lat: -87.808283<br>Long: 41.921777<br></div>`)[0];
            popup_a002f8a1ca05443a88e5cb36f263d5ee.setContent(html_a8e5726382464cfcbf67a5a95d4bb168);
        

        circle_marker_b1f26fce00ae4569a63c2388c6c9d54b.bindPopup(popup_a002f8a1ca05443a88e5cb36f263d5ee)
        ;

        
    
    
            var circle_marker_4fdceb4a236a41d6b860a00e166f5db0 = L.circleMarker(
                [41.995019, -87.813371],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_844efe7a8632454696b6584804c14a1d = L.popup({"maxWidth": "100%"});

        
            var html_54bcf039f41348d39fae2ebd02cabf1a = $(`<div id="html_54bcf039f41348d39fae2ebd02cabf1a" style="width: 100.0%; height: 100.0%;">ZIP Code: 60631<br>Cases: 1982.0<br>Lat: -87.813371<br>Long: 41.995019<br></div>`)[0];
            popup_844efe7a8632454696b6584804c14a1d.setContent(html_54bcf039f41348d39fae2ebd02cabf1a);
        

        circle_marker_4fdceb4a236a41d6b860a00e166f5db0.bindPopup(popup_844efe7a8632454696b6584804c14a1d)
        ;

        
    
    
            var circle_marker_1390dff9214a4b21ba074bb311831569 = L.circleMarker(
                [41.974566, -87.817934],
                {"bubblingMouseEvents": true, "color": "crimson", "dashArray": null, "dashOffset": null, "fill": true, "fillColor": "crimson", "fillOpacity": 0.2, "fillRule": "evenodd", "lineCap": "round", "lineJoin": "round", "opacity": 1.0, "radius": 100, "stroke": true, "weight": 3}
            ).addTo(map_e680a2db117244adaac00b9aef042b84);
        
    
        var popup_f2c508b47b2342b796172573ca263c5d = L.popup({"maxWidth": "100%"});

        
            var html_ff5b5db28e734426860ca3565f859353 = $(`<div id="html_ff5b5db28e734426860ca3565f859353" style="width: 100.0%; height: 100.0%;">ZIP Code: 60656<br>Cases: 1983.0<br>Lat: -87.817934<br>Long: 41.974566<br></div>`)[0];
            popup_f2c508b47b2342b796172573ca263c5d.setContent(html_ff5b5db28e734426860ca3565f859353);
        

        circle_marker_1390dff9214a4b21ba074bb311831569.bindPopup(popup_f2c508b47b2342b796172573ca263c5d)
        ;
